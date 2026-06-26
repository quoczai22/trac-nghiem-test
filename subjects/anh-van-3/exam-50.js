window.__QUIZ_EXAM_50__ = (() => {
  const base = window.__QUIZ_EXAM_40__;
  const extraQuestions = [
    {
      chapter: "9",
      question: "[Vocab - Unit 9] Information about a course, such as dates and fees, is usually given in a course ______.",
      options: { A: "outline", B: "history", C: "forest", D: "interview" },
      answer: "A",
    },
    {
      chapter: "10",
      question: "[Vocab - Unit 10] A short trip taken for pleasure, often to a nearby place, is an ______.",
      options: { A: "excursion", B: "argument", C: "engine", D: "experiment" },
      answer: "A",
    },
    {
      chapter: "7",
      question: "[Grammar - Unit 7] We ______ in this apartment since 2023.",
      options: { A: "live", B: "lived", C: "have lived", D: "are living" },
      answer: "C",
    },
    {
      chapter: "8",
      question: "[Grammar - Unit 8] Students ______ use this app can check their homework online.",
      options: { A: "who", B: "where", C: "which", D: "when" },
      answer: "A",
    },
    {
      chapter: "10",
      question: "[Grammar - Unit 10] These tickets ______ online, so you don't need to buy them at the station.",
      options: { A: "can book", B: "can be booked", C: "can booking", D: "can booked" },
      answer: "B",
    },
    {
      chapter: "11",
      question: "[Grammar - Unit 11] Hoa said that she ______ never visited Machu Picchu before.",
      options: { A: "has", B: "had", C: "have", D: "was" },
      answer: "B",
    },
    {
      chapter: "9",
      question: "[Cloze - Learning] Choose the best answer for blank (1).\nBefore I joined the evening class, I ______ the teacher's email carefully and prepared all the documents.",
      options: { A: "had read", B: "reads", C: "have read", D: "am reading" },
      answer: "A",
    },
    {
      chapter: "9",
      question: "[Cloze - Learning] Choose the best answer for blank (2).\nThe course was useful because the teacher gave clear ______ about the lessons and the final test.",
      options: { A: "information", B: "nature", C: "promotion", D: "journey" },
      answer: "A",
    },
    {
      chapter: "10",
      question: "[Reading 3] Read the passage and choose the best answer.\nDuring a walking tour in Venice, Mai learned that many people there travel by boat instead of by car. She was surprised by the narrow streets and the quiet canals. She said the city felt different from any place she had visited before.\nWhy did Mai think Venice was special?",
      options: { A: "Because it had many supermarkets", B: "Because people mostly travelled by car", C: "Because it felt different from other places", D: "Because the weather was very cold" },
      answer: "C",
    },
    {
      chapter: "10",
      question: "[Reading 3] Read the passage and choose the best answer.\nDuring a walking tour in Venice, Mai learned that many people there travel by boat instead of by car. She was surprised by the narrow streets and the quiet canals. She said the city felt different from any place she had visited before.\nHow do many people travel in Venice?",
      options: { A: "By boat", B: "By underground train", C: "By bicycle only", D: "By airplane" },
      answer: "A",
    },
  ];

  return {
    ...base,
    title: "Đề CLO Anh văn 3 - 50 câu",
    count: 50,
    sourceCounts: {
      vocab: 10,
      grammar: 20,
      cloze: 10,
      reading: 10,
    },
    questions: [...base.questions, ...extraQuestions],
  };
})();
