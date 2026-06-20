(function registerSubjectRegistry() {
  const STORAGE_KEY = "quiz_subject_registry_v1";

  const DEFAULT_SUBJECTS = [
    {
      id: "he-dieu-hanh",
      title: "Hệ điều hành",
      icon: "💻",
      description: "Ngân hàng câu hỏi chương 1-8, random đề, lưu lịch sử làm bài.",
      units: Array.from({ length: 8 }, (_, index) => ({ id: String(index + 1), label: `Chương ${index + 1}` })),
      kind: "static",
      href: "./subjects/he-dieu-hanh/index.html",
    },
  ];

  function clone(value) {
    return JSON.parse(JSON.stringify(value));
  }

  function readCustomSubjects() {
    try {
      const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
      return Array.isArray(saved) ? saved : [];
    } catch (error) {
      console.warn("Không đọc được danh sách môn local:", error);
      return [];
    }
  }

  function writeCustomSubjects(subjects) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(subjects));
  }

  function normalizeSlug(value) {
    const base = String(value || "")
      .normalize("NFD")
      .replace(/[\u0300-\u036f]/g, "")
      .toLowerCase()
      .replace(/đ/g, "d")
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "");
    return base || "mon-moi";
  }

  function list() {
    return [...clone(DEFAULT_SUBJECTS), ...readCustomSubjects()];
  }

  function get(id) {
    return list().find((subject) => subject.id === id) || null;
  }

  function create({ title, icon, description, unitType, unitCount }) {
    const cleanTitle = String(title || "").trim();
    if (!cleanTitle) throw new Error("Bạn cần nhập tên môn.");

    const count = Number(unitCount);
    if (!Number.isInteger(count) || count < 1 || count > 30) {
      throw new Error("Số chương/bài phải từ 1 đến 30.");
    }

    const type = unitType === "Bài" || unitType === "Bai" ? "Bài" : "Chương";
    const custom = readCustomSubjects();
    const baseId = normalizeSlug(cleanTitle);
    let id = baseId;
    let suffix = 2;
    while (get(id)) {
      id = `${baseId}-${suffix}`;
      suffix += 1;
    }

    const subject = {
      id,
      title: cleanTitle,
      icon: String(icon || "📚").trim() || "📚",
      description: String(description || "Môn học tạo local, chờ thêm dữ liệu câu hỏi.").trim(),
      units: Array.from({ length: count }, (_, index) => ({ id: String(index + 1), label: `${type} ${index + 1}` })),
      kind: "local",
      href: `./subjects/quiz/index.html?subject=${encodeURIComponent(id)}`,
      createdAt: new Date().toISOString(),
    };

    custom.push(subject);
    writeCustomSubjects(custom);
    return clone(subject);
  }

  window.QuizSubjects = {
    storageKey: STORAGE_KEY,
    list,
    get,
    create,
    isDefault(id) {
      return DEFAULT_SUBJECTS.some((subject) => subject.id === id);
    },
  };
})();
