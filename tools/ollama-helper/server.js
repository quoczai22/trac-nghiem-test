// Local Ollama helper cho admin/import-export.html
// Chạy local, không deploy lên GitHub Pages.
// Nhiệm vụ: nhận danh sách câu hỏi thiếu đáp án, gọi Ollama, trả về JSON gợi ý.

const http = require("http");
const mammoth = require("mammoth");

const PORT = Number(process.env.PORT || 3100);
const OLLAMA_URL = process.env.OLLAMA_URL || "http://localhost:11434";
const DEFAULT_MODEL = process.env.OLLAMA_MODEL || "qwen2.5:7b";

function sendJson(res, status, payload) {
  res.writeHead(status, {
    "Content-Type": "application/json; charset=utf-8",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization",
  });
  res.end(JSON.stringify(payload));
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    let body = "";
    req.on("data", (chunk) => {
      body += chunk;
      if (body.length > 5 * 1024 * 1024) {
        reject(new Error("Payload quá lớn."));
        req.destroy();
      }
    });
    req.on("end", () => resolve(body ? JSON.parse(body) : {}));
    req.on("error", reject);
  });
}

function strictJsonFromText(text) {
  const normalized = String(text || "")
    .trim()
    .replace(/^```(?:json)?\s*/i, "")
    .replace(/\s*```$/, "");

  try {
    const parsed = JSON.parse(normalized);
    return typeof parsed === "string" ? JSON.parse(parsed) : parsed;
  } catch {}

  for (let start = 0; start < normalized.length; start += 1) {
    if (normalized[start] !== "{" && normalized[start] !== "[") continue;

    const stack = [];
    let inString = false;
    let escaped = false;
    for (let end = start; end < normalized.length; end += 1) {
      const char = normalized[end];
      if (inString) {
        if (escaped) escaped = false;
        else if (char === "\\") escaped = true;
        else if (char === '"') inString = false;
        continue;
      }
      if (char === '"') inString = true;
      else if (char === "{" || char === "[") stack.push(char);
      else if (char === "}" || char === "]") {
        const open = stack.pop();
        if (!open || (open === "{" && char !== "}") || (open === "[" && char !== "]")) break;
        if (!stack.length) {
          try {
            return JSON.parse(normalized.slice(start, end + 1));
          } catch {
            break;
          }
        }
      }
    }
  }

  const preview = normalized.replace(/\s+/g, " ").slice(0, 160);
  throw new Error(`Model không trả JSON${preview ? `: ${preview}` : "."}`);
}

async function requestJsonFromOllama(model, messages) {
  async function send(requestMessages) {
    const response = await fetch(`${OLLAMA_URL}/api/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        model,
        stream: false,
        format: "json",
        messages: requestMessages,
        options: { temperature: 0.1, top_p: 0.2 },
      }),
    });

    if (!response.ok) {
      const responseText = await response.text();
      throw new Error(`Ollama lỗi ${response.status}: ${responseText.slice(0, 200)}`);
    }
    const payload = await response.json();
    return strictJsonFromText(payload.message?.content || "");
  }

  try {
    return await send(messages);
  } catch (firstError) {
    try {
      return await send([
        ...messages,
        { role: "user", content: "Your previous response was invalid. Return only one valid JSON value matching the requested schema. No prose." },
      ]);
    } catch (retryError) {
      throw new Error(`Model không trả JSON hợp lệ sau 2 lần thử: ${retryError.message || firstError.message}`);
    }
  }
}

function cleanInlineText(value) {
  return String(value || "")
    .replace(/\r/g, "")
    .replace(/\s*\n\s*/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

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
    .replace(/\*\*/g, "")
    .trim();
}

function parseAnswers(text) {
  const answers = {};
  const re = /\b(\d{1,4})\s*[\.\-:]\s*([ABCD])\b/gi;
  let match;
  while ((match = re.exec(text))) {
    answers[Number(match[1])] = match[2].toUpperCase();
  }
  return answers;
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

function findInlineAnswer(block) {
  const match = block.match(/(?:Answer)\s*[:\-]\s*([ABCD])/i);
  return match ? match[1].toUpperCase() : "";
}

function parseQuestionsFromRawText(rawText) {
  const text = cleanText(rawText);
  const answers = parseAnswers(text);
  const questionStartRe = /(?:^|\n)\s*(?:Câu\s+)?(\d{1,4})\s*[\.\)]?\s+/gi;
  const starts = [];
  let match;

  while ((match = questionStartRe.exec(text))) {
    const before = text.slice(Math.max(0, match.index - 20), match.index);
    if (/Unit|Page|ThS|English|MULTI|READING|FILL/i.test(before)) continue;
    starts.push({ number: Number(match[1]), start: match.index, bodyStart: questionStartRe.lastIndex });
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
      options[item.key] = cleanLine(block.slice(item.start, end));
    }

    const answer = answers[current.number] || findInlineAnswer(block);
    if (!questionText || !options.A || !options.B || !options.C || !options.D) continue;

    questions.push({
      question: questionText,
      options,
      answer,
      confidence: answer ? 1 : 0,
      explanation: "",
    });
  }

  return questions;
}

async function extractDocxRawTextFromBase64(fileBase64) {
  const buffer = Buffer.from(String(fileBase64 || ""), "base64");
  if (!buffer.length) throw new Error("DOCX rỗng hoặc không hợp lệ.");
  const result = await mammoth.extractRawText({ buffer });
  return String(result.value || "");
}

function parseOptionsFromTextBlock(value) {
  const text = String(value || "").replace(/\r/g, "\n");
  const normalized = text
    .replace(/\b([ABCD])\s*[:.)-]\s*/gi, "\n$1. ")
    .replace(/\n{2,}/g, "\n")
    .trim();

  const matches = [...normalized.matchAll(/(?:^|\n)([ABCD])\.\s*([\s\S]*?)(?=(?:\n[ABCD]\.\s)|$)/g)];
  if (matches.length < 4) return null;

  const options = {};
  for (const match of matches) {
    const key = String(match[1] || "").toUpperCase();
    if (!["A", "B", "C", "D"].includes(key) || options[key]) continue;
    options[key] = cleanInlineText(match[2]);
  }

  return options.A && options.B && options.C && options.D ? options : null;
}

function extractQuestionAndOptions(item) {
  const baseQuestion = cleanInlineText(
    item?.question || item?.content || item?.title || item?.prompt || item?.text || ""
  );

  const optionSources = [
    item?.options,
    item?.choices,
    item?.answers,
    item?.selections,
    item?.optionList,
  ];

  for (const source of optionSources) {
    if (Array.isArray(source) && source.length >= 4) {
      const values = source.slice(0, 4).map((entry) => {
        if (typeof entry === "string") return cleanInlineText(entry.replace(/^[ABCD]\s*[:.)-]\s*/i, ""));
        if (entry && typeof entry === "object") return cleanInlineText(entry.text || entry.content || entry.value || entry.label || "");
        return "";
      });

      if (values[0] && values[1] && values[2] && values[3]) {
        return {
          question: baseQuestion,
          options: { A: values[0], B: values[1], C: values[2], D: values[3] },
        };
      }
    }

    if (source && typeof source === "object" && !Array.isArray(source)) {
      const objectOptions = {
        A: cleanInlineText(source.A ?? source.a ?? ""),
        B: cleanInlineText(source.B ?? source.b ?? ""),
        C: cleanInlineText(source.C ?? source.c ?? ""),
        D: cleanInlineText(source.D ?? source.d ?? ""),
      };
      if (objectOptions.A && objectOptions.B && objectOptions.C && objectOptions.D) {
        return { question: baseQuestion, options: objectOptions };
      }
    }

    if (typeof source === "string") {
      const parsed = parseOptionsFromTextBlock(source);
      if (parsed) return { question: baseQuestion, options: parsed };
    }
  }

  const combinedText = [baseQuestion, item?.rawText, item?.sourceText, item?.body]
    .filter(Boolean)
    .join("\n");
  const parsedFromCombined = parseOptionsFromTextBlock(combinedText);
  if (!parsedFromCombined) return { question: baseQuestion, options: null };

  const questionOnly = cleanInlineText(combinedText.replace(/\bA\s*[:.)-]\s*[\s\S]*$/i, ""));
  return {
    question: questionOnly || baseQuestion,
    options: parsedFromCombined,
  };
}

function normalizeParsedQuestions(payload) {
  const rawQuestions = Array.isArray(payload) ? payload : payload?.questions;
  if (!Array.isArray(rawQuestions)) return [];

  return rawQuestions.map((item) => {
    const extracted = extractQuestionAndOptions(item);
    const answer = String(item?.answer || "").toUpperCase();
    return {
      question: extracted.question,
      options: extracted.options || {
        A: cleanInlineText(item?.options?.A || item?.A || ""),
        B: cleanInlineText(item?.options?.B || item?.B || ""),
        C: cleanInlineText(item?.options?.C || item?.C || ""),
        D: cleanInlineText(item?.options?.D || item?.D || ""),
      },
      answer: ["A", "B", "C", "D"].includes(answer) ? answer : "",
      confidence: Number(item?.confidence || 0),
      explanation: String(item?.explanation || ""),
    };
  }).filter((item) => (
    item.question && item.options.A && item.options.B && item.options.C && item.options.D
  ));
}

async function askOllama(question, model) {
  const prompt = `You are solving a multiple-choice English/course question for import into a quiz bank.
Return ONLY valid JSON. No markdown.
Schema:
{"answer":"A|B|C|D|null","confidence":0.0-1.0,"explanation":"short Vietnamese explanation"}

Question:
${question.question}
A. ${question.options?.A || ""}
B. ${question.options?.B || ""}
C. ${question.options?.C || ""}
D. ${question.options?.D || ""}

Rules:
- Choose the best answer.
- If the question is ambiguous or requires a passage not provided, return answer null and confidence <= 0.5.
- For grammar/vocabulary, solve directly.
- Keep explanation under 25 Vietnamese words.`;

  const parsed = await requestJsonFromOllama(model, [
    { role: "system", content: "You are a strict JSON API for multiple-choice answer extraction." },
    { role: "user", content: prompt },
  ]);
  const answer = String(parsed.answer || "").toUpperCase();

  return {
    index: question.index,
    answer: ["A", "B", "C", "D"].includes(answer) ? answer : null,
    confidence: Number(parsed.confidence || 0),
    explanation: String(parsed.explanation || ""),
  };
}

async function parseQuestionsWithOllama({ text, subject, chapter }, model) {
  const prompt = `You extract multiple-choice questions from a raw document for a quiz bank.
Return ONLY valid JSON. No markdown.
Schema:
{"questions":[{"question":"...","options":{"A":"...","B":"...","C":"...","D":"..."},"answer":"A|B|C|D|null","confidence":0.0,"explanation":"short Vietnamese explanation"}]}

Subject: ${subject || "Không xác định"}
Chapter: ${chapter || "Tổng ôn"}

Rules:
- Detect questions even when numbering, line breaks, or Word formatting is irregular.
- Only include a question when all four options A/B/C/D are present in the source text.
- Copy the question text and options as close to the source text as possible.
- If needed, you may put the full raw block into question/body/rawText, but options must still end up separable as A/B/C/D.
- Choose the best answer when possible. If not certain, answer must be null and confidence <= 0.5.
- Do not invent questions or options that are not in the document.
- Keep each explanation under 25 Vietnamese words.

Raw document text:
${text}`;

  const parsed = await requestJsonFromOllama(model, [
    { role: "system", content: "You are a strict JSON API for quiz question extraction." },
    { role: "user", content: prompt },
  ]);
  return normalizeParsedQuestions(parsed);
}

const server = http.createServer(async (req, res) => {
  if (req.method === "OPTIONS") return sendJson(res, 200, { ok: true });

  if (req.method === "GET" && req.url === "/") {
    return sendJson(res, 200, {
      ok: true,
      message: "Ollama helper is running.",
      ollamaUrl: OLLAMA_URL,
      defaultModel: DEFAULT_MODEL,
      features: ["resolve-answers", "parse-questions-v2"],
    });
  }

  if (req.method === "POST" && req.url === "/api/ai/resolve-answers") {
    try {
      const body = await readBody(req);
      const model = body.model || DEFAULT_MODEL;
      const questions = Array.isArray(body.questions) ? body.questions : [];
      if (!questions.length) return sendJson(res, 400, { message: "Thiếu questions." });

      const results = [];
      for (const question of questions) {
        try {
          results.push(await askOllama(question, model));
        } catch (error) {
          results.push({ index: question.index, answer: null, confidence: 0, explanation: error.message });
        }
      }

      return sendJson(res, 200, { results });
    } catch (error) {
      return sendJson(res, 500, { message: error.message });
    }
  }

  if (req.method === "POST" && req.url === "/api/ai/parse-questions") {
    try {
      const body = await readBody(req);
      const text = String(body.text || "").trim();
      if (!text) return sendJson(res, 400, { message: "Thiếu text của tài liệu." });

      const questions = await parseQuestionsWithOllama({
        text,
        subject: body.subject,
        chapter: body.chapter,
      }, body.model || DEFAULT_MODEL);

      return sendJson(res, 200, { questions });
    } catch (error) {
      return sendJson(res, 500, { message: error.message });
    }
  }

  if (req.method === "POST" && req.url === "/api/ai/parse-docx") {
    try {
      const body = await readBody(req);
      if (!body.fileBase64) return sendJson(res, 400, { message: "Thiếu fileBase64 của DOCX." });

      const text = await extractDocxRawTextFromBase64(body.fileBase64);
      let questions = parseQuestionsFromRawText(text);

      if (!questions.length) {
        questions = await parseQuestionsWithOllama({
          text,
          subject: body.subject,
          chapter: body.chapter,
        }, body.model || DEFAULT_MODEL);
      }

      return sendJson(res, 200, { questions, rawTextLength: text.length });
    } catch (error) {
      return sendJson(res, 500, { message: error.message });
    }
  }

  sendJson(res, 404, { message: "Not found" });
});

server.listen(PORT, () => {
  console.log(`Ollama helper running: http://localhost:${PORT}`);
  console.log(`Ollama API: ${OLLAMA_URL}`);
  console.log(`Default model: ${DEFAULT_MODEL}`);
});
