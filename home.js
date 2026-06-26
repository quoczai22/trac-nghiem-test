function renderSubjects() {
  const grid = document.getElementById("subjectGrid");
  const subjects = window.QuizSubjects.list();
  grid.innerHTML = "";

  subjects.forEach((subject) => {
    const card = document.createElement("a");
    card.className = "subject-card active";
    card.href = subject.href;
    card.dataset.subject = subject.id;

    const icon = document.createElement("span");
    icon.className = "icon";
    icon.textContent = subject.icon;

    const content = document.createElement("div");
    content.className = "subject-content";

    const badge = document.createElement("span");
    badge.className = "subject-badge";
    badge.textContent = subject.id === "he-dieu-hanh" ? "Ngân hàng luyện rộng" : "Đề mô phỏng cố định";

    const title = document.createElement("h2");
    title.textContent = subject.title;

    const description = document.createElement("p");
    description.textContent = subject.description;

    const meta = document.createElement("p");
    meta.className = "subject-meta";
    meta.textContent = subject.id === "he-dieu-hanh"
      ? "Chương 1-8, random đề, lưu lịch sử làm bài."
      : "Unit 7-12, có vocab, grammar, cloze và reading.";

    const status = document.createElement("strong");
    status.textContent = subject.kind === "static" ? "Đang có sẵn" : "Môn local";

    content.append(badge, title, description, meta, status);
    card.append(icon, content);
    grid.appendChild(card);
  });
}

renderSubjects();
window.addEventListener("pageshow", renderSubjects);
