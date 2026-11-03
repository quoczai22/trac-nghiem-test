"""Convert the reviewed ATM JSON bank to the static quiz page's data format.

Usage: python tools/convert_atm_bank.py path/to/an_toan_mang_chon_loc.json

The acronym/standards supplement in tools/atm_supplement.py is merged in, the
weak items it lists in REMOVE_IDS are dropped, and the items in OVERRIDES are
rewritten.
"""

import hashlib
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from atm_supplement import OVERRIDES, QUESTIONS as SUPPLEMENT, REMOVE_IDS  # noqa: E402


def apply_override(item: dict) -> dict:
    if item["id"] not in OVERRIDES:
        return item
    question, correct, *wrong = OVERRIDES[item["id"]]
    options = list(wrong)
    options.insert(item["answer"], correct)
    return {**item, "question": question, "options": options}


def supplement_items() -> list:
    # Each block of four questions uses every answer position once, so A-D stay balanced.
    rng = random.Random(int(hashlib.sha256(b"atm-supplement").hexdigest(), 16))
    positions = []
    while len(positions) < len(SUPPLEMENT):
        block = [0, 1, 2, 3]
        rng.shuffle(block)
        positions.extend(block)
    items = []
    for index, (chapter, section, style, family, question, correct, *wrong, source) in enumerate(SUPPLEMENT, 1):
        prefix = {"acronym": "abbr", "standard": "std"}.get(style, "rev")
        item_id = f"{prefix}_c{chapter}_{index:03d}"
        rng.shuffle(wrong)
        options = list(wrong)
        options.insert(positions[index - 1], correct)
        items.append({
            "id": item_id,
            "chapter": chapter,
            "section": section,
            "question": question,
            "options": options,
            "answer": options.index(correct),
            "family": family or item_id,
            "style": style,
            "source": source,
        })
    return items


def main() -> None:
    source = Path(sys.argv[1]).resolve()
    target = Path(__file__).resolve().parents[1] / "subjects" / "an-toan-mang" / "questions.js"
    bank = json.loads(source.read_text(encoding="utf-8"))
    letters = "ABCD"
    questions = []
    items = [apply_override(item) for item in bank["questions"]] + supplement_items()
    # Filtering after the merge keeps supplement ids stable when a supplement item is dropped.
    items = [item for item in items if item["id"] not in REMOVE_IDS]
    items.sort(key=lambda item: int(item["chapter"]))
    for item in items:
        options = item["options"]
        answer = item["answer"]
        if len(options) != 4 or not 0 <= answer < 4:
            raise ValueError(f"Invalid question {item['id']}")
        questions.append({
            "id": item["id"],
            "chapter": str(item["chapter"]),
            "question": item["question"],
            "options": dict(zip(letters, options)),
            "answer": letters[answer],
            "family": item["family"],
            "style": item.get("style", "review"),
            "section": item["section"],
            "source": item["source"],
        })

    if not questions:
        raise ValueError("The ATM question bank is empty")
    data = {
        "title": "Ngân hàng trắc nghiệm An toàn mạng máy tính",
        "count": len(questions),
        "sourceCounts": {"default": len(questions)},
        "questions": questions,
    }
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("window.__QUIZ_DATA__ = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
    print(f"Wrote {len(questions)} questions to {target}")


if __name__ == "__main__":
    main()
