"""Convert the reviewed ATM JSON bank to the static quiz page's data format.

Usage: python tools/convert_atm_bank.py path/to/an_toan_mang_500_cau.json
"""

import json
import sys
from pathlib import Path


def main() -> None:
    source = Path(sys.argv[1]).resolve()
    target = Path(__file__).resolve().parents[1] / "subjects" / "an-toan-mang" / "questions.js"
    bank = json.loads(source.read_text(encoding="utf-8"))
    letters = "ABCD"
    questions = []
    for item in bank["questions"]:
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
            "section": item["section"],
            "source": item["source"],
        })

    if len(questions) != 500:
        raise ValueError(f"Expected 500 questions, found {len(questions)}")
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
