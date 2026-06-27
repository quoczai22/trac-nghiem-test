const subjectId = new URLSearchParams(window.location.search).get("subject");
const subject = window.QuizSubjects?.get(subjectId);

if (!subject || subject.kind !== "local") {
  throw new Error("Không tìm thấy môn local cần làm bài.");
}

const SUBJECT_KEY = subject.id;
const IMPORTED_DATA_KEY = `quiz_subject_${SUBJECT_KEY}_data`;
const QUIZ_STORAGE_PREFIX = `quiz_subject_${SUBJECT_KEY}_random`;

function storageKey(suffix) {
  return `${QUIZ_STORAGE_PREFIX}_${suffix}`;
}

function getDataSignature(data) {
  const questions = Array.isArray(data?.questions) ? data.questions : [];
  return `${data?.title || "quiz"}__${questions.length}__${questions[0]?.question || ""}__${questions[questions.length - 1]?.question || ""}`;
}

function getQuizDataSource() {
  const imported = localStorage.getItem(IMPORTED_DATA_KEY);
  if (imported) {
    try {
      const parsed = JSON.parse(imported);
      if (parsed && Array.isArray(parsed.questions)) {
        parsed.count = parsed.questions.length;
        return parsed;
      }
    } catch (error) {
      console.warn("Không đọc được bộ đề import:", error);
    }
  }
  if (subject.id === "anh-van-3") {
    if (window.__QUIZ_DATA__ && Array.isArray(window.__QUIZ_DATA__.questions) && window.__QUIZ_DATA__.questions.length) {
      window.__QUIZ_DATA__.count = window.__QUIZ_DATA__.questions.length;
      return window.__QUIZ_DATA__;
    }
    const fallback = window.__QUIZ_EXAM_50__ || window.__QUIZ_EXAM_40__;
    if (fallback && Array.isArray(fallback.questions)) {
      fallback.count = fallback.questions.length;
      return fallback;
    }
  }
  return {
    title: `Ngân hàng trắc nghiệm ${subject.title}`,
    count: 0,
    sourceCounts: { imported: 0 },
    questions: [],
  };
}

const state = {
  bank: [],
  questions: [],
  answers: JSON.parse(localStorage.getItem(storageKey("answers")) || "{}"),
  history: JSON.parse(localStorage.getItem(storageKey("history")) || "[]"),
  filter: "all",
  submitted: JSON.parse(localStorage.getItem(storageKey("submitted")) || "false"),
  autoSubmitted: JSON.parse(localStorage.getItem(storageKey("auto_submitted")) || "false"),
  attemptRecorded: JSON.parse(localStorage.getItem(storageKey("attempt_recorded")) || "false"),
  currentIndex: Number(localStorage.getItem(storageKey("current")) || 0),
  deadline: Number(localStorage.getItem(storageKey("deadline")) || 0),
  timerId: null,
};

const TIME_LIMIT_MS = 60 * 60 * 1000;
const MAX_HISTORY_ITEMS = 50;
const AV3_CORE_CHAPTERS = ["7", "8", "9", "10", "11", "12"];

const PHRASE_REPLACEMENTS = [
  ["He dieu hanh", "Hệ điều hành"],
  ["he dieu hanh", "hệ điều hành"],
  ["Bo nho chinh", "Bộ nhớ chính"],
  ["bo nho chinh", "bộ nhớ chính"],
  ["Bo nho", "Bộ nhớ"],
  ["bo nho", "bộ nhớ"],
  ["thanh ghi", "thanh ghi"],
  ["va thanh ghi", "và thanh ghi"],
  ["quan trong", "quan trọng"],
  ["truc tiep", "trực tiếp"],
  ["nguoi dung", "người dùng"],
  ["chuong trinh", "chương trình"],
  ["phan cung", "phần cứng"],
  ["thuan tien", "thuận tiện"],
  ["tai nguyen", "tài nguyên"],
  ["hieu qua", "hiệu quả"],
  ["Vai tro", "Vai trò"],
  ["cap phat", "cấp phát"],
  ["dieu phoi", "điều phối"],
  ["Kernel la", "Kernel là"],
  ["nhan", "nhân"],
  ["thuong tru", "thường trú"],
  ["firmware", "firmware"],
  ["khoi dong", "khởi động"],
  ["Interrupt", "Interrupt"],
  ["tam dung", "tạm dừng"],
  ["xu ly", "xử lý"],
  ["su kien", "sự kiện"],
  ["chua", "chứa"],
  ["dia chi", "địa chỉ"],
  ["routine phuc vu ngat", "routine phục vụ ngắt"],
  ["loi hoac", "lỗi hoặc"],
  ["Dual mode", "Dual mode"],
  ["dac quyen", "đặc quyền"],
  ["User mode", "User mode"],
  ["Kernel mode", "Kernel mode"],
  ["Bo trung gian giua", "Bộ trung gian giữa"],
  ["nhap xuat", "nhập xuất"],
  ["Bo bien dich ngon ngu", "Bộ biên dịch ngôn ngữ"],
  ["Tang kich thuoc man hinh", "Tăng kích thước màn hình"],
  ["Loai bo hoan toan loi lap trinh", "Loại bỏ hoàn toàn lỗi lập trình"],
  ["Microkernel", "Microkernel"],
  ["de dang mo rong", "dễ dàng mở rộng"],
  ["an toan hon", "an toàn hơn"],
  ["Process scheduler", "Process scheduler"],
  ["chon process", "chọn process"],
  ["hang doi", "hàng đợi"],
  ["Ready queue", "Ready queue"],
  ["Device queue", "Device queue"],
  ["Job queue duy nhat", "Job queue duy nhất"],
  ["Cac thread", "Các thread"],
  ["cung mot process", "cùng một process"],
  ["thuong chia se", "thường chia sẻ"],
  ["Code, data va cac file mo", "Code, data và các file mở"],
  ["Tat ca stack rieng", "Tất cả stack riêng"],
  ["Tat ca register rieng cua nhau", "Tất cả register riêng của nhau"],
  ["PID rieng cua tung process khac", "PID riêng của từng process khác"],
  ["Mot cau hay bay", "Một câu hay bẫy"],
  ["KHONG phai", "KHÔNG phải"],
  ["Don vi thuc thi nhe hon process", "Đơn vị thực thi nhẹ hơn process"],
  ["Mot process con doc lap voi khong gian dia chi rieng", "Một process con độc lập với không gian địa chỉ riêng"],
  ["Thanh phan co", "Thành phần có"],
  ["rieng", "riêng"],
  ["du lieu chia se", "dữ liệu chia sẻ"],
  ["thong bao cho CPU", "thông báo cho CPU"],
  ["I/O hoan tat", "I/O hoàn tất"],
  ["Semaphore", "Semaphore"],
  ["fork()", "fork()"],
  ["exec()", "exec()"],
  ["cau truc", "cấu trúc"],
  ["Single-thread", "Single-thread"],
  ["FIFO", "FIFO"],
  ["dang cho", "đang chờ"],
  ["TLC", "TLB"],
  ["tiểu trình", "tiểu trình"],
  ["Tien trinh", "Tiến trình"],
  ["tien trinh", "tiến trình"],
  ["Tieu trinh", "Tiểu trình"],
  ["tieu trinh", "tiểu trình"],
  ["dong bo", "đồng bộ"],
  ["khong", "không"],
  ["mot", "một"],
  ["cua", "của"],
  ["thuong", "thường"],
  ["dung", "đúng"],
  ["sai", "sai"],
  ["truoc", "trước"],
  ["sau", "sau"],
];

function prettifyText(text) {
  return String(text);
}

function formatChapterBadge(chapter) {
  const value = String(chapter ?? "").trim();
  if (value === "tong-on" || value === "all" || value === "0" || !value) return "Tổng ôn";
  return subject.units.find((unit) => unit.id === value)?.label || `Chương ${chapter}`;
}

function inferClo(question) {
  if (question?.clo) return question.clo;
  if (subject.id !== "anh-van-3") return "";

  const text = String(question?.question || "");
  if (text.startsWith("[Vocab")) return "CLO1.2";
  if (text.startsWith("[Grammar")) return "CLO1.1";
  if (text.startsWith("[Reading")) return "CLO2.3";
  if (text.startsWith("[Cloze")) return "CLO2.4";
  return "";
}

function shuffleArray(items) {
  const pool = [...items];
  for (let i = pool.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [pool[i], pool[j]] = [pool[j], pool[i]];
  }
  return pool;
}

function buildQuestionGroupKey(question, index) {
  if (subject.id !== "anh-van-3") return `single:${index}`;

  const text = String(question?.question || "").trim();
  const source = String(question?.source || "unknown");

  const clozeMatch = text.match(/^\[Cloze\]\s*(Passage\s+\d+)/i);
  if (clozeMatch) return `${source}|cloze|${clozeMatch[1].toLowerCase()}`;

  const blankMatch = text.match(/fill in the blank\s*\((\d+)\)/i);
  if (blankMatch) {
    const stem = text.replace(/\(\d+\)\s*$/i, "").trim().toLowerCase();
    return `${source}|blank|${stem}`;
  }

  const readingMatch = text.match(/^\[(Reading[^\]]*)\]\s*(.+?)\n/i);
  if (readingMatch) return `${source}|reading|${readingMatch[1].toLowerCase()}|${readingMatch[2].toLowerCase()}`;

  return `single:${index}`;
}

function isBlankSeriesQuestion(question) {
  return /fill in the blank\s*\(\d+\)/i.test(String(question?.question || ""));
}

function buildRandomUnits() {
  const orderedItems = state.bank.map((question, index) => ({
    question,
    index,
    key: buildQuestionGroupKey(question, index),
  }));
  const units = [];

  for (const item of orderedItems) {
    const currentSource = String(item.question?.source || "unknown");
    const lastUnit = units[units.length - 1];
    const lastItem = lastUnit?.[lastUnit.length - 1];
    const lastSource = String(lastItem?.question?.source || "unknown");

    const sameNamedGroup = lastItem && item.key === lastItem.key && !item.key.startsWith("single:");
    const sameBlankRun =
      lastItem &&
      isBlankSeriesQuestion(item.question) &&
      isBlankSeriesQuestion(lastItem.question) &&
      currentSource === lastSource;

    if (sameNamedGroup || sameBlankRun) {
      lastUnit.push(item);
    } else {
      units.push([item]);
    }
  }

  return units;
}

function getUnitQuestionCount(unit) {
  return unit.reduce((total, item) => total + 1, 0);
}

function getUnitChapter(unit) {
  return String(unit?.[0]?.question?.chapter ?? "").trim();
}

function isReadingUnit(unit) {
  return unit.some((item) => String(item?.question?.question || "").trim().startsWith("[Reading"));
}

function buildAv3ChapterTargets(units, targetCount) {
  const chapterStats = new Map();

  AV3_CORE_CHAPTERS.forEach((chapter) => {
    const chapterUnits = units.filter((unit) => getUnitChapter(unit) === chapter);
    const available = chapterUnits.reduce((sum, unit) => sum + getUnitQuestionCount(unit), 0);
    chapterStats.set(chapter, { units: chapterUnits, available, target: 0 });
  });

  const activeChapters = AV3_CORE_CHAPTERS.filter((chapter) => (chapterStats.get(chapter)?.available || 0) > 0);
  if (!activeChapters.length) return chapterStats;

  let remaining = Math.min(targetCount, state.bank.length);
  const baseTarget = Math.floor(remaining / activeChapters.length);

  activeChapters.forEach((chapter) => {
    const info = chapterStats.get(chapter);
    info.target = Math.min(info.available, baseTarget);
    remaining -= info.target;
  });

  const expandable = [...activeChapters];
  let guard = 0;
  while (remaining > 0 && expandable.length && guard < 1000) {
    guard += 1;
    let allocatedInRound = false;

    for (const chapter of expandable) {
      if (remaining <= 0) break;
      const info = chapterStats.get(chapter);
      if (info.target < info.available) {
        info.target += 1;
        remaining -= 1;
        allocatedInRound = true;
      }
    }

    if (!allocatedInRound) break;
  }

  return chapterStats;
}

function pickUnitsGreedy(units, targetCount) {
  const selected = [];
  let picked = 0;

  for (const unit of units) {
    const size = getUnitQuestionCount(unit);
    if (picked + size > targetCount) continue;
    selected.push(unit);
    picked += size;
    if (picked === targetCount) break;
  }

  return selected;
}

function pickBalancedAv3Questions(count) {
  const safeCount = Math.min(count, state.bank.length);
  const allUnits = buildRandomUnits();
  const chosenUnits = [];
  const chosenKeys = new Set();

  const readingUnits = allUnits.filter((unit) => isReadingUnit(unit));
  if (readingUnits.length) {
    const pickedReadingUnit = shuffleArray(readingUnits)[0];
    const readingSize = getUnitQuestionCount(pickedReadingUnit);
    if (readingSize <= safeCount) {
      const key = pickedReadingUnit.map((item) => `${item.index}`).join("-");
      chosenKeys.add(key);
      chosenUnits.push(pickedReadingUnit);
    }
  }

  const chapterTargets = buildAv3ChapterTargets(
    allUnits.filter((unit) => {
      const key = unit.map((item) => `${item.index}`).join("-");
      return !chosenKeys.has(key);
    }),
    safeCount - chosenUnits.flat().length
  );

  for (const chapter of AV3_CORE_CHAPTERS) {
    const info = chapterTargets.get(chapter);
    if (!info || !info.units.length || !info.target) continue;

    const shuffled = shuffleArray(info.units);
    const exact = pickUnitsToCount(shuffled, info.target);
    const selected = exact || pickUnitsGreedy(shuffled, info.target);

    selected.forEach((unit) => {
      const key = unit.map((item) => `${item.index}`).join("-");
      if (!chosenKeys.has(key)) {
        chosenKeys.add(key);
        chosenUnits.push(unit);
      }
    });
  }

  let questions = chosenUnits.flat().map((item) => item.question);
  if (questions.length >= safeCount) {
    return questions.slice(0, safeCount);
  }

  const remainingUnits = shuffleArray(allUnits).filter((unit) => {
    const key = unit.map((item) => `${item.index}`).join("-");
    return !chosenKeys.has(key);
  });

  const filler = pickUnitsToCount(remainingUnits, safeCount - questions.length)
    || pickUnitsGreedy(remainingUnits, safeCount - questions.length);

  if (filler?.length) {
    questions = questions.concat(filler.flat().map((item) => item.question));
  }

  if (questions.length < safeCount) {
    const existing = new Set(questions.map((question) => question.question));
    const fallback = shuffleArray(state.bank).filter((question) => !existing.has(question.question));
    questions = questions.concat(fallback.slice(0, safeCount - questions.length));
  }

  return questions.slice(0, safeCount);
}

function pickUnitsToCount(units, targetCount) {
  const memo = new Map();

  function solve(position, remaining) {
    if (remaining === 0) return [];
    if (position >= units.length || remaining < 0) return null;

    const key = `${position}:${remaining}`;
    if (memo.has(key)) return memo.get(key);

    const current = units[position];
    let result = null;

    if (current.length <= remaining) {
      const withCurrent = solve(position + 1, remaining - current.length);
      if (withCurrent) result = [current, ...withCurrent];
      else if (remaining === current.length) result = [current];
    }

    if (!result) result = solve(position + 1, remaining);

    memo.set(key, result);
    return result;
  }

  return solve(0, targetCount);
}

const els = {
  totalCount: document.getElementById("totalCount"),
  answeredCount: document.getElementById("answeredCount"),
  remainingCount: document.getElementById("remainingCount"),
  progressText: document.getElementById("progressText"),
  progressFill: document.getElementById("progressFill"),
  questionHost: document.getElementById("questionHost"),
  questionNavigator: document.getElementById("questionNavigator"),
  template: document.getElementById("questionTemplate"),
  submitBtn: document.getElementById("submitBtn"),
  resetBtn: document.getElementById("resetBtn"),
  resultPanel: document.getElementById("resultPanel"),
  quizTitle: document.getElementById("quizTitle"),
  resultLegend: document.getElementById("resultLegend"),
  prevBtn: document.getElementById("prevBtn"),
  nextBtn: document.getElementById("nextBtn"),
  jumpInput: document.getElementById("jumpInput"),
  jumpBtn: document.getElementById("jumpBtn"),
  randomCount: document.getElementById("randomCount"),
  newRandomBtn: document.getElementById("newRandomBtn"),
  randomCard: document.getElementById("randomCard"),
  timerText: document.getElementById("timerText"),
  historyList: document.getElementById("historyList"),
  clearHistoryBtn: document.getElementById("clearHistoryBtn"),
  filters: document.getElementById("filters"),
  subjectHeading: document.getElementById("subjectHeading"),
  subjectDescription: document.getElementById("subjectDescription"),
  adminLink: document.getElementById("adminLink"),
};

function saveState() {
  localStorage.setItem(storageKey("questions"), JSON.stringify(state.questions));
  localStorage.setItem(storageKey("answers"), JSON.stringify(state.answers));
  localStorage.setItem(storageKey("submitted"), JSON.stringify(state.submitted));
  localStorage.setItem(storageKey("auto_submitted"), JSON.stringify(state.autoSubmitted));
  localStorage.setItem(storageKey("attempt_recorded"), JSON.stringify(state.attemptRecorded));
  localStorage.setItem(storageKey("current"), String(state.currentIndex));
  localStorage.setItem(storageKey("deadline"), String(state.deadline));
}

function saveHistory() {
  localStorage.setItem(storageKey("history"), JSON.stringify(state.history));
}

function formatTime(ms) {
  const totalSeconds = Math.max(0, Math.ceil(ms / 1000));
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = totalSeconds % 60;
  return `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
}

function updateTimer() {
  if (!state.deadline || state.submitted) {
    els.timerText.textContent = state.submitted ? "Đã nộp" : "60:00";
    els.timerText.classList.remove("warning");
    return;
  }

  const remaining = state.deadline - Date.now();
  els.timerText.textContent = formatTime(remaining);
  els.timerText.classList.toggle("warning", remaining <= 5 * 60 * 1000);

  if (remaining <= 0) {
    submitQuiz(true);
  }
}

function startTimer(reset = false) {
  if (state.timerId) clearInterval(state.timerId);
  if (reset || !state.deadline) {
    state.deadline = Date.now() + TIME_LIMIT_MS;
  }
  if (!reset && state.deadline <= Date.now() && !state.submitted) {
    submitQuiz(true);
    return;
  }
  saveState();
  updateTimer();
  state.timerId = setInterval(updateTimer, 1000);
}

function getResultStats() {
  const total = state.questions.length;
  const correct = state.questions.reduce((count, q, idx) => count + (state.answers[idx] === q.answer ? 1 : 0), 0);
  const answered = Object.values(state.answers).filter(Boolean).length;
  const score10 = total ? Number(((correct / total) * 10).toFixed(2)) : 0;
  const usedMs = state.deadline ? Math.min(TIME_LIMIT_MS, Math.max(0, TIME_LIMIT_MS - (state.deadline - Date.now()))) : 0;
  return {
    total,
    correct,
    answered,
    wrong: answered - correct,
    blank: total - answered,
    score10,
    usedMs,
  };
}

function formatDateTime(isoDate) {
  return new Date(isoDate).toLocaleString("vi-VN", {
    day: "2-digit",
    month: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
  });
}

function recordAttempt(auto = false) {
  const stats = getResultStats();
  const attempt = {
    id: Date.now(),
    submittedAt: new Date().toISOString(),
    auto,
    ...stats,
  };
  state.history = [attempt, ...state.history].slice(0, MAX_HISTORY_ITEMS);
  saveHistory();
  renderHistory();
}

function renderHistory() {
  if (!els.historyList) return;
  if (!state.history.length) {
    els.historyList.innerHTML = `<p class="history-empty">Chưa có lần nộp nào.</p>`;
    return;
  }

  els.historyList.innerHTML = state.history
    .slice(0, 10)
    .map((item, index) => {
      const mode = item.auto ? "Tự nộp" : "Nộp tay";
      return `
        <div class="history-item">
          <div class="history-main">
            <span>Lần ${state.history.length - index}</span>
            <span class="history-score">${item.score10.toFixed(2)}</span>
          </div>
          <div class="history-meta">${item.correct}/${item.total} đúng · ${formatTime(item.usedMs)} · ${mode}</div>
          <div class="history-meta">${formatDateTime(item.submittedAt)} · Sai ${item.wrong}, trống ${item.blank}</div>
        </div>
      `;
    })
    .join("");
}

function setFilter(filter) {
  state.filter = filter;
  state.currentIndex = 0;
  saveState();
  renderFilters();
  renderQuestions();
  renderNavigator();
}

function renderFilters() {
  const sourceData = getQuizDataSource();
  const isFixedExam = Boolean(sourceData?.fixedExam);
  const entries = [
    { id: "all", label: isFixedExam ? "Toàn bộ đề" : "Đề hiện tại" },
    ...subject.units.map((unit) => ({ id: unit.id, label: unit.label })),
    { id: "tong-on", label: "Tổng ôn" },
    { id: "unanswered", label: "Chưa làm" },
  ];

  els.filters.innerHTML = "";
  entries.forEach((entry) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "chip";
    button.dataset.filter = entry.id;
    button.textContent = entry.label;
    button.classList.toggle("active", state.filter === entry.id);
    button.addEventListener("click", () => setFilter(entry.id));
    els.filters.appendChild(button);
  });
}

function getVisibleQuestions() {
  if (state.filter === "all") return state.questions;
  if (state.filter === "unanswered") {
    return state.questions.filter((_, idx) => !state.answers[idx]);
  }
  return state.questions.filter((q) => String(q.chapter) === state.filter);
}

function updateStats() {
  const total = state.questions.length;
  const answered = Object.values(state.answers).filter(Boolean).length;
  const remaining = total - answered;
  const percent = total ? Math.round((answered / total) * 100) : 0;

  els.totalCount.textContent = total;
  els.answeredCount.textContent = answered;
  els.remainingCount.textContent = remaining;
  els.progressText.textContent = `${percent}%`;
  els.progressFill.style.width = `${percent}%`;
}

function renderNavigator() {
  els.questionNavigator.innerHTML = "";
  const visibleQuestions = getVisibleQuestions();
  const visibleSet = new Set(visibleQuestions.map((q) => state.questions.indexOf(q)));

  state.questions.forEach((question, idx) => {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "nav-q";
    button.textContent = idx + 1;

    const selected = state.answers[idx];
    if (selected) button.classList.add("answered");
    if (state.submitted) {
      if (selected === question.answer) {
        button.classList.remove("answered");
        button.classList.add("correct");
        button.textContent = `${idx + 1}✓`;
      } else if (selected) {
        button.classList.remove("answered");
        button.classList.add("wrong");
        button.textContent = `${idx + 1}×`;
      }
    }

    if (!visibleSet.has(idx)) {
      button.style.opacity = "0.45";
    }

    const currentVisible = getVisibleQuestions()[state.currentIndex];
    const currentActualIndex = currentVisible ? state.questions.indexOf(currentVisible) : -1;
    if (idx === currentActualIndex) button.classList.add("current");

    button.addEventListener("click", () => {
      const currentFilter = state.filter;
      if (currentFilter === "all") {
        state.currentIndex = idx;
      } else {
        const targetVisibleIndex = getVisibleQuestions().findIndex((q) => state.questions.indexOf(q) === idx);
        if (targetVisibleIndex >= 0) {
          state.currentIndex = targetVisibleIndex;
        } else {
          state.filter = "all";
          renderFilters();
          state.currentIndex = idx;
        }
      }
      saveState();
      renderQuestions();
      renderNavigator();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });

    els.questionNavigator.appendChild(button);
  });
}

function renderResult() {
  if (!state.submitted) {
    els.resultPanel.classList.add("hidden");
    els.resultLegend.classList.add("hidden");
    return;
  }

  const stats = getResultStats();

  els.resultPanel.innerHTML = `
    <div><strong>${stats.correct}/${stats.total}</strong> câu đúng</div>
    <p>Điểm quy đổi: <strong>${stats.score10.toFixed(2)}</strong></p>
    <p>${state.autoSubmitted ? "Đã hết 60 phút nên hệ thống tự nộp bài." : "Làm lại được ngay."} Các câu đúng/sai đã được tô màu để bạn rà cực nhanh.</p>
  `;
  els.resultPanel.classList.remove("hidden");
  els.resultLegend.classList.remove("hidden");
}

function clampCurrentIndex() {
  const visibleQuestions = getVisibleQuestions();
  if (!visibleQuestions.length) {
    state.currentIndex = 0;
    return;
  }
  if (state.currentIndex >= visibleQuestions.length) state.currentIndex = visibleQuestions.length - 1;
  if (state.currentIndex < 0) state.currentIndex = 0;
}

function renderQuestions() {
  const visibleQuestions = getVisibleQuestions();
  clampCurrentIndex();
  els.questionHost.innerHTML = "";

  if (!visibleQuestions.length) {
    const content = state.bank.length
      ? "Không có câu nào trong bộ lọc này."
      : `Môn này chưa có câu hỏi. <a href="../../admin/import-export.html?subject=${encodeURIComponent(SUBJECT_KEY)}">Thêm câu hỏi trong Admin</a> rồi quay lại tạo đề.`;
    els.questionHost.innerHTML = `<div class="question-card"><h3 class="question-text">${content}</h3></div>`;
    return;
  }

  const question = visibleQuestions[state.currentIndex];
  const actualIndex = state.questions.indexOf(question);
  const fragment = els.template.content.cloneNode(true);
  const card = fragment.querySelector(".question-card");
  const chapterBadge = fragment.querySelector(".chapter-badge");
  const questionIndex = fragment.querySelector(".question-index");
  const questionText = fragment.querySelector(".question-text");
  const questionClo = fragment.querySelector(".question-clo");
  const optionsWrap = fragment.querySelector(".options");
  const explain = fragment.querySelector(".explain");

  chapterBadge.textContent = formatChapterBadge(question.chapter);
  questionIndex.textContent = `Câu ${actualIndex + 1} / ${state.questions.length}`;
  questionText.textContent = prettifyText(question.question);
  const clo = inferClo(question);
  if (clo) {
    questionClo.textContent = `Chuẩn đầu ra: ${clo}`;
    questionClo.classList.remove("hidden");
  }

  const selected = state.answers[actualIndex];
  const isCorrect = selected === question.answer;

  if (state.submitted) {
    card.classList.add(isCorrect ? "correct-state" : "wrong-state");
    explain.classList.remove("hidden");
    explain.innerHTML = selected
      ? `Bạn chọn <strong>${selected}</strong>. Đáp án đúng là <strong>${question.answer}</strong>.`
      : `Bạn chưa chọn. Đáp án đúng là <strong>${question.answer}</strong>.`;
  }

  for (const [key, value] of Object.entries(question.options)) {
    const label = document.createElement("label");
    label.className = "option";

    if (selected === key) label.classList.add("selected");
    if (state.submitted && key === question.answer) label.classList.add("correct-answer");
    if (state.submitted && selected === key && key !== question.answer) label.classList.add("wrong-answer");

    label.innerHTML = `
      <input type="radio" name="q_${actualIndex}" value="${key}" ${selected === key ? "checked" : ""} ${state.submitted ? "disabled" : ""}>
      <span><strong>${key}.</strong> ${prettifyText(value)}</span>
    `;

    label.addEventListener("change", () => {
      state.answers[actualIndex] = key;
      saveState();
      updateStats();
      renderQuestions();
    });

    optionsWrap.appendChild(label);
  }

  els.questionHost.appendChild(fragment);
  els.jumpInput.value = actualIndex + 1;
  els.prevBtn.disabled = state.currentIndex === 0;
  els.nextBtn.disabled = state.currentIndex === visibleQuestions.length - 1;
}

function applyPresentationMode(data) {
  const isFixedExam = Boolean(data?.fixedExam);
  document.body.classList.toggle("exam-mode", isFixedExam);

  if (isFixedExam) {
    els.subjectDescription.textContent = "Đề mô phỏng cố định 40 câu, bám Unit 7-12 với vocab, grammar, cloze và reading.";
    document.getElementById("quizSubtitle").textContent = "Mặc định mở đề 40 câu, nhưng bạn vẫn có thể tạo đề khác và hệ thống sẽ tự nộp khi hết 60 phút.";
  } else {
    els.subjectDescription.textContent = subject.description;
    document.getElementById("quizSubtitle").textContent = "Chọn đáp án rồi nộp bài để xem điểm.";
  }
}

async function loadQuiz() {
  const data = getQuizDataSource();
  if (!data) throw new Error("Không tìm thấy dữ liệu câu hỏi.");
  document.title = `${subject.title} - Trắc nghiệm`;
  els.subjectHeading.textContent = `${subject.icon} ${subject.title}`;
  els.adminLink.href = `../../admin/import-export.html?subject=${encodeURIComponent(SUBJECT_KEY)}`;
  applyPresentationMode(data);
  state.bank = data.questions;
  const sourceSignature = getDataSignature(data);
  const oldSignature = localStorage.getItem(storageKey("source_signature"));
  const sourceChanged = oldSignature && oldSignature !== sourceSignature;
  if (sourceChanged) {
    state.answers = {};
    state.submitted = false;
    state.autoSubmitted = false;
    state.attemptRecorded = false;
    state.currentIndex = 0;
    state.deadline = 0;
    localStorage.removeItem(storageKey("questions"));
  }
  localStorage.setItem(storageKey("source_signature"), sourceSignature);
  const savedQuestions = JSON.parse(localStorage.getItem(storageKey("questions")) || "null");
  const initialQuestionSet = data.fixedExam
    ? data.questions
    : pickRandomQuestions(Math.min(subject.id === "anh-van-3" ? 50 : 20, data.count || 20));
  state.questions = Array.isArray(savedQuestions) && savedQuestions.length ? savedQuestions : initialQuestionSet;
  if (subject.id === "anh-van-3" && els.randomCount && !els.randomCount.dataset.av3Ready) {
    els.randomCount.value = "50";
    els.randomCount.dataset.av3Ready = "true";
  }
  saveState();
  els.quizTitle.textContent = data.fixedExam
    ? `${data.title} (${state.questions.length} câu)`
    : `${data.title} (${data.count} câu, đề hiện tại ${state.questions.length} câu)`;
  updateStats();
  if (state.submitted && !state.attemptRecorded) {
    recordAttempt(state.autoSubmitted);
    state.attemptRecorded = true;
    saveState();
  }
  renderFilters();
  renderHistory();
  renderResult();
  renderQuestions();
  renderNavigator();
  if (!state.submitted) startTimer(false);
  else updateTimer();
}

function pickRandomQuestions(count) {
  const safeCount = Math.min(count, state.bank.length);

  if (subject.id !== "anh-van-3") {
    const pool = shuffleArray(state.bank);
    return pool.slice(0, safeCount);
  }
  return pickBalancedAv3Questions(safeCount);
}

function createNewRandomQuiz() {
  const count = Number(els.randomCount.value || 20);
  state.questions = pickRandomQuestions(count);
  state.answers = {};
  state.submitted = false;
  state.autoSubmitted = false;
  state.attemptRecorded = false;
  state.currentIndex = 0;
  state.filter = "all";
  renderFilters();
  const sourceData = getQuizDataSource();
  els.quizTitle.textContent = `${sourceData.title} (${sourceData.questions.length} câu, đề hiện tại ${state.questions.length} câu)`;
  saveState();
  startTimer(true);
  updateStats();
  renderResult();
  renderQuestions();
  renderNavigator();
}

function submitQuiz(auto = false) {
  if (state.submitted) return;
  state.submitted = true;
  state.autoSubmitted = auto;
  state.attemptRecorded = true;
  if (state.timerId) clearInterval(state.timerId);
  recordAttempt(auto);
  saveState();
  updateTimer();
  renderResult();
  renderQuestions();
  renderNavigator();
  window.scrollTo({ top: 0, behavior: "smooth" });
}

els.newRandomBtn.addEventListener("click", createNewRandomQuiz);

els.submitBtn.addEventListener("click", () => {
  submitQuiz(false);
});

els.resetBtn.addEventListener("click", () => {
  if (!confirm("Xóa toàn bộ đáp án đã chọn và làm lại từ đầu?")) return;
  state.answers = {};
  state.submitted = false;
  state.autoSubmitted = false;
  state.attemptRecorded = false;
  startTimer(true);
  saveState();
  updateStats();
  renderResult();
  renderQuestions();
  renderNavigator();
});

els.clearHistoryBtn.addEventListener("click", () => {
  if (!confirm("Xóa toàn bộ lịch sử làm bài?")) return;
  state.history = [];
  saveHistory();
  renderHistory();
});

els.prevBtn.addEventListener("click", () => {
  state.currentIndex -= 1;
  saveState();
  renderQuestions();
  renderNavigator();
  window.scrollTo({ top: 0, behavior: "smooth" });
});

els.nextBtn.addEventListener("click", () => {
  state.currentIndex += 1;
  saveState();
  renderQuestions();
  renderNavigator();
  window.scrollTo({ top: 0, behavior: "smooth" });
});

els.jumpBtn.addEventListener("click", () => {
  const target = Number(els.jumpInput.value);
  if (!Number.isFinite(target) || target < 1 || target > state.questions.length) return;
  const visibleQuestions = getVisibleQuestions();
  const idx = visibleQuestions.findIndex((q) => state.questions.indexOf(q) === target - 1);
  if (idx >= 0) {
    state.currentIndex = idx;
    saveState();
    renderQuestions();
    renderNavigator();
    window.scrollTo({ top: 0, behavior: "smooth" });
  }
});

loadQuiz().catch((error) => {
  els.quizTitle.textContent = "Không tải được đề";
  els.questionHost.innerHTML = `<p>Lỗi: ${error.message}</p>`;
});
