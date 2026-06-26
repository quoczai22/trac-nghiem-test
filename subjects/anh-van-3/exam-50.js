window.__QUIZ_EXAM_50__ = (() => {
  const base = window.__QUIZ_EXAM_40__;
  const extraQuestions = [
    {
      chapter: "10",
      question: "[Reading 3] Read the email and choose the best answer.\nJane wrote that she had applied for a waitressing job, but she didn't get it because the people there wanted someone with experience.\nWhy wasn't Jane working as a waitress?",
      options: {
        A: "She wanted something with more money.",
        B: "They wanted someone who had done that kind of work before.",
        C: "She wanted to work with children.",
      },
      answer: "B",
    },
    {
      chapter: "10",
      question: "[Reading 3] Read the email and choose the best answer.\nJane went to the zoo with Karen and the children. Adult tickets cost 20 pounds, each child ticket cost 15.50 pounds, and Jane had a 2-pound student discount while Karen paid for Jane's ticket.\nHow much did it cost for Jane and the children to get into the zoo?",
      options: { A: "49 pounds", B: "51 pounds", C: "52 pounds" },
      answer: "B",
    },
    {
      chapter: "10",
      question: "[Reading 3] Read the email and choose the best answer.\nJane said she hadn't been to a zoo since she was a little girl, but she remembered that her parents used to take her quite often.\nWhen she was a child, how often did Jane go to the zoo?",
      options: { A: "She never went to the zoo.", B: "Once.", C: "Regularly." },
      answer: "C",
    },
    {
      chapter: "10",
      question: "[Reading 3] Read the email and choose the best answer.\nJane wrote that the zoo was much bigger than she remembered and that there was so much to see.\nHow much did the ticket cost compared with the past?",
      options: { A: "The same as it used to.", B: "More than it used to.", C: "Less than it used to." },
      answer: "B",
    },
    {
      chapter: "10",
      question: "[Reading 3] Read the email and choose the best answer.\nJane said Ryan loved the reptile house with all those disgusting snakes, Julie liked the tigers, and Jane's favourite was the elephant house. She didn't know what it was about elephants, especially the babies, but she loved them.\nWhich animals does Jane not like?",
      options: { A: "Snakes", B: "Elephants", C: "Tigers" },
      answer: "A",
    },
    {
      chapter: "10",
      question: "[Grammar - Unit 10] About 400 million cups of coffee ______ every day in the USA.",
      options: { A: "drink", B: "drinks", C: "are drunk" },
      answer: "C",
    },
    {
      chapter: "10",
      question: "[Grammar - Unit 10] Facebook ______ by Mark Zuckerberg.",
      options: { A: "was created", B: "creates", C: "is created" },
      answer: "A",
    },
    {
      chapter: "12",
      question: "[Grammar - Unit 12] If I ______ to a different country now, I ______ to South Africa.",
      options: {
        A: "can move / definitely move",
        B: "could move / would definitely move",
        C: "can move / will definitely move",
      },
      answer: "B",
    },
    {
      chapter: "11",
      question: "[Grammar - Unit 11] \"I really don't like this film.\"\nChoose the best reported sentence.",
      options: {
        A: "She said she really wasn't liking the film.",
        B: "She told me she really didn't like the film.",
        C: "She said me she really didn't like the film.",
      },
      answer: "B",
    },
    {
      chapter: "11",
      question: "[Grammar - Unit 11] \"I want to go there tomorrow.\"\nChoose the best reported sentence.",
      options: {
        A: "She said she wanted to go there the day before.",
        B: "She told she wanted to go there the day before.",
        C: "She said she wanted to go there the next day.",
      },
      answer: "C",
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
