(function registerSubjectRegistry() {
  const DEFAULT_SUBJECTS = [
    {
      id: "he-dieu-hanh",
      title: "Hệ điều hành",
      icon: "💻",
      description: "Ngân hàng trắc nghiệm Hệ điều hành chương 1-8, random đề và lưu lịch sử làm bài.",
      units: Array.from({ length: 8 }, (_, index) => ({ id: String(index + 1), label: `Chương ${index + 1}` })),
      kind: "static",
      href: "./subjects/he-dieu-hanh/index.html",
    },
    {
      id: "anh-van-3",
      title: "Anh văn 3",
      icon: "A3",
      description: "Ngân hàng trắc nghiệm Anh văn 3, mở vào là làm luôn trên web.",
      units: [7, 8, 9, 10, 11, 12].map((unit) => ({ id: String(unit), label: `Unit ${unit}` })),
      kind: "local",
      href: "./subjects/quiz/index.html?subject=anh-van-3",
    },
  ];

  function clone(value) {
    return JSON.parse(JSON.stringify(value));
  }

  function list() {
    return clone(DEFAULT_SUBJECTS);
  }

  function get(id) {
    return list().find((subject) => subject.id === id) || null;
  }

  function create({ title, icon, description, unitType, unitCount }) {
    throw new Error("Bản này giữ sẵn Hệ điều hành và một mục Anh văn 3 duy nhất.");
  }

  window.QuizSubjects = {
    storageKey: "quiz_subject_registry_v1",
    list,
    get,
    create,
    isDefault(id) {
      return DEFAULT_SUBJECTS.some((subject) => subject.id === id);
    },
  };
})();
