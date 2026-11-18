// Build the public English for IT bank from a locally reviewed source JSON.
// Usage: node tools/curate_english_for_it.js <source-json>
const fs = require("node:fs");
const path = require("node:path");

const sourcePath = process.argv[2];
if (!sourcePath) {
  throw new Error("Pass the source question-bank JSON path.");
}

const selected = {
  1: [
    4, 5, 6, 7, 9, 10,
    11, 12, 13, 14, 15, 16, 18, 20, 22, 24, 26, 28, 30, 32,
    41, 49, 50, 55, 58, 60, 65, 66, 67, 73,
  ],
  2: [
    77, 78, 80,
    84, 85, 86, 87, 88, 92, 94, 96, 98, 100, 102, 104, 106, 108,
    115, 117, 118, 120, 125, 126, 134, 138, 143, 149, 156,
  ],
  3: [
    166, 167, 168, 169, 170,
    171, 172, 173, 174, 176, 178, 180, 182, 184, 188, 190,
    194, 196, 200, 202, 207, 213, 219, 225,
  ],
  4: [
    234, 235, 237, 238,
    239, 240, 241, 243, 245, 247, 253,
    259, 261, 263, 268, 275, 277, 281,
  ],
  5: [
    296, 297, 298,
    302, 303, 304, 306, 308, 312, 314, 318,
    324, 326, 327, 328,
  ],
  6: [
    345, 346, 347, 348, 349, 350, 351,
    352, 358, 360, 362, 364, 367,
    376, 377, 378, 381,
    385, 400, 403, 404,
  ],
  7: [
    414, 415,
    422, 424, 426, 438,
    443, 444, 455, 467,
  ],
};

const englishPrompts = {
  4: "Which Present Simple question follows the pattern in the book?",
  5: "What is the -ing form of 'debug'?",
  6: "Which time marker is commonly used with Present Simple?",
  7: "Which time marker is commonly used with Present Continuous?",
  9: "Which verb describing a state does the book usually use in Present Simple rather than Present Continuous?",
  10: "Which Present Simple negative sentence matches the example in the book?",
  77: "Which tense is commonly used with 'yesterday'?",
  78: "Which sentence uses Present Perfect for a period continuing to now?",
  80: "What is the affirmative Present Perfect form shown in the book?",
  166: "What is the short form of 'will not'?",
  167: "Which form is used for a decision made at the moment of speaking?",
  168: "Which form is used for a plan decided before speaking?",
  169: "Which form does the book use for a prediction based on present evidence?",
  170: "Which question follows the 'be going to' pattern in the book?",
  234: "What is the comparative form of 'big'?",
  235: "What is the superlative form of 'wide'?",
  237: "What is the irregular comparative form of 'good'?",
  238: "What is the irregular superlative form of 'bad'?",
  296: "Complete the phrase from the book: find _____ time for it.",
  297: "Which noun from the book is countable?",
  298: "Which noun from the book is uncountable?",
  345: "Which Present Perfect passive sentence appears in the book's table?",
  346: "Which passive sentence with a modal follows the book's table?",
  347: "What is the passive-voice pattern shown in the book?",
  348: "Which preposition introduces the person doing the action in a passive sentence?",
  349: "Which Present Simple passive sentence appears in the book's table?",
  350: "Which Past Simple passive sentence appears in the book's table?",
  351: "Which modal passive sentence appears in the book's table?",
  414: "What is the past form of 'have to' in the book's table?",
  415: "What is the future form of 'have to' in the book's table?",
};

// Short passages are adapted from the indicated reading pages; every blank
// tests a term or construction taught on that page.
const passages = [
  {
    unit: 1,
    bookPage: 14,
    text: "DevOps engineers help (1) _____ development time and improve communication between developers, testers and system administrators. Beginners in this field learn programming languages, operating systems, cloud computing and (2) _____. They need to understand a broad range of (3) _____ before working with code releases and deployments.",
    blanks: [
      { options: { A: "shorten", B: "collect", C: "qualify", D: "specialize" }, answer: "A" },
      { options: { A: "transactions", B: "networking", C: "stakeholders", D: "pitching" }, answer: "B" },
      { options: { A: "technologies", B: "customers", C: "transactions", D: "buttons" }, answer: "A" },
    ],
  },
  {
    unit: 2,
    bookPage: 34,
    text: "A startup begins with an idea that solves a customer (1) _____. The team should ask whether its solution is elegant and (2) _____. As the company grows, it needs people with the right skills and a shared vision. An incubator can provide mentorship, equipment and (3) _____ opportunities.",
    blanks: [
      { options: { A: "pitch deck", B: "pain point", C: "shareholder", D: "budget" }, answer: "B" },
      { options: { A: "concise", B: "prospective", C: "scalable", D: "annual" }, answer: "C" },
      { options: { A: "networking", B: "debugging", C: "testing", D: "coding" }, answer: "A" },
    ],
  },
  {
    unit: 3,
    bookPage: 56,
    text: "AI can gather user data and track user (1) _____. Businesses can turn this data into predictions and use them to improve their (2) _____. The reading notes that AI may remove some low-skilled jobs, but it may also create more (3) _____ jobs.",
    blanks: [
      { options: { A: "behavior", B: "architecture", C: "software", D: "hardware" }, answer: "A" },
      { options: { A: "interface", B: "strategy", C: "profile", D: "simulation" }, answer: "B" },
      { options: { A: "low-skilled", B: "high-skilled", C: "obsolete", D: "virtual" }, answer: "B" },
    ],
  },
  {
    unit: 4,
    bookPage: 72,
    text: "Python is often recommended for beginners because its (1) _____ is straightforward. It is also used in Machine Learning and Artificial Intelligence. Java is common in large (2) _____ projects and backend applications. PHP has traditionally been a language of the (3) _____.",
    blanks: [
      { options: { A: "syntax", B: "terminal", C: "runtime", D: "platform" }, answer: "A" },
      { options: { A: "enterprise", B: "mobile", C: "gaming", D: "freelance" }, answer: "A" },
      { options: { A: "desktop", B: "web", C: "cloud", D: "server" }, answer: "B" },
    ],
  },
  {
    unit: 5,
    bookPage: 90,
    text: "Git is a (1) _____ system that tracks changes to source code. GitHub is different: it is a (2) _____ service for repositories. To contribute to an open-source project, developers can fork a repo and create a (3) _____ to share their changes with the original authors.",
    blanks: [
      { options: { A: "version control", B: "runtime", C: "testing", D: "cloud" }, answer: "A" },
      { options: { A: "programming", B: "hosting", C: "design", D: "testing" }, answer: "B" },
      { options: { A: "branch", B: "commit", C: "pull request", D: "repository" }, answer: "C" },
    ],
  },
  {
    unit: 6,
    bookPage: 104,
    text: "A clear bug report describes the problem and lists steps to (1) _____ it. It can include a screenshot and a clickable (2) _____. The testing team should define its objectives and write clear test (3) _____. This helps developers understand what went wrong.",
    blanks: [
      { options: { A: "reproduce", B: "compile", C: "deploy", D: "merge" }, answer: "A" },
      { options: { A: "branch", B: "URL", C: "commit", D: "database" }, answer: "B" },
      { options: { A: "cases", B: "branches", C: "repositories", D: "sprints" }, answer: "A" },
    ],
  },
  {
    unit: 7,
    bookPage: 122,
    text: "Agile is flexible because it relies on (1) _____ and lets teams adjust their work. Kanban uses a visual (2) _____ to show what has been accomplished and where setbacks remain. Scrum organizes work into (3) _____ that usually last less than 30 days and lead to a working demo.",
    blanks: [
      { options: { A: "iterations", B: "queries", C: "tickets", D: "repos" }, answer: "A" },
      { options: { A: "terminal", B: "board", C: "database", D: "report" }, answer: "B" },
      { options: { A: "commits", B: "releases", C: "sprints", D: "features" }, answer: "C" },
    ],
  },
];

const source = JSON.parse(fs.readFileSync(sourcePath, "utf8"));
const byId = new Map(source.questions.map((question) => [Number(question.id.split("-")[1]), question]));
const ids = new Set(Object.values(selected).flat());
const questions = [];

for (const [unit, numbers] of Object.entries(selected)) {
  for (const number of numbers) {
    const original = byId.get(number);
    if (!original || original.unit !== Number(unit)) {
      throw new Error(`Question EIT-${number} is missing or assigned to the wrong unit.`);
    }

    let prompt = englishPrompts[number] || original.question;
    if (original.type === "acronym") {
      const acronym = prompt.split(" ")[0];
      prompt = `What does ${acronym} stand for?`;
    } else if (original.type === "glossary-term") {
      const definition = prompt.replace(/^Theo glossary, thuật ngữ nào khớp với định nghĩa:\s*/u, "");
      prompt = `Which term matches this definition from the book's glossary? ${definition}`;
    }

    if (/[\u00c0-\u1ef9]/u.test(prompt) || Object.values(original.options).some((option) => /[\u00c0-\u1ef9]/u.test(option))) {
      throw new Error(`Non-English text remains in ${original.id}.`);
    }
    if (!prompt.trim() || !["A", "B", "C", "D"].every((letter) => original.options[letter]?.trim())) {
      throw new Error(`Incomplete question ${original.id}.`);
    }
    if (new Set(Object.values(original.options).map((option) => option.toLowerCase().trim())).size !== 4) {
      throw new Error(`Repeated options in ${original.id}.`);
    }
    if (!original.options[original.answer] || !Number.isInteger(original.book_page)) {
      throw new Error(`Missing answer or book page in ${original.id}.`);
    }

    questions.push({
      id: original.id,
      chapter: unit,
      question: prompt,
      options: original.options,
      answer: original.answer,
      bookPage: original.book_page,
    });
  }
}

for (const passage of passages) {
  passage.blanks.forEach((blank, index) => {
    if (!passage.text.includes(`(${index + 1}) _____`) || !blank.options[blank.answer]) {
      throw new Error(`Invalid passage blank in Unit ${passage.unit}.`);
    }
    questions.push({
      id: `EIT-P${passage.unit}-${index + 1}`,
      chapter: String(passage.unit),
      question: `Choose the best word or phrase for blank (${index + 1}).`,
      passage: passage.text,
      passageGroup: `EIT-P${passage.unit}`,
      passageAdapted: true,
      options: blank.options,
      answer: blank.answer,
      bookPage: passage.bookPage,
    });
  });
}

if (questions.length !== 167 || new Set(questions.map((question) => question.id)).size !== questions.length || ids.size + passages.length * 3 !== questions.length) {
  throw new Error("The selected question IDs are not unique.");
}

const data = {
  title: "English for IT - Trọng tâm có bài đọc",
  count: questions.length,
  questions,
};
const outputPath = path.join(__dirname, "..", "subjects", "english-for-it", "questions.js");
fs.writeFileSync(outputPath, `window.__QUIZ_DATA__ = ${JSON.stringify(data, null, 2)};\n`, "utf8");
console.log(`Wrote ${questions.length} English-only questions: ${Object.entries(selected).map(([unit, list]) => `Unit ${unit}: ${list.length}`).join(", ")}`);

if (source.questions.length !== 475) {
  throw new Error(`Expected 475 source questions, found ${source.questions.length}.`);
}
const reviewQuestions = source.questions.map((original) => {
  if (!original.id || !original.question || !["A", "B", "C", "D"].every((letter) => original.options?.[letter]?.trim()) || !original.options[original.answer] || !Number.isInteger(original.book_page)) {
    throw new Error(`Incomplete review question ${original.id}.`);
  }
  return {
    id: original.id,
    chapter: String(original.unit),
    question: original.question,
    options: original.options,
    answer: original.answer,
    bookPage: original.book_page,
  };
});
const reviewData = {
  title: "English for IT - Ôn rộng",
  count: reviewQuestions.length,
  questions: reviewQuestions,
};
const reviewPath = path.join(__dirname, "..", "subjects", "english-for-it", "review-questions.js");
fs.writeFileSync(reviewPath, `window.__QUIZ_DATA__ = ${JSON.stringify(reviewData, null, 2)};\n`, "utf8");
console.log(`Wrote ${reviewQuestions.length} broad-review questions.`);
