(function registerSubjectRegistry() {
  const DEFAULT_SUBJECTS = [
    {
      id: "anh-van-3",
      title: "Anh văn 3",
      icon: "A3",
      description: "Ngân hàng trắc nghiệm Anh văn 3, mở vào là làm luôn trên web.",
      units: [7, 8, 9, 10, 11, 12].map((unit) => ({ id: String(unit), label: `Unit ${unit}` })),
      kind: "local",
      href: "./subjects/anh-van-3/index.html",
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
    throw new Error("Bản này chỉ giữ lại một môn duy nhất là Anh văn 3.");
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
