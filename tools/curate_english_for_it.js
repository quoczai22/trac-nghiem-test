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
    41, 46, 49, 50, 55, 58, 59, 60, 64, 65, 66, 67, 73,
  ],
  2: [
    77, 78, 80,
    84, 85, 86, 87, 88, 92, 94, 96, 98, 100, 102, 104, 106, 108,
    115, 117, 118, 120, 125, 126, 127, 129, 134, 138, 143,
    148, 149, 156,
  ],
  3: [
    166, 167, 168, 169, 170,
    171, 172, 173, 174, 176, 178, 180, 182, 184, 188, 190,
    194, 196, 200, 202, 206, 207, 209,
    213, 215, 219, 225,
  ],
  4: [
    234, 235, 237, 238,
    239, 240, 241, 243, 245, 247, 253,
    258, 259, 261, 263, 268, 275, 277, 281, 282, 288,
  ],
  5: [
    296, 297, 298,
    302, 303, 304, 306, 308, 312, 314, 318,
    324, 326, 327, 328, 332, 334, 338,
  ],
  6: [
    345, 346, 347, 348, 349, 350, 351,
    352, 358, 360, 362, 364, 367,
    376, 377, 378, 381,
    385, 394, 395, 396, 400, 403, 404,
  ],
  7: [
    414, 415,
    422, 424, 426, 438,
    443, 444, 453, 455, 461, 467, 472,
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

if (questions.length !== ids.size) {
  throw new Error("The selected question IDs are not unique.");
}

const data = {
  title: "English for IT - English For Tech",
  count: questions.length,
  questions,
};
const outputPath = path.join(__dirname, "..", "subjects", "english-for-it", "questions.js");
fs.writeFileSync(outputPath, `window.__QUIZ_DATA__ = ${JSON.stringify(data, null, 2)};\n`, "utf8");
console.log(`Wrote ${questions.length} English-only questions: ${Object.entries(selected).map(([unit, list]) => `Unit ${unit}: ${list.length}`).join(", ")}`);
