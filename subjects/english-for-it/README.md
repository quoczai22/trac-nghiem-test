# English for IT question bank

There are two public banks from the seven units of *English For Tech*:

- `questions.js`: 167 English-only, four-option questions for focused practice,
  including seven adapted reading passages with three linked blanks each.
- `review-questions.js`: the original 475-question broad review bank, including
  Vietnamese prompts and supplemental questions.

The focused quiz selects complete passage groups and keeps their blanks
consecutive. Each question includes the printed book page (`bookPage`). The source JSON
remains local; the textbook PDF is not shipped with the site. The two quiz
entries have separate saved progress and history.

Selection favors each unit's stated grammar topic and IT vocabulary. Repeated
reverse glossary questions, incidental filler-word clozes, off-topic terms, and
questions with more than one plausible answer are omitted. The website's quiz
runner and the other subject banks are unchanged.

To rebuild after reviewing the local source JSON:

```sh
node tools/curate_english_for_it.js /path/to/english_for_it_475_cau.json
```

Review the generated questions and answer keys before publishing future changes.
