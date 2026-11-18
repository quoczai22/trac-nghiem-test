const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.join(__dirname, "..");
const read = (file) => fs.readFileSync(path.join(root, file), "utf8");
const loadBank = (file) => {
  const context = { window: {} };
  vm.runInNewContext(read(file), context);
  return context.window.__QUIZ_DATA__;
};

const focused = loadBank("subjects/english-for-it/questions.js");
const review = loadBank("subjects/english-for-it/review-questions.js");
assert.equal(focused.questions.length, 167);
assert.equal(review.questions.length, 475);
assert.equal(focused.count, 167);
assert.equal(review.count, 475);

const passageGroups = new Map();
for (const question of focused.questions) {
  assert.ok(question.options[question.answer], question.id);
  assert.equal(Object.keys(question.options).length, 4, question.id);
  assert.ok(question.bookPage, question.id);
  assert.ok(!/[\u00c0-\u1ef9]/u.test(question.question + Object.values(question.options).join("")), question.id);
  if (!question.passageGroup) continue;
  const group = passageGroups.get(question.passageGroup) || [];
  group.push(question);
  passageGroups.set(question.passageGroup, group);
}
assert.equal(passageGroups.size, 7);
for (const [id, group] of passageGroups) {
  assert.equal(group.length, 3, id);
  assert.ok(group.every((question) => question.passage === group[0].passage), id);
  for (let index = 1; index <= 3; index += 1) {
    assert.ok(group[0].passage.includes(`(${index}) _____`), id);
  }
}

const registry = { window: {} };
vm.runInNewContext(read("shared/subjects-registry.js"), registry);
assert.equal(registry.window.QuizSubjects.get("english-for-it").kind, "local");
assert.equal(registry.window.QuizSubjects.get("english-for-it-review").kind, "local");
for (const file of ["subjects/quiz/index.html", "admin/import-export.html"]) {
  assert.ok(read(file).includes('window.__SUBJECT_DEFAULT_DATA__["english-for-it"]'), file);
  assert.ok(read(file).includes('window.__SUBJECT_DEFAULT_DATA__["english-for-it-review"]'), file);
}

const app = read("subjects/quiz/app.js");
const begin = app.indexOf("function pickEnglishForItQuestions(");
const end = app.indexOf("\nfunction pickBalancedAtmQuestions(", begin);
assert.ok(begin >= 0 && end > begin);
const context = {
  state: { bank: focused.questions },
  seenRounds: {},
  shuffleArray: (items) => [...items].sort(() => Math.random() - 0.5),
  freshFirst: (items) => items,
  familyKey: (question) => question.family || question.id || question.question,
};
vm.createContext(context);
vm.runInContext(`${app.slice(begin, end)}\nthis.pick = pickEnglishForItQuestions;`, context);

function checkGroups(questions) {
  for (const [id] of passageGroups) {
    const indexes = questions.flatMap((question, index) => question.passageGroup === id ? [index] : []);
    if (!indexes.length) continue;
    assert.equal(indexes.length, 3, id);
    assert.equal(indexes[2] - indexes[0], 2, id);
  }
}

for (const count of [10, 20, 40, 50, 100, 167]) {
  for (let iteration = 0; iteration < 20; iteration += 1) {
    const questions = context.pick(count);
    assert.equal(questions.length, count);
    assert.equal(new Set(questions.map((question) => question.id)).size, count);
    checkGroups(questions);
    if (count === 50) assert.equal(questions.filter((question) => question.passageGroup).length, 6);
  }
}
for (let unit = 1; unit <= 7; unit += 1) {
  const questions = context.pick(10, String(unit));
  assert.equal(questions.length, 10);
  assert.ok(questions.every((question) => question.chapter === String(unit)));
  assert.equal(questions.filter((question) => question.passageGroup).length, 3);
  checkGroups(questions);
}

const firstPassages = new Set(context.pick(50).filter((question) => question.passageGroup).map((question) => question.passageGroup));
for (const id of firstPassages) {
  context.seenRounds[`${id}-1`] = 1;
}
const nextPassages = new Set(context.pick(50).filter((question) => question.passageGroup).map((question) => question.passageGroup));
assert.ok([...firstPassages].every((id) => !nextPassages.has(id)));

console.log("English for IT: 167 focused questions, 475 broad questions, grouped passages OK.");
