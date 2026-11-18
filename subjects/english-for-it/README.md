# English for IT question bank

The public bank is `questions.js`. It contains 167 English-only, four-option
questions selected from the seven units of *English For Tech*. Each question
includes the printed book page (`bookPage`). The original source JSON remains
local; the textbook PDF is not shipped with the site.

Selection favors each unit's stated grammar topic and IT vocabulary. Repeated
reverse glossary questions, incidental filler-word clozes, off-topic terms, and
questions with more than one plausible answer are omitted. The website's quiz
runner and the other subject banks are unchanged.

To rebuild after reviewing the local source JSON:

```sh
node tools/curate_english_for_it.js /path/to/english_for_it_475_cau.json
```

Review the generated questions and answer keys before publishing future changes.
