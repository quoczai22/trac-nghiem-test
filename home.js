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

function renderStartMenu() {
  const subjects = window.QuizSubjects.list();
  const toggle = document.getElementById("startToggle");
  const menu = document.getElementById("startMenu");
  if (!toggle || !menu) return;

  menu.innerHTML = "";

  subjects.forEach((subject) => {
    const link = document.createElement("a");
    link.className = "dropdown-item";
    link.href = subject.href;
    link.setAttribute("role", "menuitem");
    link.innerHTML = `
      <span class="dropdown-icon">${subject.icon}</span>
      <span class="dropdown-copy">
        <strong>${subject.title}</strong>
        <small>${subject.description}</small>
      </span>
    `;
    menu.appendChild(link);
  });

  function closeMenu() {
    menu.classList.add("hidden");
    toggle.setAttribute("aria-expanded", "false");
  }

  toggle.onclick = () => {
    const isHidden = menu.classList.contains("hidden");
    menu.classList.toggle("hidden", !isHidden);
    toggle.setAttribute("aria-expanded", String(isHidden));
  };

  document.addEventListener("click", (event) => {
    if (!menu.contains(event.target) && !toggle.contains(event.target)) {
      closeMenu();
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeMenu();
  });
}

renderSubjects();
renderStartMenu();
window.addEventListener("pageshow", renderSubjects);
