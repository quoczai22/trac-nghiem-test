import fs from "fs/promises";
import path from "path";
import mammoth from "mammoth";

const PROJECT_ROOT = path.resolve("C:/Users/kienq/Documents/Codex/2026-06-15/https-tracnghiemhuit-onrender-com-de-cuong/publish_trac_nghiem_test");
const OUTPUT_DIR = path.join(PROJECT_ROOT, "subjects", "anh-van-3");
const OUTPUT_FILE = path.join(OUTPUT_DIR, "questions.js");
const HELPER_URL = process.env.OLLAMA_HELPER_URL || "http://localhost:3100";
const MODEL = process.env.OLLAMA_MODEL || "qwen2.5:7b";

const SOURCES = [
  {
    label: "AV3 de thi",
    chapterFallback: "tong-on",
    path: "C:/Users/kienq/Downloads/av3_ đề thi_.docx",
  },
  {
    label: "AV3 review",
    chapterFallback: "tong-on",
    path: "C:/Users/kienq/Downloads/dề thi AV3  REVIEW.docx",
  },
];

function cleanText(value) {
  return String(value || "")
    .replace(/\r/g, "")
    .replace(/[ \t]+\n/g, "\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

function cleanLine(value) {
  return cleanText(value)
    .replace(/\s*\n\s*/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function optionIndexes(block) {
  const labels = [];
  const re = /(?:^|\n|\s)([ABCD])\s*[\.\)]\s*/g;
  let match;
  while ((match = re.exec(block))) {
    labels.push({ key: match[1].toUpperCase(), start: match.index + match[0].length, labelStart: match.index });
  }
  return labels;
}

function detectUnit(text, startIndex, fallback) {
  const windowText = text.slice(Math.max(0, startIndex - 1200), startIndex);
  const matches = [...windowText.matchAll(/Unit\s+(\d{1,2})/gi)];
  if (!matches.length) return fallback;
  return String(matches[matches.length - 1][1]);
}

function normalizeQuestionKey(question) {
  return String(question || "")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[“”‘’'"`]/g, "")
    .replace(/[^a-zA-Z0-9]+/g, " ")
    .trim()
    .toLowerCase();
}

function isSuspiciousQuestion(question) {
  const text = String(question.question || "");
  if (!text || text.length > 260) return true;
  if (/ThS\.|MULTILPLE CHOICE QUESTIONS|READING COMPREHENSION|SENTENCE ARRANGEMENT/i.test(text)) return true;
  if (/\b\d{1,3}\.\s+[A-D]\./.test(text)) return true;
  return Object.values(question.options || {}).some((option) => {
    const value = String(option || "");
    return (
      !value ||
      value.length > 180 ||
      /\b\d{1,3}\.\s+[A-D]\./.test(value) ||
      /II\.|III\.|IV\.|READING COMPREHENSION|SENTENCE ARRANGEMENT/i.test(value)
    );
  });
}

function parseFourChoiceQuestions(rawText, chapterFallback) {
  const text = cleanText(rawText);
  const questionStartRe = /(?:^|\n)\s*(?:Câu\s+)?(\d{1,4})\s*[\.\)]?\s+/gi;
  const starts = [];
  let match;

  while ((match = questionStartRe.exec(text))) {
    const before = text.slice(Math.max(0, match.index - 20), match.index);
    if (/Unit|Page|ThS|English|MULTI|READING|FILL/i.test(before)) continue;
    starts.push({
      number: Number(match[1]),
      start: match.index,
      bodyStart: questionStartRe.lastIndex,
      chapter: detectUnit(text, match.index, chapterFallback),
    });
  }

  const questions = [];
  for (let i = 0; i < starts.length; i += 1) {
    const current = starts[i];
    const nextStart = starts[i + 1]?.start ?? text.length;
    const block = text.slice(current.bodyStart, nextStart);

    const idxs = optionIndexes(block);
    const firstA = idxs.findIndex((item) => item.key === "A");
    if (firstA < 0) continue;

    const usable = idxs.slice(firstA);
    const hasABCD = ["A", "B", "C", "D"].every((key) => usable.some((item) => item.key === key));
    if (!hasABCD) continue;

    const firstOption = usable[0];
    const questionText = cleanLine(block.slice(0, firstOption.labelStart));
    const options = {};

    for (let j = 0; j < usable.length; j += 1) {
      const item = usable[j];
      if (!["A", "B", "C", "D"].includes(item.key) || options[item.key]) continue;
      const next = usable.slice(j + 1).find((candidate) => ["A", "B", "C", "D"].includes(candidate.key) && !options[candidate.key]);
      const end = next ? next.labelStart : block.length;
      options[item.key] = cleanLine(block.slice(item.start, end)).replace(/\s+\d+\s*$/, "").trim();
    }

    if (!questionText || !options.A || !options.B || !options.C || !options.D) continue;

    questions.push({
      source: path.basename(chapterFallback),
      chapter: current.chapter || chapterFallback,
      question: questionText,
      options,
      answer: "",
      confidence: 0,
      answerSource: "missing",
      explanation: "",
    });
  }

  return questions;
}

async function extractDocxText(filePath) {
  const result = await mammoth.extractRawText({ path: filePath });
  return String(result.value || "");
}

async function resolveAnswers(questions) {
  const unresolved = questions
    .map((question, index) => ({ index, question }))
    .filter((item) => !item.question.answer);

  const batchSize = 10;
  for (let offset = 0; offset < unresolved.length; offset += batchSize) {
    const batch = unresolved.slice(offset, offset + batchSize).map((item) => ({
      index: item.index,
      question: item.question.question,
      options: item.question.options,
    }));

    const response = await fetch(`${HELPER_URL}/api/ai/resolve-answers`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ model: MODEL, questions: batch }),
    });

    if (!response.ok) {
      const responseText = await response.text();
      throw new Error(`Resolve answers failed: ${response.status} ${responseText.slice(0, 200)}`);
    }

    const payload = await response.json();
    for (const result of payload.results || []) {
      const target = questions[result.index];
      if (!target) continue;
      if (result.answer) {
        target.answer = String(result.answer).toUpperCase();
        target.confidence = Number(result.confidence || 0);
        target.answerSource = "ollama";
        target.explanation = String(result.explanation || "");
      }
    }

    console.log(`Resolved ${Math.min(offset + batch.length, unresolved.length)}/${unresolved.length}`);
  }
}

async function build() {
  const collected = [];

  for (const source of SOURCES) {
    const rawText = await extractDocxText(source.path);
    const parsed = parseFourChoiceQuestions(rawText, source.chapterFallback)
      .map((question) => ({ ...question, source: source.label }));
    console.log(`${source.label}: ${parsed.length} questions`);
    collected.push(...parsed);
  }

  const seen = new Set();
  const uniqueQuestions = collected.filter((question) => {
    const key = normalizeQuestionKey(question.question);
    if (!key || seen.has(key) || isSuspiciousQuestion(question)) return false;
    seen.add(key);
    return true;
  });

  console.log(`Unique questions: ${uniqueQuestions.length}`);
  await resolveAnswers(uniqueQuestions);

  const readyQuestions = uniqueQuestions.filter((question) => question.answer);
  console.log(`Ready questions: ${readyQuestions.length}`);

  const payload = {
    title: "Ngân hàng trắc nghiệm Anh văn 3 tổng hợp",
    count: readyQuestions.length,
    sourceCounts: {
      imported: readyQuestions.length,
    },
    questions: readyQuestions,
  };

  await fs.mkdir(OUTPUT_DIR, { recursive: true });
  await fs.writeFile(OUTPUT_FILE, `window.__QUIZ_DATA__ = ${JSON.stringify(payload)};\n`, "utf8");
}

build().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
