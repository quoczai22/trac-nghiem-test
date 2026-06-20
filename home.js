function renderSubjects() {
  const grid = document.getElementById("subjectGrid");
  const subjects = window.QuizSubjects.list();
  grid.innerHTML = "";

  subjects.forEach((subject) => {
    const card = document.createElement("a");
    card.className = "subject-card active";
    card.href = subject.href;

    const icon = document.createElement("span");
    icon.className = "icon";
    icon.textContent = subject.icon;

    const content = document.createElement("div");
    const title = document.createElement("h2");
    title.textContent = subject.title;
    const description = document.createElement("p");
    description.textContent = subject.description;
    const status = document.createElement("strong");
    status.textContent = subject.kind === "static" ? "Đang có sẵn" : "Môn local";

    content.append(title, description, status);
    card.append(icon, content);
    grid.appendChild(card);
  });
}

renderSubjects();
window.addEventListener("pageshow", renderSubjects);
