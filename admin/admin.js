// Admin Import / Export local cho GitHub Pages.
// Ghi chú quan trọng:
// - Không có backend nên không thể bảo mật tuyệt đối ở frontend.
// - Import hiện tại chỉ lưu vào localStorage của máy đang dùng.
// - Không cho "replace toàn bộ" trong UI để tránh người dùng import nhầm làm mất bộ đề.
// - Sau này khi có Node.js + database, phần này có thể chuyển sang API thật.

const SUBJECTS = {
  "he-dieu-hanh": {
    title: "Ngân hàng trắc nghiệm Hệ điều hành",
    localKey: "quiz_subject_he-dieu-hanh_data",
    batchesKey: "quiz_subject_he-dieu-hanh_import_batches",
    defaultData: () => window.__SUBJECT_DEFAULT_DATA__["he-dieu-hanh"],
    outputBase: "questions_he_dieu_hanh",
  },
  "co-so-du-lieu-demo": {
    title: "Ngân hàng trắc nghiệm Cơ sở dữ liệu - Demo",
    localKey: "quiz_subject_co-so-du-lieu-demo_data",
    batchesKey: "quiz_subject_co-so-du-lieu-demo_import_batches",
    defaultData: () => window.__SUBJECT_DEFAULT_DATA__["co-so-du-lieu-demo"],
    outputBase: "questions_co_so_du_lieu_demo",
  },
};

const els = {
  fileInput: document.getElementById("fileInput"),
  dropzone: document.getElementById("dropzone"),
  importSubject: document.getElementById("importSubject"),
  importChapter: document.getElementById("importChapter"),
  importMode: document.getElementById("importMode"),
  parseBtn: document.getElementById("parseBtn"),
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
};

let importedData = null;
let importedBatch = null;

function normalizeChapterValue(value) {
  const raw = String(value ?? "").trim();
  if (!raw || raw === "tong-on" || raw.toLowerCase() === "all") return "tong-on";
  const number = Number(raw);
  return Number.isFinite(number) && number >= 1 && number <= 8 ? number : "tong-on";
}

function formatChapterLabel(value) {
  return normalizeChapterValue(value) === "tong-on" ? "Tổng ôn" : `Chương ${value}`;
}

function cleanText(value) {
  return String(value || "")
    .replace(/\r/g, "")
    .replace(/[ \t]+\n/g, "\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

function cleanLine(value) {
  return cleanText(value).replace(/\s*\n\s*/g, " ").replace(/\s+/g, " ").trim();
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
  const re = /(?:^|\n)\s*([ABCD])\s*[\.\)]\s*/g;
  let match;
  while ((match = re.exec(block))) {
    labels.push({ key: match[1].toUpperCase(), start: match.index + match[0].length, labelStart: match.index });
  }
  return labels;
}

function findInlineAnswer(block) {
  const match = block.match(/(?:Đáp\s*án|Answer)\s*[:\-]\s*([ABCD])/i);
  return match ? match[1].toUpperCase() : "";
}

function parseQuestionsFromText(rawText, chapter) {
  const text = cleanText(rawText);
  const answers = parseAnswers(text);
  const questionStartRe = /(?:^|\n)\s*Câu\s+(\d{1,4})\s*\n?/gi;
  const starts = [];
  let match;

  while ((match = questionStartRe.exec(text))) {
    starts.push({ number: Number(match[1]), start: match.index, bodyStart: questionStartRe.lastIndex });
  }

  const questions = [];
  for (let i = 0; i < starts.length; i += 1) {
    const current = starts[i];
    const nextStart = starts[i + 1]?.start ?? text.length;
    let block = text.slice(current.bodyStart, nextStart);

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

    for (let j = 0; j < usable.length; j += 1) {
      const item = usable[j];
      if (!["A", "B", "C", "D"].includes(item.key) || options[item.key]) continue;
      const next = usable.slice(j + 1).find((candidate) => ["A", "B", "C", "D"].includes(candidate.key) && !options[candidate.key]);
      const end = next ? next.labelStart : block.length;
      let value = cleanLine(block.slice(item.start, end));
      value = value.replace(/(?:THAM KHẢO|BẢNG ĐÁP ÁN|ĐÁP ÁN).*$/i, "").trim();
      options[item.key] = value;
    }

    const answer = answers[current.number] || findInlineAnswer(block);
    if (!questionText || !options.A || !options.B || !options.C || !options.D || !answer) continue;

    questions.push({
      chapter: normalizeChapterValue(chapter),
      question: questionText,
      options,
      answer,
    });
  }

  return questions;
}

function parseJsData(text) {
  const match = text.match(/window\.__QUIZ_DATA__\s*=\s*([\s\S]*?);?\s*$/);
  if (!match) throw new Error("File JS không đúng dạng window.__QUIZ_DATA__ = {...}");
  return JSON.parse(match[1]);
}

function normalizeData(data, subject, chapter) {
  const subjectInfo = SUBJECTS[subject];
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
  })).filter((q) => q.question && q.options.A && q.options.B && q.options.C && q.options.D && q.answer);

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

async function extractDocxText(file) {
  if (!window.mammoth) throw new Error("Không tải được Mammoth.js. Hãy mở bằng internet hoặc dùng TXT/JSON.");
  const buffer = await file.arrayBuffer();
  const result = await mammoth.extractRawText({ arrayBuffer: buffer });
  return result.value;
}

async function readFileToData(file, subject, chapter) {
  const name = file.name.toLowerCase();
  if (name.endsWith(".json")) {
    return normalizeData(JSON.parse(await file.text()), subject, chapter);
  }
  if (name.endsWith(".js")) {
    return normalizeData(parseJsData(await file.text()), subject, chapter);
  }

  let text = "";
  if (name.endsWith(".pdf")) text = await extractPdfText(file);
  else if (name.endsWith(".docx")) text = await extractDocxText(file);
  else text = await file.text();

  const questions = parseQuestionsFromText(text, chapter);
  return normalizeData({ title: SUBJECTS[subject].title, questions }, subject, chapter);
}

function structuredCloneSafe(value) {
  return JSON.parse(JSON.stringify(value));
}

function getDefaultData(subject) {
  const data = SUBJECTS[subject].defaultData();
  if (!data) throw new Error("Không tìm thấy bộ đề mặc định.");
  return structuredCloneSafe(data);
}

function getBatches(subject) {
  const raw = localStorage.getItem(SUBJECTS[subject].batchesKey);
  return raw ? JSON.parse(raw) : [];
}

function saveBatches(subject, batches) {
  localStorage.setItem(SUBJECTS[subject].batchesKey, JSON.stringify(batches));
}

function getImportedOnlyData(subject) {
  const batches = getBatches(subject);
  const questions = batches.flatMap((batch) => batch.questions || []);
  return {
    title: `${SUBJECTS[subject].title} - Bộ đã import`,
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

function getLocalData(subject) {
  const raw = localStorage.getItem(SUBJECTS[subject].localKey);
  return raw ? JSON.parse(raw) : null;
}

function saveMergedForQuiz(subject) {
  const data = getMergedData(subject);
  localStorage.setItem(SUBJECTS[subject].localKey, toQuestionsJson(data));
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
      <p><strong>Đáp án:</strong> ${escapeHtml(q.answer)}</p>
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
  const html = toDocumentHtml(data);
  downloadText(filename, html, "application/msword");
}

function printPdf(data) {
  const html = toDocumentHtml(data);
  const win = window.open("", "_blank");
  if (!win) {
    els.exportStatus.textContent = "Trình duyệt đang chặn popup. Hãy cho phép popup để xuất PDF.";
    return;
  }
  win.document.open();
  win.document.write(html);
  win.document.close();
  win.focus();
  setTimeout(() => win.print(), 300);
}

function setImportStatus(message) {
  els.importStatus.textContent = message;
}

function showPreview(data, batch) {
  const sample = data.questions.slice(0, 3);
  els.previewBox.classList.remove("hidden");
  els.previewBox.textContent = JSON.stringify({
    batch: batch ? { fileName: batch.fileName, count: batch.questions.length } : null,
    count: data.questions.length,
    sourceCounts: data.sourceCounts,
    sample,
  }, null, 2);
}

async function handleParse() {
  const files = Array.from(els.fileInput.files || []);
  if (!files.length) {
    setImportStatus("Bạn chưa chọn file.");
    return;
  }

  const subject = els.importSubject.value;
  const chapter = els.importChapter.value;
  const batches = getBatches(subject);
  const parsedQuestions = [];

  try {
    setImportStatus(`Đang đọc ${files.length} file...`);
    for (const file of files) {
      const parsed = await readFileToData(file, subject, chapter);
      if (!parsed.questions.length) {
        throw new Error(`Không tách được câu hỏi từ file ${file.name}.`);
      }

      const batch = {
        id: Date.now() + Math.random(),
        fileName: file.name,
        importedAt: new Date().toISOString(),
        chapter: normalizeChapterValue(chapter),
        questions: parsed.questions,
      };
      batches.push(batch);
      parsedQuestions.push(...parsed.questions);
      importedBatch = batch;
    }

    saveBatches(subject, batches);
    importedData = normalizeData({
      title: `${SUBJECTS[subject].title} - Batch import mới`,
      questions: parsedQuestions,
    }, subject, chapter);

    const merged = getMergedData(subject);
    showPreview(merged, importedBatch);

    els.saveLocalBtn.disabled = false;
    els.downloadJsBtn.disabled = false;
    els.downloadJsonBtn.disabled = false;

    setImportStatus(
      `Đã import thêm ${parsedQuestions.length} câu từ ${files.length} file (${formatChapterLabel(chapter)}). ` +
      `Tổng import tạm: ${getImportedOnlyData(subject).questions.length} câu. ` +
      `Bản gộp hiện có: ${merged.questions.length} câu.`
    );
  } catch (error) {
    importedData = null;
    importedBatch = null;
    els.saveLocalBtn.disabled = true;
    els.downloadJsBtn.disabled = true;
    els.downloadJsonBtn.disabled = true;
    setImportStatus(`Lỗi: ${error.message}`);
  }
}

function saveImportedLocal() {
  const subject = els.importSubject.value;
  const data = saveMergedForQuiz(subject);
  setImportStatus(`Đã lưu tạm bản gộp ${data.questions.length} câu vào trình duyệt. Vào môn Hệ điều hành để test ngay.`);
}

function getExportData() {
  const subject = els.exportSubject.value;
  const source = els.exportSource.value;

  let data;
  if (source === "default") data = getDefaultData(subject);
  else if (source === "imported") data = getImportedOnlyData(subject);
  else data = getMergedData(subject);

  if (!data || !data.questions.length) {
    throw new Error("Không có dữ liệu để xuất.");
  }

  return { subject, data: normalizeData(data, subject, 1) };
}

els.parseBtn.addEventListener("click", handleParse);
els.saveLocalBtn.addEventListener("click", saveImportedLocal);

els.downloadJsBtn.addEventListener("click", () => {
  if (!importedData) return;
  downloadText("questions_imported_latest.js", toQuestionsJs(importedData), "text/javascript");
});

els.downloadJsonBtn.addEventListener("click", () => {
  if (!importedData) return;
  downloadText("questions_imported_latest.json", toQuestionsJson(importedData), "application/json");
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
  localStorage.removeItem(SUBJECTS[subject].batchesKey);
  localStorage.removeItem(SUBJECTS[subject].localKey);
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
