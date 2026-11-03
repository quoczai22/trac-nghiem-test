const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const dataContext = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(root, "subjects/an-toan-mang/questions.js"), "utf8"), dataContext);
const bank = dataContext.window.__QUIZ_DATA__.questions;
assert.equal(bank.length, 500);

const counts = bank.reduce((result, question) => {
  assert.ok(question.options[question.answer], question.id);
  result[question.chapter] = (result[question.chapter] || 0) + 1;
  return result;
}, {});
assert.deepEqual(counts, { 1: 50, 2: 100, 3: 100, 4: 100, 5: 100, 6: 50 });

const app = fs.readFileSync(path.join(root, "subjects/quiz/app.js"), "utf8");
const start = app.indexOf("function pickBalancedAtmQuestions(count)");
const end = app.indexOf("function createNewRandomQuiz()", start);
assert.ok(start >= 0 && end > start);
const picker = vm.runInNewContext(
  `${app.slice(start, end)}; pickBalancedAtmQuestions`,
  { state: { bank }, shuffleArray: (items) => [...items].reverse() }
);

for (const count of [10, 20, 40, 50, 100, 500]) {
  const selected = picker(count);
  assert.equal(selected.length, count);
  assert.equal(new Set(selected.map((question) => question.id)).size, count);
  if (count < 500) {
    assert.equal(new Set(selected.map((question) => question.family)).size, count);
    const expected = [1, 2, 2, 2, 2, 1].map((weight) => (count * weight) / 10);
    for (let chapter = 1; chapter <= 6; chapter += 1) {
      assert.equal(selected.filter((question) => Number(question.chapter) === chapter).length, expected[chapter - 1]);
    }
  }
}

const registryContext = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(root, "shared/subjects-registry.js"), "utf8"), registryContext);
assert.equal(registryContext.window.QuizSubjects.get("an-toan-mang").units.length, 6);
assert.ok(registryContext.window.QuizSubjects.get("he-dieu-hanh"));
assert.ok(registryContext.window.QuizSubjects.get("anh-van-3"));

const sourceContext = {
  window: { __SUBJECT_DEFAULT_DATA__: {} },
  localStorage: { getItem: () => null },
  IMPORTED_DATA_KEY: "unused-in-test",
};
vm.runInNewContext(fs.readFileSync(path.join(root, "subjects/anh-van-3/questions.js"), "utf8"), sourceContext);
sourceContext.window.__SUBJECT_DEFAULT_DATA__["anh-van-3"] = sourceContext.window.__QUIZ_DATA__;
vm.runInNewContext(fs.readFileSync(path.join(root, "subjects/an-toan-mang/questions.js"), "utf8"), sourceContext);
sourceContext.window.__SUBJECT_DEFAULT_DATA__["an-toan-mang"] = sourceContext.window.__QUIZ_DATA__;
const sourceStart = app.indexOf("function getQuizDataSource()");
const sourceEnd = app.indexOf("const state =", sourceStart);
for (const id of ["anh-van-3", "an-toan-mang"]) {
  sourceContext.subject = { id, title: id };
  const result = vm.runInNewContext(`${app.slice(sourceStart, sourceEnd)}; getQuizDataSource()`, sourceContext);
  assert.equal(result.questions.length, id === "an-toan-mang" ? 500 : sourceContext.window.__SUBJECT_DEFAULT_DATA__["anh-van-3"].questions.length);
  assert.equal(result, sourceContext.window.__SUBJECT_DEFAULT_DATA__[id]);
}

console.log("ATM bank, subject registry, and balanced random selection: OK");
