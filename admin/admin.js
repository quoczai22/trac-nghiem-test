// Admin Import / Export local cho GitHub Pages.
// Phase hiện tại: web tĩnh, không backend, không database.
// Workflow an toàn:
// 1) Phân tích file -> tạo draft
// 2) Nếu thiếu đáp án -> tùy chọn gọi Ollama local để gợi ý
// 3) Preview/deduplicate -> người dùng bấm Merge
// 4) Merge chỉ append vào localStorage, không replace questions.js gốc

function getSubjectInfo(subjectId) {
  const subject = window.QuizSubjects.get(subjectId);
  if (!subject) throw new Error("Không tìm thấy môn học.");

  return {
    ...subject,
    title: `Ngân hàng trắc nghiệm ${subject.title}`,
    localKey: `quiz_subject_${subject.id}_data`,
    batchesKey: `quiz_subject_${subject.id}_import_batches`,
    outputBase: `questions_${subject.id.replace(/-/g, "_")}`,
    defaultData: () => {
      const defaultData = window.__SUBJECT_DEFAULT_DATA__?.[subject.id];
      return defaultData || {
        title: `Ngân hàng trắc nghiệm ${subject.title}`,
        count: 0,
        sourceCounts: { default: 0 },
        questions: [],
      };
    },
  };
}

const els = {
  fileInput: document.getElementById("fileInput"),
  dropzone: document.getElementById("dropzone"),
  importSubject: document.getElementById("importSubject"),
  importChapter: document.getElementById("importChapter"),
  importMode: document.getElementById("importMode"),
  parseBtn: document.getElementById("parseBtn"),
  aiSuggestBtn: document.getElementById("aiSuggestBtn"),
  mergeDraftBtn: document.getElementById("mergeDraftBtn"),
  saveLocalBtn: document.getElementById("saveLocalBtn"),
  downloadJsBtn: document.getElementById("downloadJsBtn"),
  downloadJsonBtn: document.getElementById("downloadJsonBtn"),
  importStatus: document.getElementById("importStatus"),
  previewBox: document.getElementById("previewBox"),
  exportSubject: document.getElementById("exportSubject"),
  exportSource: document.getElementById("exportSource"),
  exportJsBtn: document.getElementById("exportJsBtn"),
  exportJsonBtn: document.getElementById("exportJsonBtn"),
  exportDocBtn: document.getElementById("exportDocBtn"),
  exportPdfBtn: document.getElementById("exportPdfBtn"),
  clearLocalBtn: document.getElementById("clearLocalBtn"),
  exportStatus: document.getElementById("exportStatus"),
  ollamaHelperUrl: document.getElementById("ollamaHelperUrl"),
  ollamaModel: document.getElementById("ollamaModel"),
  newSubjectTitle: document.getElementById("newSubjectTitle"),
  newSubjectIcon: document.getElementById("newSubjectIcon"),
  newSubjectUnitType: document.getElementById("newSubjectUnitType"),
  newSubjectUnitCount: document.getElementById("newSubjectUnitCount"),
  newSubjectDescription: document.getElementById("newSubjectDescription"),
  createSubjectBtn: document.getElementById("createSubjectBtn"),
  createSubjectStatus: document.getElementById("createSubjectStatus"),
};

let draftData = null;
let draftBatchMeta = null;
let importedData = null;
let importedBatch = null;

function populateSubjectSelect(select, selectedId) {
  const subjects = window.QuizSubjects.list();
  select.innerHTML = "";
  subjects.forEach((subject) => {
    const option = document.createElement("option");
    option.value = subject.id;
    option.textContent = `${subject.icon} ${subject.title}`;
    option.selected = subject.id === selectedId;
    select.appendChild(option);
  });
}

function renderChapterOptions(subjectId, selectedValue = "tong-on") {
  const subject = getSubjectInfo(subjectId);
  els.importChapter.innerHTML = "";

  const all = document.createElement("option");
  all.value = "tong-on";
  all.textContent = "Tất cả / Tổng ôn / Không chọn chương-bài";
  els.importChapter.appendChild(all);

  subject.units.forEach((unit) => {
    const option = document.createElement("option");
    option.value = unit.id;
    option.textContent = unit.label;
    els.importChapter.appendChild(option);
  });

  els.importChapter.value = Array.from(els.importChapter.options).some((option) => option.value === String(selectedValue))
    ? String(selectedValue)
    : "tong-on";
}

function refreshSubjectControls(preferredSubjectId) {
  const currentImport = preferredSubjectId || els.importSubject.value || "he-dieu-hanh";
  const currentExport = preferredSubjectId || els.exportSubject.value || currentImport;
  const importChapter = els.importChapter.value || "tong-on";

  populateSubjectSelect(els.importSubject, currentImport);
  populateSubjectSelect(els.exportSubject, currentExport);
  renderChapterOptions(els.importSubject.value, importChapter);
}

function createSubject() {
  try {
    const subject = window.QuizSubjects.create({
      title: els.newSubjectTitle.value,
      icon: els.newSubjectIcon.value,
      description: els.newSubjectDescription.value,
      unitType: els.newSubjectUnitType.value,
      unitCount: els.newSubjectUnitCount.value,
    });

    refreshSubjectControls(subject.id);
    els.newSubjectTitle.value = "";
    els.newSubjectIcon.value = "📚";
    els.newSubjectDescription.value = "";
    els.newSubjectUnitCount.value = "8";
    els.createSubjectStatus.textContent = `Đã tạo ${subject.icon} ${subject.title}. Bây giờ chọn file và Import thêm câu hỏi.`;
  } catch (error) {
    els.createSubjectStatus.textContent = `Lỗi: ${error.message}`;
  }
}

function normalizeChapterValue(value) {
  const raw = String(value ?? "").trim();
  if (!raw || raw === "tong-on" || raw.toLowerCase() === "all") return "tong-on";
  const number = Number(raw);
  return Number.isFinite(number) && number >= 1 ? number : "tong-on";
}

function formatChapterLabel(value, subjectId) {
  const normalized = normalizeChapterValue(value);
  if (normalized === "tong-on") return "Tổng ôn";
  const unit = subjectId ? getSubjectInfo(subjectId).units.find((item) => item.id === String(normalized)) : null;
  return unit?.label || `Chương ${normalized}`;
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
    // Tránh bắt nhầm A/B/C/D nằm trong chữ thường bằng cách ưu tiên vị trí đầu dòng hoặc sau khoảng trắng rõ ràng.
    labels.push({ key: match[1].toUpperCase(), start: match.index + match[0].length, labelStart: match.index });
  }
  return labels;
}

function findInlineAnswer(block) {
  const match = block.match(/(?:Đáp\s*án|Answer)\s*[:\-]\s*([ABCD])/i);
  return match ? match[1].toUpperCase() : "";
}

function findBoldAnswerFromOptions(optionsWithMarkup) {
  for (const [key, value] of Object.entries(optionsWithMarkup)) {
    if (/\*\*[^*]+\*\*/.test(value)) return key;
  }
  return "";
}

function parseQuestionsFromText(rawText, chapter, { allowMissingAnswer = true } = {}) {
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

    if (/THAM KHẢO|BẢNG ĐÁP ÁN|ĐÁP ÁN/i.test(block) && !/\bA\s*[\.\)]/i.test(block)) continue;

    const idxs = optionIndexes(block);
    const firstA = idxs.findIndex((item) => item.key === "A");
    if (firstA < 0) continue;

    const usable = idxs.slice(firstA);
    const hasABCD = ["A", "B", "C", "D"].every((key) => usable.some((item) => item.key === key));
    if (!hasABCD) continue;

    const firstOption = usable[0];
    const questionText = cleanLine(block.slice(0, firstOption.labelStart));
    const options = {};
    const optionsWithMarkup = {};

    for (let j = 0; j < usable.length; j += 1) {
      const item = usable[j];
      if (!["A", "B", "C", "D"].includes(item.key) || options[item.key]) continue;
      const next = usable.slice(j + 1).find((candidate) => ["A", "B", "C", "D"].includes(candidate.key) && !options[candidate.key]);
      const end = next ? next.labelStart : block.length;
      let rawValue = cleanText(block.slice(item.start, end)).replace(/(?:THAM KHẢO|BẢNG ĐÁP ÁN|ĐÁP ÁN).*$/i, "").trim();
      optionsWithMarkup[item.key] = rawValue;
      options[item.key] = cleanLine(rawValue);
    }

    const answer = answers[current.number] || findInlineAnswer(block) || findBoldAnswerFromOptions(optionsWithMarkup);
    if (!questionText || !options.A || !options.B || !options.C || !options.D) continue;
    if (!answer && !allowMissingAnswer) continue;

    questions.push({
      chapter: normalizeChapterValue(chapter),
      question: questionText,
      options,
      answer,
      confidence: answer ? 1 : 0,
      answerSource: answer ? (answers[current.number] ? "answer-table" : findBoldAnswerFromOptions(optionsWithMarkup) ? "bold-docx" : "inline") : "missing",
    });
  }

  return questions;
}

function parseJsData(text) {
  const match = text.match(/window\.__QUIZ_DATA__\s*=\s*([\s\S]*?);?\s*$/);
  if (!match) throw new Error("File JS không đúng dạng window.__QUIZ_DATA__ = {...}");
  return JSON.parse(match[1]);
}

function normalizeData(data, subject, chapter, { allowMissingAnswer = true } = {}) {
  const subjectInfo = getSubjectInfo(subject);
  const questions = (data.questions || data || []).map((q) => ({
    chapter: normalizeChapterValue(q.chapter || chapter),
    question: String(q.question || "").trim(),
    options: {
      A: String(q.options?.A || q.A || "").trim(),
      B: String(q.options?.B || q.B || "").trim(),
      C: String(q.options?.C || q.C || "").trim(),
      D: String(q.options?.D || q.D || "").trim(),
    },
    answer: String(q.answer || "").trim().toUpperCase(),
    confidence: Number(q.confidence ?? (q.answer ? 1 : 0)),
    answerSource: q.answerSource || (q.answer ? "provided" : "missing"),
    explanation: q.explanation || "",
  })).filter((q) => q.question && q.options.A && q.options.B && q.options.C && q.options.D && (allowMissingAnswer || q.answer));

  return {
    title: data.title || subjectInfo.title,
    count: questions.length,
    sourceCounts: { imported: questions.length },
    questions,
  };
}

async function extractPdfText(file) {
  if (!window.pdfjsLib) throw new Error("Không tải được PDF.js. Hãy mở bằng internet hoặc dùng TXT/JSON.");
  pdfjsLib.GlobalWorkerOptions.workerSrc = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js";
  const buffer = await file.arrayBuffer();
  const pdf = await pdfjsLib.getDocument({ data: buffer }).promise;
  let text = "";
  for (let pageNo = 1; pageNo <= pdf.numPages; pageNo += 1) {
    const page = await pdf.getPage(pageNo);
    const content = await page.getTextContent();
    text += content.items.map((item) => item.str).join("\n") + "\n";
  }
  return text;
}

function getXmlText(node) {
  return Array.from(node.getElementsByTagName("w:t")).map((item) => item.textContent || "").join("");
}

async function extractDocxTextWithBold(file) {
  // DOCX là file zip. Hàm này đọc word/document.xml để giữ dấu **bold** quanh run in đậm.
  // Nhờ vậy đề Anh văn 3 có đáp án in đậm có thể nhận diện bằng rule mà không cần AI.
  if (!window.JSZip) {
    if (!window.mammoth) throw new Error("Không tải được JSZip/Mammoth.js. Hãy mở bằng internet hoặc dùng TXT/JSON.");
    const buffer = await file.arrayBuffer();
    const result = await mammoth.extractRawText({ arrayBuffer: buffer });
    return result.value;
  }

  const zip = await JSZip.loadAsync(await file.arrayBuffer());
  const documentXml = await zip.file("word/document.xml")?.async("text");
  if (!documentXml) throw new Error("DOCX không có word/document.xml.");

  const xml = new DOMParser().parseFromString(documentXml, "application/xml");
  const paragraphs = Array.from(xml.getElementsByTagName("w:p"));

  return paragraphs.map((p) => {
    return Array.from(p.getElementsByTagName("w:r")).map((run) => {
      const text = getXmlText(run);
      if (!text) return "";
      const isBold = run.getElementsByTagName("w:b").length > 0;
      return isBold ? `**${text}**` : text;
    }).join("");
  }).join("\n");
}

async function extractDocxText(file) {
  return extractDocxTextWithBold(file);
}

function arrayBufferToBase64(buffer) {
  const bytes = new Uint8Array(buffer);
  const chunkSize = 0x8000;
  let binary = "";
  for (let i = 0; i < bytes.length; i += chunkSize) {
    const chunk = bytes.subarray(i, i + chunkSize);
    binary += String.fromCharCode(...chunk);
  }
  return btoa(binary);
}

async function parseRawTextWithOllama(text, subject, chapter, fileName) {
  const baseUrl = String(els.ollamaHelperUrl.value || "http://localhost:3100").replace(/\/$/, "");
  const model = String(els.ollamaModel.value || "qwen2.5:7b").trim();
  const subjectInfo = getSubjectInfo(subject);

  setImportStatus(`Parser chưa nhận ra câu hỏi trong ${fileName}. Đang nhờ Qwen/Ollama tách từ nội dung thô...`);
  const response = await fetch(`${baseUrl}/api/ai/parse-questions`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      model,
      text,
      subject: subjectInfo.title,
      chapter: formatChapterLabel(chapter, subject),
    }),
  });

  const payload = await response.json();
  if (!response.ok) throw new Error(payload.message || "Ollama helper lỗi.");

  const questions = (payload.questions || []).map((question) => ({
    ...question,
    chapter: question.chapter || chapter,
    answerSource: "ollama-parser",
  }));
  return normalizeData({ title: subjectInfo.title, questions }, subject, chapter, { allowMissingAnswer: true });
}

async function parseDocxWithHelper(file, subject, chapter) {
  const baseUrl = String(els.ollamaHelperUrl.value || "http://localhost:3100").replace(/\/$/, "");
  const model = String(els.ollamaModel.value || "qwen2.5:7b").trim();
  const subjectInfo = getSubjectInfo(subject);

  setImportStatus(`Parser trong trình duyệt chưa nhận ra ${file.name}. Đang nhờ helper local đọc DOCX trực tiếp...`);
  const response = await fetch(`${baseUrl}/api/ai/parse-docx`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      model,
      fileName: file.name,
      fileBase64: arrayBufferToBase64(await file.arrayBuffer()),
      subject: subjectInfo.title,
      chapter: formatChapterLabel(chapter, subject),
    }),
  });

  const payload = await response.json();
  if (!response.ok) throw new Error(payload.message || "DOCX helper lỗi.");

  const questions = (payload.questions || []).map((question) => ({
    ...question,
    chapter: question.chapter || chapter,
    answerSource: question.answerSource || (question.answer ? "docx-helper" : "missing"),
  }));

  return normalizeData({ title: subjectInfo.title, questions }, subject, chapter, { allowMissingAnswer: true });
}

async function readFileToData(file, subject, chapter) {
  const name = file.name.toLowerCase();
  if (name.endsWith(".json")) {
    return normalizeData(JSON.parse(await file.text()), subject, chapter, { allowMissingAnswer: true });
  }
  if (name.endsWith(".js")) {
    return normalizeData(parseJsData(await file.text()), subject, chapter, { allowMissingAnswer: true });
  }

  let text = "";
  if (name.endsWith(".pdf")) text = await extractPdfText(file);
  else if (name.endsWith(".docx")) text = await extractDocxText(file);
  else text = await file.text();

  const questions = parseQuestionsFromText(text, chapter, { allowMissingAnswer: true });
  const parsed = normalizeData({ title: getSubjectInfo(subject).title, questions }, subject, chapter, { allowMissingAnswer: true });
  if (parsed.questions.length) return parsed;

  if (name.endsWith(".docx")) {
    try {
      const docxFallback = await parseDocxWithHelper(file, subject, chapter);
      if (docxFallback.questions.length) return docxFallback;
    } catch (error) {
      throw new Error(`Không tách được câu hỏi từ file ${file.name}. Parser thường và helper DOCX đều thất bại: ${error.message}`);
    }
  }

  try {
    const fallback = await parseRawTextWithOllama(text, subject, chapter, file.name);
    if (fallback.questions.length) return fallback;
  } catch (error) {
    throw new Error(`Không tách được câu hỏi từ file ${file.name}. Parser thường và Qwen/Ollama fallback đều thất bại: ${error.message}`);
  }

  throw new Error(`Không tách được câu hỏi từ file ${file.name}. Parser thường và Qwen/Ollama fallback không tạo được câu hỏi hợp lệ.`);
}

function structuredCloneSafe(value) {
  return JSON.parse(JSON.stringify(value));
}

function getDefaultData(subject) {
  const data = getSubjectInfo(subject).defaultData();
  if (!data) throw new Error("Không tìm thấy bộ đề mặc định.");
  return structuredCloneSafe(data);
}

function getBatches(subject) {
  const raw = localStorage.getItem(getSubjectInfo(subject).batchesKey);
  return raw ? JSON.parse(raw) : [];
}

function saveBatches(subject, batches) {
  localStorage.setItem(getSubjectInfo(subject).batchesKey, JSON.stringify(batches));
}

function getImportedOnlyData(subject) {
  const batches = getBatches(subject);
  const questions = batches.flatMap((batch) => batch.questions || []);
  return {
    title: `${getSubjectInfo(subject).title} - Bộ đã import`,
    count: questions.length,
    sourceCounts: { imported: questions.length },
    questions,
  };
}

function dedupeQuestions(questions) {
  const seen = new Set();
  const output = [];
  for (const q of questions) {
    const key = `${q.chapter}|${q.question}`.toLowerCase().replace(/\s+/g, " ").trim();
    if (seen.has(key)) continue;
    seen.add(key);
    output.push(q);
  }
  return output;
}

function getMergedData(subject) {
  const base = getDefaultData(subject);
  const imported = getImportedOnlyData(subject);
  const questions = dedupeQuestions([...base.questions, ...imported.questions]);
  return {
    ...base,
    title: `${base.title} - Bản gộp`,
    count: questions.length,
    sourceCounts: {
      default: base.questions.length,
      imported: imported.questions.length,
      merged: questions.length,
    },
    questions,
  };
}

function saveMergedForQuiz(subject) {
  const data = getMergedData(subject);
  localStorage.setItem(getSubjectInfo(subject).localKey, toQuestionsJson(data));
  return data;
}

function toQuestionsJs(data) {
  const normalized = { ...data, count: data.questions.length };
  return `window.__QUIZ_DATA__ = ${JSON.stringify(normalized, null, 2)};\n`;
}

function toQuestionsJson(data) {
  return JSON.stringify({ ...data, count: data.questions.length }, null, 2);
}

function escapeHtml(value) {
  return String(value || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function toDocumentHtml(data) {
  const rows = data.questions.map((q, index) => `
    <div class="question">
      <h3>Câu ${index + 1} - ${formatChapterLabel(q.chapter)}</h3>
      <p><strong>${escapeHtml(q.question)}</strong></p>
      <ol type="A">
        <li>${escapeHtml(q.options.A)}</li>
        <li>${escapeHtml(q.options.B)}</li>
        <li>${escapeHtml(q.options.C)}</li>
        <li>${escapeHtml(q.options.D)}</li>
      </ol>
      <p><strong>Đáp án:</strong> ${escapeHtml(q.answer || "Chưa xác định")}</p>
      ${q.explanation ? `<p><em>${escapeHtml(q.explanation)}</em></p>` : ""}
    </div>
  `).join("\n");

  return `<!doctype html>
<html lang="vi">
<head>
  <meta charset="utf-8">
  <title>${escapeHtml(data.title)}</title>
  <style>
    body { font-family: Arial, sans-serif; line-height: 1.45; padding: 28px; }
    h1 { text-align: center; }
    .meta { text-align: center; color: #555; margin-bottom: 24px; }
    .question { page-break-inside: avoid; border-bottom: 1px solid #ddd; padding: 12px 0; }
    h3 { margin-bottom: 6px; }
  </style>
</head>
<body>
  <h1>${escapeHtml(data.title)}</h1>
  <p class="meta">Tổng số câu: ${data.questions.length}</p>
  ${rows}
</body>
</html>`;
}

function downloadText(filename, content, type = "text/plain") {
  const blob = new Blob([content], { type });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(url);
}

function downloadDoc(filename, data) {
  downloadText(filename, toDocumentHtml(data), "application/msword");
}

function printPdf(data) {
  const win = window.open("", "_blank");
  if (!win) {
    els.exportStatus.textContent = "Trình duyệt đang chặn popup. Hãy cho phép popup để xuất PDF.";
    return;
  }
  win.document.open();
  win.document.write(toDocumentHtml(data));
  win.document.close();
  win.focus();
  setTimeout(() => win.print(), 300);
}

function setImportStatus(message) {
  els.importStatus.textContent = message;
}

function getDraftStats(data = draftData) {
  const questions = data?.questions || [];
  const resolved = questions.filter((q) => q.answer).length;
  const missing = questions.length - resolved;
  const ai = questions.filter((q) => String(q.answerSource || "").startsWith("ollama")).length;
  return { total: questions.length, resolved, missing, ai };
}

function renderDraftPreview(data = draftData) {
  if (!data) {
    els.previewBox.classList.add("hidden");
    return;
  }

  const stats = getDraftStats(data);
  const sample = data.questions.slice(0, 12).map((q, index) => ({
    stt: index + 1,
    chapter: q.chapter,
    question: q.question,
    answer: q.answer || null,
    confidence: q.confidence || 0,
    answerSource: q.answerSource,
    options: q.options,
    explanation: q.explanation || "",
  }));

  els.previewBox.classList.remove("hidden");
  els.previewBox.textContent = JSON.stringify({ stats, sample }, null, 2);

  els.aiSuggestBtn.disabled = stats.missing === 0;
  els.mergeDraftBtn.disabled = stats.total === 0;
  els.downloadJsBtn.disabled = stats.total === 0;
  els.downloadJsonBtn.disabled = stats.total === 0;
}

async function handleParse() {
  const files = Array.from(els.fileInput.files || []);
  if (!files.length) {
    setImportStatus("Bạn chưa chọn file.");
    return;
  }

  const subject = els.importSubject.value;
  const chapter = els.importChapter.value;
  const parsedQuestions = [];

  try {
    setImportStatus(`Đang phân tích ${files.length} file...`);
    for (const file of files) {
      const parsed = await readFileToData(file, subject, chapter);
      if (!parsed.questions.length) {
        throw new Error(`Không tách được câu hỏi từ file ${file.name}.`);
      }
      parsed.questions.forEach((q) => {
        q.sourceFile = file.name;
        parsedQuestions.push(q);
      });
    }

    draftData = normalizeData({
      title: `${getSubjectInfo(subject).title} - Draft import`,
      questions: parsedQuestions,
    }, subject, chapter, { allowMissingAnswer: true });

    draftBatchMeta = {
      id: Date.now() + Math.random(),
      fileName: files.map((f) => f.name).join(", "),
      importedAt: new Date().toISOString(),
      chapter: normalizeChapterValue(chapter),
    };

    importedData = draftData;
    importedBatch = draftBatchMeta;
    renderDraftPreview();

    const stats = getDraftStats();
    setImportStatus(
      `Đã tạo draft ${stats.total} câu từ ${files.length} file (${formatChapterLabel(chapter, subject)}). ` +
      `Nhận diện được ${stats.resolved} đáp án, còn thiếu ${stats.missing}. ` +
      `Kiểm tra preview trước khi Merge.`
    );
  } catch (error) {
    draftData = null;
    draftBatchMeta = null;
    importedData = null;
    importedBatch = null;
    els.aiSuggestBtn.disabled = true;
    els.mergeDraftBtn.disabled = true;
    els.saveLocalBtn.disabled = true;
    els.downloadJsBtn.disabled = true;
    els.downloadJsonBtn.disabled = true;
    setImportStatus(`Lỗi: ${error.message}`);
  }
}

async function suggestMissingAnswersWithOllama() {
  if (!draftData) return;
  const missing = draftData.questions
    .map((question, index) => ({ ...question, index }))
    .filter((q) => !q.answer);

  if (!missing.length) {
    setImportStatus("Draft không còn câu thiếu đáp án.");
    return;
  }

  const baseUrl = String(els.ollamaHelperUrl.value || "http://localhost:3100").replace(/\/$/, "");
  const model = String(els.ollamaModel.value || "qwen2.5:7b").trim();

  try {
    setImportStatus(`Đang gọi Ollama cho ${missing.length} câu thiếu đáp án...`);
    const response = await fetch(`${baseUrl}/api/ai/resolve-answers`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ model, questions: missing }),
    });

    const payload = await response.json();
    if (!response.ok) throw new Error(payload.message || "Ollama helper lỗi.");

    (payload.results || []).forEach((result) => {
      const target = draftData.questions[result.index];
      if (!target) return;
      const answer = String(result.answer || "").toUpperCase();
      if (!["A", "B", "C", "D"].includes(answer)) return;
      target.answer = answer;
      target.confidence = Number(result.confidence || 0.75);
      target.answerSource = "ollama";
      target.explanation = result.explanation || "AI/Ollama gợi ý. Cần người dùng kiểm tra trước khi dùng chính thức.";
    });

    importedData = draftData;
    renderDraftPreview();
    const stats = getDraftStats();
    setImportStatus(`Ollama đã gợi ý xong. Nhận diện ${stats.resolved}/${stats.total} câu, còn thiếu ${stats.missing}.`);
  } catch (error) {
    setImportStatus(`Không gọi được Ollama: ${error.message}. Hãy chạy tools/ollama-helper hoặc tự bổ sung đáp án.`);
  }
}

function mergeDraft() {
  if (!draftData || !draftData.questions.length) return;
  const subject = els.importSubject.value;
  const stats = getDraftStats();

  if (stats.missing > 0) {
    const ok = confirm(`Draft còn ${stats.missing} câu chưa có đáp án. Merge các câu đã có đáp án và bỏ câu thiếu?`);
    if (!ok) return;
  }

  const readyQuestions = draftData.questions.filter((q) => q.answer);
  if (!readyQuestions.length) {
    setImportStatus("Không có câu nào đủ đáp án để merge.");
    return;
  }

  const batches = getBatches(subject);
  const batch = {
    ...draftBatchMeta,
    id: draftBatchMeta?.id || Date.now() + Math.random(),
    fileName: draftBatchMeta?.fileName || "draft-import",
    importedAt: draftBatchMeta?.importedAt || new Date().toISOString(),
    chapter: normalizeChapterValue(els.importChapter.value),
    questions: readyQuestions,
  };

  batches.push(batch);
  saveBatches(subject, batches);

  importedBatch = batch;
  importedData = normalizeData({
    title: `${getSubjectInfo(subject).title} - Batch import mới`,
    questions: readyQuestions,
  }, subject, els.importChapter.value, { allowMissingAnswer: false });

  const merged = getMergedData(subject);
  els.saveLocalBtn.disabled = false;
  renderDraftPreview(importedData);
  setImportStatus(
    `Đã merge ${readyQuestions.length} câu vào bộ import. ` +
    `Tổng import tạm: ${getImportedOnlyData(subject).questions.length} câu. ` +
    `Bản gộp hiện có: ${merged.questions.length} câu.`
  );
}

function saveImportedLocal() {
  const subject = els.importSubject.value;
  const data = saveMergedForQuiz(subject);
  const subjectInfo = getSubjectInfo(subject);
  setImportStatus(`Đã lưu tạm bản gộp ${data.questions.length} câu vào trình duyệt. Vào môn ${subjectInfo.title.replace("Ngân hàng trắc nghiệm ", "")} để test ngay.`);
}

function getExportData() {
  const subject = els.exportSubject.value;
  const source = els.exportSource.value;

  let data;
  if (source === "default") data = getDefaultData(subject);
  else if (source === "imported") data = getImportedOnlyData(subject);
  else data = getMergedData(subject);

  if (!data || !data.questions.length) throw new Error("Không có dữ liệu để xuất.");
  return { subject, data: normalizeData(data, subject, 1, { allowMissingAnswer: false }) };
}

els.parseBtn.addEventListener("click", handleParse);
els.aiSuggestBtn.addEventListener("click", suggestMissingAnswersWithOllama);
els.mergeDraftBtn.addEventListener("click", mergeDraft);
els.saveLocalBtn.addEventListener("click", saveImportedLocal);
els.createSubjectBtn.addEventListener("click", createSubject);
els.importSubject.addEventListener("change", () => renderChapterOptions(els.importSubject.value));

els.downloadJsBtn.addEventListener("click", () => {
  if (!draftData) return;
  downloadText("questions_draft.js", toQuestionsJs(draftData), "text/javascript");
});

els.downloadJsonBtn.addEventListener("click", () => {
  if (!draftData) return;
  downloadText("questions_draft.json", toQuestionsJson(draftData), "application/json");
});

els.exportJsBtn.addEventListener("click", () => {
  try {
    const { data } = getExportData();
    downloadText("questions.js", toQuestionsJs(data), "text/javascript");
    els.exportStatus.textContent = `Đã xuất JS ${data.questions.length} câu.`;
  } catch (error) {
    els.exportStatus.textContent = `Lỗi: ${error.message}`;
  }
});

els.exportJsonBtn.addEventListener("click", () => {
  try {
    const { data } = getExportData();
    downloadText("questions.json", toQuestionsJson(data), "application/json");
    els.exportStatus.textContent = `Đã xuất JSON ${data.questions.length} câu.`;
  } catch (error) {
    els.exportStatus.textContent = `Lỗi: ${error.message}`;
  }
});

els.exportDocBtn.addEventListener("click", () => {
  try {
    const { data } = getExportData();
    downloadDoc("questions.doc", data);
    els.exportStatus.textContent = `Đã xuất Word .doc ${data.questions.length} câu.`;
  } catch (error) {
    els.exportStatus.textContent = `Lỗi: ${error.message}`;
  }
});

els.exportPdfBtn.addEventListener("click", () => {
  try {
    const { data } = getExportData();
    printPdf(data);
    els.exportStatus.textContent = `Đã mở cửa sổ in. Chọn Save as PDF để lưu ${data.questions.length} câu.`;
  } catch (error) {
    els.exportStatus.textContent = `Lỗi: ${error.message}`;
  }
});

els.clearLocalBtn.addEventListener("click", () => {
  const subject = els.exportSubject.value;
  if (!confirm("Xóa tất cả batch import tạm trong trình duyệt? Bộ đề mặc định không bị ảnh hưởng.")) return;
  localStorage.removeItem(getSubjectInfo(subject).batchesKey);
  localStorage.removeItem(getSubjectInfo(subject).localKey);
  els.exportStatus.textContent = "Đã xóa tất cả import tạm trong trình duyệt.";
});

["dragenter", "dragover"].forEach((eventName) => {
  els.dropzone.addEventListener(eventName, (event) => {
    event.preventDefault();
    els.dropzone.classList.add("dragover");
  });
});

["dragleave", "drop"].forEach((eventName) => {
  els.dropzone.addEventListener(eventName, (event) => {
    event.preventDefault();
    els.dropzone.classList.remove("dragover");
  });
});

els.dropzone.addEventListener("drop", (event) => {
  const files = Array.from(event.dataTransfer.files || []);
  if (!files.length) return;
  const dataTransfer = new DataTransfer();
  files.forEach((file) => dataTransfer.items.add(file));
  els.fileInput.files = dataTransfer.files;
  setImportStatus(`Đã chọn ${files.length} file: ${files.map((f) => f.name).join(", ")}`);
});

els.fileInput.addEventListener("change", () => {
  const files = Array.from(els.fileInput.files || []);
  setImportStatus(files.length ? `Đã chọn ${files.length} file: ${files.map((f) => f.name).join(", ")}` : "Chưa có file.");
});

const requestedSubject = new URLSearchParams(window.location.search).get("subject");
refreshSubjectControls(window.QuizSubjects.get(requestedSubject) ? requestedSubject : "he-dieu-hanh");
