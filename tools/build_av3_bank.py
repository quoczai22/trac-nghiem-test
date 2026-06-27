import json
import re
import unicodedata
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

from pypdf import PdfReader


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FILE = PROJECT_ROOT / "subjects" / "anh-van-3" / "questions.js"
SOURCE_ROOT = Path(r"D:\av3")
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:7b"
W_NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


PDF_PATTERNS = [
    "LIFE - Multiple choice Exercises (English B2) - With answers*.pdf",
]

DOCX_FILES = [
    "Progress Test 2-B1.docx",
    "Progress Test 2 - B2.docx",
]


ALWAYS_KEEP_SOURCES = {
    "AV3 de thi",
    "Co Thu review",
}


STRICT_SCOPE_RULES = {
    "7": [
        r"\bfor\b",
        r"\bsince\b",
        r"present perfect",
        r"past simple",
        r"how long",
        r"\byet\b",
        r"\bjust\b",
        r"\bever\b",
        r"\bnever\b",
        r"preposition",
        r"next to",
        r"opposite",
        r"between",
        r"in front of",
        r"\bnear\b",
        r"\bacross\b",
        r"\bthrough\b",
        r"\balong\b",
        r"\binside\b",
        r"\boutside\b",
        r"\bup\b",
        r"\bdown\b",
        r"organic",
        r"market stall",
        r"outweigh",
        r"variety",
        r"bring together",
        r"applicant",
        r"reference",
        r"promotion",
        r"unskilled",
        r"qualified",
        r"colleague",
        r"spacious",
        r"sales representative",
        r"fashion designer",
        r"shop assistant",
        r"ground floor",
        r"manager",
    ],
    "8": [
        r"zero conditional",
        r"first conditional",
        r"relative clause",
        r"\bwho\b",
        r"\bwhich\b",
        r"\bwhere\b",
        r"if .+ will",
        r"if .+ won'?t",
        r"disappears",
        r"awareness",
        r"die out",
        r"survive",
        r"\bshift\b",
        r"neglect",
        r"apatani",
        r"enduring voices",
        r"recording equipment",
        r"technology kits",
        r"language disappears",
        r"native language",
    ],
    "9": [
        r"past perfect",
        r"\bhad\b",
        r"subject question",
        r"how many people",
        r"who wrote",
        r"who called",
        r"who lives",
        r"when i got to the station",
        r"the train had left",
        r"\bvenice\b",
        r"trader",
        r"challenge",
        r"gondolier",
        r"property",
        r"move away",
        r"\bgift\b",
        r"quality of life",
        r"advantages",
        r"disadvantages",
        r"\bcrowd\b",
        r"\bhuge\b",
        r"\bincrease\b",
        r"archaeologists",
        r"paintings",
        r"user-friendly",
        r"pisa",
    ],
    "10": [
        r"passive",
        r"\bis\b .+\bby\b",
        r"\bare\b .+\bby\b",
        r"\bwas\b .+\bby\b",
        r"\bwere\b .+\bby\b",
        r"used to",
        r"didn'?t use to",
        r"flat",
        r"paid off",
        r"\bloan\b",
        r"withstand",
        r"\bgrid\b",
        r"\bton\b",
        r"\bcrops\b",
        r"wind turbine",
        r"electricity",
        r"facebook was created",
        r"youtube",
    ],
    "11": [
        r"reported speech",
        r"\bsaid\b",
        r"\btold\b",
        r"would produce",
        r"would help",
        r"golden record",
        r"voyager",
        r"spacecraft",
        r"launched",
        r"solar system",
        r"mission",
        r"\bfunction\b",
        r"classical",
        r"\bjazz\b",
        r"universe",
        r"life forms",
    ],
    "12": [
        r"second conditional",
        r"\bwould\b",
        r"if i",
        r"if you",
        r"if we",
        r"anywhere",
        r"everywhere",
        r"everyone",
        r"everybody",
        r"nobody",
        r"no one",
        r"someone",
        r"somebody",
        r"something",
        r"nothing",
        r"somewhere",
        r"anybody",
        r"anyone",
        r"wilderness protection mobile unit",
        r"\bpoacher",
        r"\bsponsor",
        r"\brelease\b",
        r"\bvictim",
        r"\billegal\b",
        r"\bpowder\b",
        r"endangered",
        r"rescue centre",
        r"cambodia",
    ],
}


READING_SCOPE_HINTS = [
    r"^\[Cloze\]",
    r"^\[Reading",
    r"fill in the blank",
    r"choose the correct",
    r"read the",
]


EXTERNAL_SCOPE_PATTERNS = [
    r"^\[Cloze\]",
    r"^\[Reading",
    r"fill in the blank",
    r"choose the correct",
    r"read the",
    r"\bfor\b",
    r"\bsince\b",
    r"present perfect",
    r"past simple",
    r"how long",
    r"\byet\b",
    r"\bjust\b",
    r"\bever\b",
    r"\bnever\b",
    r"preposition",
    r"next to",
    r"opposite",
    r"between",
    r"in front of",
    r"\bnear\b",
    r"\bacross\b",
    r"\bthrough\b",
    r"\balong\b",
    r"\binside\b",
    r"\boutside\b",
    r"\bup\b",
    r"\bdown\b",
    r"zero conditional",
    r"first conditional",
    r"relative clause",
    r"\bwho\b",
    r"\bwhich\b",
    r"\bwhere\b",
    r"past perfect",
    r"subject question",
    r"how many people",
    r"used to",
    r"passive",
    r"reported speech",
    r"\bsaid\b",
    r"\btold\b",
    r"second conditional",
    r"anywhere",
    r"everyone",
    r"nobody",
    r"someone",
    r"somebody",
    r"something",
    r"nothing",
    r"somewhere",
    r"anybody",
    r"anyone",
    r"organic",
    r"market stall",
    r"outweigh",
    r"variety",
    r"bring together",
    r"disappears",
    r"awareness",
    r"die out",
    r"survive",
    r"\bshift\b",
    r"neglect",
    r"apatani",
    r"enduring voices",
    r"technology kits",
    r"recording equipment",
    r"trader",
    r"challenge",
    r"gondolier",
    r"property",
    r"move away",
    r"\bgift\b",
    r"quality of life",
    r"advantages",
    r"disadvantages",
    r"\bcrowd\b",
    r"\bhuge\b",
    r"\bincrease\b",
    r"\bvenice\b",
    r"flat",
    r"paid off",
    r"\bloan\b",
    r"withstand",
    r"\bgrid\b",
    r"\bton\b",
    r"\bcrops\b",
    r"wind turbine",
    r"electricity",
    r"golden record",
    r"voyager",
    r"spacecraft",
    r"launched",
    r"solar system",
    r"mission",
    r"\bfunction\b",
    r"classical",
    r"\bjazz\b",
    r"universe",
    r"life forms",
    r"wilderness protection mobile unit",
    r"\bpoacher",
    r"\bsponsor",
    r"\brelease\b",
    r"\bvictim",
    r"\billegal\b",
    r"\bpowder\b",
    r"endangered",
    r"rescue centre",
    r"cambodia",
]


def has_nested_choice_markup(text):
    value = str(text or "")
    return bool(
        re.search(r"\b\d{1,3}\.\s", value)
        or re.search(r"\([ABCD]\)", value)
        or "MULTILPLE CHOICE QUESTIONS" in value
        or "Grammar (Unit" in value
        or "Part 3:" in value
    )


def is_suspicious_question(item):
    question = str(item.get("question") or "")
    options = item.get("options") or {}

    if not question or len(options) < 3:
        return True

    if item.get("answer") and item["answer"] not in options:
        return True

    for value in options.values():
        option_text = str(value or "").strip()
        if not option_text:
            return True
        if len(option_text) > 110:
            return True
        if has_nested_choice_markup(option_text):
            return True

    return False


def sanitize_questions(questions):
    clean = []
    dropped = []
    for item in questions:
        if is_suspicious_question(item):
            dropped.append(item)
        else:
            clean.append(item)
    return clean, dropped


def read_existing_payload():
    text = OUTPUT_FILE.read_text(encoding="utf-8")
    match = re.search(r"window\.__QUIZ_DATA__\s*=\s*(\{.*\})\s*;\s*$", text, re.S)
    if not match:
        raise RuntimeError("questions.js khong dung dinh dang window.__QUIZ_DATA__ = {...};")
    payload = json.loads(match.group(1))
    cleaned, dropped = sanitize_questions(payload.get("questions", []))
    if dropped:
        print(f"Dropped {len(dropped)} broken existing questions")
    payload["questions"] = cleaned
    payload["count"] = len(cleaned)
    payload["sourceCounts"] = {"imported": len(cleaned)}
    return payload


def normalize_spaces(text):
    return re.sub(r"\s+", " ", str(text or "").replace("\xa0", " ")).strip()


def clean_question(text):
    text = normalize_spaces(text)
    text = re.sub(r"^\d{1,3}\.\s*", "", text)
    return text.strip(" -")


def normalize_key(text):
    normalized = unicodedata.normalize("NFD", str(text or ""))
    normalized = "".join(ch for ch in normalized if unicodedata.category(ch) != "Mn")
    normalized = re.sub(r"[^a-zA-Z0-9]+", " ", normalized).strip().lower()
    return normalized


def question_blob(item):
    options = item.get("options") or {}
    option_text = " ".join(str(value or "") for value in options.values())
    return normalize_spaces(f"{item.get('question', '')} {option_text} {item.get('source', '')}")


def infer_scope_chapter(item):
    original = str(item.get("chapter") or "").strip()
    if original in STRICT_SCOPE_RULES:
        return original

    blob = question_blob(item)
    for chapter, patterns in STRICT_SCOPE_RULES.items():
        for pattern in patterns:
            if re.search(pattern, blob, re.I):
                return chapter
    return "tong-on"


def matches_strict_scope(item):
    source = str(item.get("source") or "").strip()
    if source in ALWAYS_KEEP_SOURCES:
        return True

    blob = question_blob(item)
    return any(re.search(pattern, blob, re.I) for pattern in EXTERNAL_SCOPE_PATTERNS)


def dedupe_flat_questions(items):
    seen = set()
    unique = []
    for item in items:
        key = normalize_key(item.get("question"))
        if not key or key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


def apply_strict_scope(questions):
    filtered = []
    for item in questions:
        if not matches_strict_scope(item):
            continue
        normalized = dict(item)
        normalized["chapter"] = infer_scope_chapter(normalized)
        filtered.append(normalized)
    return dedupe_flat_questions(filtered)


def extract_docx_text(path):
    with zipfile.ZipFile(path) as archive:
        xml_text = archive.read("word/document.xml")
    root = ET.fromstring(xml_text)
    paragraphs = []
    for para in root.findall(".//w:p", W_NS):
        pieces = []
        for node in para.findall(".//w:t", W_NS):
            pieces.append(node.text or "")
        paragraphs.append("".join(pieces))
    return "\n".join(paragraphs)


def option_like(line):
    raw = normalize_spaces(line)
    if not raw:
        return False
    return (
        "(A)" in raw
        or re.search(r"[BCD][\.\)]", raw) is not None
        or re.match(r"^A[\.\)]\s*", raw) is not None
    )


def parse_option_line(line):
    raw = normalize_spaces(line)
    if not raw:
        return {}

    if "(A)" in raw:
        pattern = re.compile(r"\(([ABCD])\)\s*")
    else:
        raw = re.sub(r"([a-zA-Z])([BCD])\.", r"\1 \2.", raw)
        raw = re.sub(r"([a-zA-Z])([BCD])\)", r"\1 \2)", raw)
        if re.search(r"[BCD][\.\)]", raw) and not re.match(r"^A[\.\)]\s*", raw):
            raw = f"A. {raw}"
        pattern = re.compile(r"([ABCD])[\.\)]\s*")

    matches = list(pattern.finditer(raw))
    if not matches:
        return {}

    options = {}
    for index, match in enumerate(matches):
        key = match.group(1)
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(raw)
        value = normalize_spaces(raw[start:end])
        value = re.split(r"\s+\d{1,3}\.\s+", value, maxsplit=1)[0].strip()
        if value:
            options[key] = value
    return options


def docx_source_label(path):
    return path.stem


def pdf_source_label(path):
    return path.stem.replace("  ", " ")


def infer_chapter_from_text(text, fallback="tong-on"):
    match = re.search(r"Unit\s+(\d{1,2})", text, re.I)
    return match.group(1) if match else fallback


def parse_docx_part1_questions(path):
    text = extract_docx_text(path)
    if "Part 2:" in text:
        text = text.split("Part 2:", 1)[0]
    lines = [normalize_spaces(line) for line in text.splitlines()]
    lines = [line for line in lines if line]

    questions = []
    for index in range(len(lines) - 1):
        question_line = lines[index]
        option_line = lines[index + 1]
        if not option_like(option_line):
            continue
        if re.match(r"^(MINISTRY|HCMC|PROGRESS TEST|Part 1|Unit)\b", question_line, re.I):
            continue

        options = parse_option_line(option_line)
        if len(options) < 3:
            continue

        question_text = clean_question(question_line)
        if len(question_text) < 8:
            continue

        questions.append(
            {
                "source": docx_source_label(path),
                "chapter": "tong-on",
                "question": question_text,
                "options": options,
                "answer": "",
                "confidence": 0,
                "answerSource": "missing",
                "explanation": "",
            }
        )
    return questions


def parse_docx_part2_cloze_questions(path):
    text = extract_docx_text(path)
    if "Part 2:" not in text:
        return []

    section = text.split("Part 2:", 1)[1]
    if "Part 3:" in section:
        section = section.split("Part 3:", 1)[0]

    lines = [normalize_spaces(line) for line in section.splitlines()]
    lines = [line for line in lines if line]

    questions = []
    current_passage_label = ""
    passage_lines = []
    blank_numbers = []
    blank_index = 0

    def flush_passage():
        nonlocal current_passage_label, passage_lines, blank_numbers, blank_index
        current_passage_label = ""
        passage_lines = []
        blank_numbers = []
        blank_index = 0

    for line in lines:
        if re.match(r"^Passage\s+\d+", line, re.I):
            flush_passage()
            current_passage_label = line
            continue

        if option_like(line) and blank_numbers:
            options = parse_option_line(line)
            if len(options) >= 3 and blank_index < len(blank_numbers):
                blank_no = blank_numbers[blank_index]
                passage_text = " ".join(passage_lines)
                questions.append(
                    {
                        "source": docx_source_label(path),
                        "chapter": "tong-on",
                        "question": f"[Cloze] {current_passage_label} {passage_text} Chon dap an tot nhat cho cho trong ({blank_no}).",
                        "options": options,
                        "answer": "",
                        "confidence": 0,
                        "answerSource": "missing",
                        "explanation": "",
                    }
                )
                blank_index += 1
            continue

        if current_passage_label:
            passage_lines.append(line)
            if not blank_numbers:
                blank_numbers = re.findall(r"\((\d{1,3})\)", " ".join(passage_lines))

    return questions


def clean_pdf_page_text(text):
    cleaned = str(text or "").replace("\xa0", " ")
    cleaned = re.sub(r"\s+", " ", cleaned)
    cleaned = re.sub(r"Multiple definitions in dictionary.*$", "", cleaned).strip()
    return cleaned


def parse_pdf_page_questions(page_text, source):
    chapter = infer_chapter_from_text(page_text, "tong-on")
    text = clean_pdf_page_text(page_text)
    first_question = re.search(r"\b1\.\s*", text)
    if first_question:
        text = text[first_question.start():]

    pattern = re.compile(
        r"(\d{1,3})\.\s*(.*?)\s*\(A\)\s*(.*?)\s*\(B\)\s*(.*?)\s*\(C\)\s*(.*?)(?:\s*\(D\)\s*(.*?))?(?=\s*\d{1,3}\.\s|$)",
        re.S,
    )

    questions = []
    for match in pattern.finditer(text):
        question_text = clean_question(match.group(2))
        options = {
            "A": normalize_spaces(match.group(3)),
            "B": normalize_spaces(match.group(4)),
            "C": normalize_spaces(match.group(5)),
        }
        if match.group(6):
            options["D"] = normalize_spaces(match.group(6))

        if len(question_text) < 8 or not all(options.values()):
            continue

        questions.append(
            {
                "source": source,
                "chapter": chapter,
                "question": question_text,
                "options": options,
                "answer": "",
                "confidence": 0,
                "answerSource": "missing",
                "explanation": "",
            }
        )
    return questions


def parse_pdf_questions(path):
    reader = PdfReader(str(path))
    questions = []
    for page in reader.pages:
        questions.extend(parse_pdf_page_questions(page.extract_text() or "", pdf_source_label(path)))
    return questions


def build_seed_questions():
    seed = [
        ("9", "I know my phone is ________ here.", {"A": "nowhere", "B": "anywhere", "C": "somewhere"}, "C"),
        ("9", "I can't find my cat ________. I hope she isn't lost.", {"A": "nowhere", "B": "anywhere", "C": "somewhere"}, "B"),
        ("9", "________ called for you but he didn't leave his name.", {"A": "Everyone", "B": "Someone", "C": "No one"}, "B"),
        ("9", "Today, you can visit the huge pyramids that the Incas built, and ________ are still finding objects such as pots for cooking or ________ showing pictures from their past.", {"A": "archaeologists / statues", "B": "archaeologists / paintings", "C": "collectors / paintings"}, "B"),
        ("9", "You don't need to read the instructions because it's so ________.", {"A": "basic", "B": "user-friendly", "C": "useful"}, "B"),
        ("9", "Let me begin by telling ________.", {"A": "about my visit to Italy", "B": "you a bit about the city of Pisa", "C": "a bit about the city of Pisa"}, "B"),
        ("9", "Everyone was playing ________ on their phones because, unlike other video games, you didn't have to spend much money ________ the app and you could take it ________ everywhere.", {"A": "with it / on / with", "B": "in it / on / with", "C": "it / on / with"}, "C"),
        ("11", "We ________ our first video game when we were eleven.", {"A": "used to play", "B": "played", "C": "had played"}, "B"),
        ("11", "My parents ________ me to the park, but I go regularly now.", {"A": "didn't use to take", "B": "used to take", "C": "took"}, "A"),
        ("11", "Mum ________ us she would be late home and not to wait for her for dinner.", {"A": "told", "B": "said", "C": "spoke"}, "A"),
        ("11", "Did David ________ you about his plans for the summer?", {"A": "say", "B": "tell", "C": "talk"}, "B"),
        ("11", "My husband ________ me a funny joke this morning.", {"A": "says", "B": "told", "C": "said"}, "B"),
        ("12", "When it ________ cold, we ________ to stay at home.", {"A": "is / prefer", "B": "is / will prefer", "C": "were / would prefer"}, "A"),
        ("12", "How many people ________ to the party?", {"A": "came", "B": "did / come", "C": "had come"}, "A"),
        ("12", "When I got to the station, the train ________ already.", {"A": "left", "B": "had left", "C": "leaves"}, "B"),
    ]
    return [
        {
            "source": "Co Thu review",
            "chapter": chapter,
            "question": question,
            "options": options,
            "answer": answer,
            "confidence": 1,
            "answerSource": "teacher-review",
            "explanation": "",
        }
        for chapter, question, options, answer in seed
    ]


def strict_json_from_text(text):
    normalized = str(text or "").strip()
    normalized = re.sub(r"^```(?:json)?\s*", "", normalized, flags=re.I)
    normalized = re.sub(r"\s*```$", "", normalized)

    try:
        parsed = json.loads(normalized)
        return json.loads(parsed) if isinstance(parsed, str) else parsed
    except Exception:
        pass

    for start, char in enumerate(normalized):
        if char not in "[{":
            continue
        stack = []
        in_string = False
        escaped = False
        for end in range(start, len(normalized)):
            current = normalized[end]
            if in_string:
                if escaped:
                    escaped = False
                elif current == "\\":
                    escaped = True
                elif current == '"':
                    in_string = False
                continue
            if current == '"':
                in_string = True
            elif current in "[{":
                stack.append(current)
            elif current in "]}":
                opening = stack.pop() if stack else None
                if not opening:
                    break
                if (opening == "{" and current != "}") or (opening == "[" and current != "]"):
                    break
                if not stack:
                    return json.loads(normalized[start : end + 1])
    raise RuntimeError("Khong doc duoc JSON tu Ollama.")


def extract_answer_label(value):
    match = re.search(r"\b([ABCD])\b", str(value or "").upper())
    return match.group(1) if match else ""


def ask_ollama_batch(batch):
    schema = {
        "results": [
            {
                "index": item["index"],
                "answer": "A",
                "confidence": 0.95,
                "explanation": "short",
            }
            for item in batch[:1]
        ]
    }
    user_prompt = (
        "Return JSON only. Schema: "
        + json.dumps(schema, ensure_ascii=False)
        + ". Choose exactly one existing option label for each question. "
        + "Do not include option text in the answer field, only A/B/C/D. "
        + "Questions: "
        + json.dumps(batch, ensure_ascii=False)
    )
    payload = {
        "model": MODEL,
        "stream": False,
        "format": "json",
        "messages": [
            {"role": "system", "content": "You are a strict JSON API for multiple-choice answer selection."},
            {"role": "user", "content": user_prompt},
        ],
        "options": {"temperature": 0.1, "top_p": 0.2},
    }
    request = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=240) as response:
        raw = json.loads(response.read().decode("utf-8"))
    return strict_json_from_text(raw.get("message", {}).get("content", ""))


def resolve_answers(questions):
    unresolved = [
        {
            "index": idx,
            "question": item["question"],
            "options": item["options"],
        }
        for idx, item in enumerate(questions)
        if not item.get("answer")
    ]

    batch_size = 20
    for start in range(0, len(unresolved), batch_size):
        batch = unresolved[start : start + batch_size]
        try:
            parsed = ask_ollama_batch(batch)
        except (urllib.error.URLError, TimeoutError) as error:
            raise RuntimeError(f"Khong goi duoc Ollama batch: {error}") from error

        results = parsed.get("results", []) if isinstance(parsed, dict) else []
        mapped = {item.get("index"): item for item in results}
        for question_meta in batch:
            answer_meta = mapped.get(question_meta["index"], {})
            target = questions[question_meta["index"]]
            label = extract_answer_label(answer_meta.get("answer"))
            if label and label in target["options"]:
                target["answer"] = label
                target["confidence"] = float(answer_meta.get("confidence") or 0.75)
                target["answerSource"] = "ollama-batch"
                target["explanation"] = str(answer_meta.get("explanation") or "")
        print(f"Resolved {min(start + len(batch), len(unresolved))}/{len(unresolved)}")


def dedupe_questions(existing_questions, new_questions):
    seen = {normalize_key(item.get("question")) for item in existing_questions}
    unique = []
    for item in new_questions:
        key = normalize_key(item.get("question"))
        if not key or key in seen:
            continue
        seen.add(key)
        unique.append(item)
    return unique


def collect_new_questions():
    collected = []

    for file_name in DOCX_FILES:
        path = SOURCE_ROOT / file_name
        if path.exists():
            part1 = parse_docx_part1_questions(path)
            part2 = parse_docx_part2_cloze_questions(path)
            print(f"{path.name}: {len(part1)} part1 + {len(part2)} part2 parsed")
            collected.extend(part1)
            collected.extend(part2)

    for pattern in PDF_PATTERNS:
        for path in sorted(SOURCE_ROOT.glob(pattern)):
            parsed = parse_pdf_questions(path)
            print(f"{path.name}: {len(parsed)} parsed")
            collected.extend(parsed)

    collected.extend(build_seed_questions())
    cleaned, dropped = sanitize_questions(collected)
    if dropped:
        print(f"Dropped {len(dropped)} broken newly parsed questions")
    return cleaned


def main():
    payload = read_existing_payload()
    existing_questions = payload.get("questions", [])
    new_questions = collect_new_questions()
    new_questions = dedupe_questions(existing_questions, new_questions)
    print(f"New unique questions: {len(new_questions)}")

    try:
        resolve_answers(new_questions)
    except RuntimeError as error:
        print(f"Warning: {error}")
        print("Skip them moi chua co dap an vi Ollama dang khong san sang.")
    ready_questions = [item for item in new_questions if item.get("answer")]
    print(f"Ready new questions: {len(ready_questions)}")

    payload["questions"] = apply_strict_scope(existing_questions + ready_questions)
    payload["count"] = len(payload["questions"])
    payload["sourceCounts"] = {"imported": payload["count"]}

    OUTPUT_FILE.write_text(
        "window.__QUIZ_DATA__ = " + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";\n",
        encoding="utf-8",
    )
    print(f"Wrote {payload['count']} questions -> {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
