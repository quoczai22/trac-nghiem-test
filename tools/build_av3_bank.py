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
    "AV3 scoped synthetic",
}


EXCLUDED_SOURCES = {
    "Co Thu review",
    "AV3 review",
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
    if source in EXCLUDED_SOURCES:
        return False
    if source in ALWAYS_KEEP_SOURCES:
        return True

    blob = question_blob(item)
    return any(re.search(pattern, blob, re.I) for pattern in EXTERNAL_SCOPE_PATTERNS)


def is_future_plans_noise(item):
    blob = question_blob(item).lower()
    question = str(item.get("question") or "").strip().lower()
    chapter = infer_scope_chapter(item)

    # Keep "going to" when it is part of Unit 11 reported speech content.
    if chapter == "11" and (
        question.startswith(("‘", "'", '"'))
        or "reported speech" in blob
        or "said that" in blob
        or "told me that" in blob
    ):
        return False

    future_markers = [
        "going to",
        "will buy",
        "will retire",
        "are leaving",
        "will leave",
        "going to leave",
        "going to retire",
        "going to have a small party",
    ]
    return any(marker in blob for marker in future_markers)


def is_connector_noise(item):
    blob = question_blob(item).lower()
    connector_markers = ["nevertheless", "although", "despite", "though"]
    return all(marker in blob for marker in connector_markers)


def is_external_reading_noise(item):
    source = str(item.get("source") or "").strip()
    question = str(item.get("question") or "").strip()
    if source in EXCLUDED_SOURCES:
        return True
    if question.startswith("[Cloze]") or question.startswith("[Reading"):
        return True
    return False


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
        if is_external_reading_noise(normalized):
            continue
        if is_future_plans_noise(normalized):
            continue
        if is_connector_noise(normalized):
            continue
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


def make_manual_question(source, chapter, question, options, answer, explanation=""):
    return {
        "source": source,
        "chapter": chapter,
        "question": question,
        "options": options,
        "answer": answer,
        "confidence": 1,
        "answerSource": "scoped-generator",
        "explanation": explanation,
    }


def build_scoped_generated_questions():
    source = "AV3 scoped synthetic"
    items = []

    unit7 = [
        ("7", "I have worked here ________ 2022.", {"A": "for", "B": "since", "C": "from", "D": "during"}, "B"),
        ("7", "We have lived in this city ________ three years.", {"A": "since", "B": "from", "C": "for", "D": "at"}, "C"),
        ("7", "She ________ her first job in 2021.", {"A": "has found", "B": "found", "C": "finds", "D": "had found"}, "B"),
        ("7", "Have you ever ________ abroad?", {"A": "work", "B": "worked", "C": "working", "D": "works"}, "B"),
        ("7", "I haven't finished my report ________.", {"A": "already", "B": "yet", "C": "ever", "D": "just"}, "B"),
        ("7", "He has ________ received your email.", {"A": "yet", "B": "ever", "C": "just", "D": "since"}, "C"),
        ("7", "My office is ________ the second floor.", {"A": "on", "B": "in", "C": "at", "D": "between"}, "A"),
        ("7", "The bank is ________ the supermarket and the cafe.", {"A": "through", "B": "between", "C": "along", "D": "up"}, "B"),
        ("7", "Walk ________ the bridge and turn left.", {"A": "across", "B": "between", "C": "inside", "D": "opposite"}, "A"),
        ("7", "The station is ________ the museum.", {"A": "next to", "B": "through", "C": "down", "D": "inside"}, "A"),
        ("7", "A person who works with you is your ________.", {"A": "applicant", "B": "colleague", "C": "customer", "D": "guard"}, "B"),
        ("7", "A letter saying positive things about your work is a ________.", {"A": "reference", "B": "promotion", "C": "salary", "D": "contact"}, "A"),
        ("7", "A person who has applied for a job is an ________.", {"A": "assistant", "B": "applicant", "C": "employer", "D": "actor"}, "B"),
        ("7", "If a room has a lot of space, it is ________.", {"A": "modern", "B": "positive", "C": "spacious", "D": "manual"}, "C"),
        ("7", "A person with a lot of training is highly-________.", {"A": "qualified", "B": "friendly", "C": "natural", "D": "careful"}, "A"),
        ("7", "Food grown without chemicals is called ________ food.", {"A": "organic", "B": "portable", "C": "electronic", "D": "domestic"}, "A"),
        ("7", "A market ________ is a place for selling things outside.", {"A": "screen", "B": "stall", "C": "route", "D": "record"}, "B"),
        ("7", "If the positives are more important than the negatives, they ________ them.", {"A": "produce", "B": "outweigh", "C": "retire", "D": "replace"}, "B"),
        ("7", "A job with many different activities has a lot of ________.", {"A": "variety", "B": "reference", "C": "risk", "D": "loan"}, "A"),
        ("7", "To bring together means to ________ everyone in the same place.", {"A": "protect", "B": "join", "C": "move", "D": "invite"}, "B"),
        ("7", "How long ________ you known your best friend?", {"A": "did", "B": "have", "C": "are", "D": "had"}, "B"),
        ("7", "They ________ already, so we can start the meeting.", {"A": "arrive", "B": "arrived", "C": "have arrived", "D": "had arrived"}, "C"),
        ("7", "I ________ to university when I was nineteen.", {"A": "have gone", "B": "went", "C": "go", "D": "had gone"}, "B"),
        ("7", "We have been friends ________ we were children.", {"A": "for", "B": "since", "C": "during", "D": "while"}, "B"),
        ("7", "The restaurant is ________ the left, opposite the park.", {"A": "on", "B": "in", "C": "at", "D": "under"}, "A"),
        ("7", "Go ________ the stairs carefully; the meeting room is upstairs.", {"A": "down", "B": "into", "C": "up", "D": "through"}, "C"),
        ("7", "The train goes ________ the tunnel.", {"A": "through", "B": "between", "C": "over", "D": "next to"}, "A"),
        ("7", "I haven't seen that film ________.", {"A": "just", "B": "yet", "C": "since", "D": "for"}, "B"),
    ]

    unit8 = [
        ("8", "If it rains, we ________ at home.", {"A": "stayed", "B": "stay", "C": "will stay", "D": "have stayed"}, "C"),
        ("8", "If you heat water to 100 degrees, it ________.", {"A": "boiled", "B": "boils", "C": "will boil", "D": "is boiling"}, "B"),
        ("8", "If I hear any news, I ________ you a message.", {"A": "sent", "B": "send", "C": "will send", "D": "would send"}, "C"),
        ("8", "If the weather is good, we ________ the forest on Saturday.", {"A": "visit", "B": "visited", "C": "will visit", "D": "would visit"}, "C"),
        ("8", "The woman ________ works in that lab is my aunt.", {"A": "where", "B": "who", "C": "when", "D": "whose"}, "B"),
        ("8", "This is the phone ________ I bought yesterday.", {"A": "which", "B": "who", "C": "where", "D": "when"}, "A"),
        ("8", "That is the village ________ my grandparents were born.", {"A": "which", "B": "who", "C": "where", "D": "what"}, "C"),
        ("8", "A language disappears when nobody ________ it anymore.", {"A": "speaks", "B": "spoke", "C": "will speak", "D": "has spoken"}, "A"),
        ("8", "Awareness means knowledge or ________ of a problem.", {"A": "distance", "B": "understanding", "C": "payment", "D": "direction"}, "B"),
        ("8", "If a language dies out, it slowly stops being ________.", {"A": "recorded", "B": "sold", "C": "used", "D": "borrowed"}, "C"),
        ("8", "Humans cannot survive without clean ________.", {"A": "screens", "B": "water", "C": "roads", "D": "bridges"}, "B"),
        ("8", "A shift is a ________ in the way something happens.", {"A": "change", "B": "result", "C": "promise", "D": "flight"}, "A"),
        ("8", "If you neglect your homework, you do not give it enough ________.", {"A": "attention", "B": "noise", "C": "space", "D": "cash"}, "A"),
        ("8", "The team used technology kits to ________ disappearing languages.", {"A": "repair", "B": "record", "C": "paint", "D": "throw"}, "B"),
        ("8", "Older people in the village still speak ________.", {"A": "organic", "B": "Apatani", "C": "Greek", "D": "Italian"}, "B"),
        ("8", "A laptop is a computer ________ you can carry with you.", {"A": "where", "B": "who", "C": "which", "D": "when"}, "C"),
        ("8", "If my dog hears a noise outside, he ________.", {"A": "barked", "B": "barks", "C": "will barked", "D": "would bark"}, "B"),
        ("8", "If they don't save those recordings, the language ________ forever.", {"A": "disappears", "B": "disappeared", "C": "will disappear", "D": "has disappeared"}, "C"),
        ("8", "The machine ________ cooks dinner for us would be very useful.", {"A": "who", "B": "where", "C": "that", "D": "when"}, "C"),
        ("8", "People use sunglasses to protect their eyes from the ________.", {"A": "sun", "B": "rain", "C": "river", "D": "engine"}, "A"),
        ("8", "You use a torch to see in the ________.", {"A": "market", "B": "dark", "C": "afternoon", "D": "airport"}, "B"),
        ("8", "If the battery is flat, the device ________ work.", {"A": "doesn't", "B": "won't", "C": "didn't", "D": "hasn't"}, "A"),
        ("8", "A reception is the place ________ visitors first arrive in a building.", {"A": "who", "B": "which", "C": "where", "D": "what"}, "C"),
        ("8", "The children are learning English, ________ is very useful for technology jobs.", {"A": "who", "B": "which", "C": "where", "D": "when"}, "B"),
        ("8", "If nobody records the last speaker, the language will ________ out.", {"A": "die", "B": "set", "C": "bring", "D": "grow"}, "A"),
        ("8", "This is the app ________ helps me learn vocabulary.", {"A": "where", "B": "who", "C": "that", "D": "when"}, "C"),
        ("8", "If I finish early, I ________ you after class.", {"A": "called", "B": "call", "C": "will call", "D": "would call"}, "C"),
    ]

    unit9 = [
        ("9", "When we arrived at the station, the train ________.", {"A": "left", "B": "has left", "C": "had left", "D": "leaves"}, "C"),
        ("9", "She was tired because she ________ all day.", {"A": "worked", "B": "had worked", "C": "works", "D": "has worked"}, "B"),
        ("9", "As soon as the sun had come out, the children ________ outside.", {"A": "run", "B": "ran", "C": "have run", "D": "were running"}, "B"),
        ("9", "Who ________ this message?", {"A": "did write", "B": "wrote", "C": "has wrote", "D": "writing"}, "B"),
        ("9", "How many people ________ to the party?", {"A": "came", "B": "did come", "C": "had come", "D": "comes"}, "A"),
        ("9", "Who ________ here?", {"A": "does live", "B": "lives", "C": "did lived", "D": "has living"}, "B"),
        ("9", "A trader is a person who buys and ________ things.", {"A": "sells", "B": "moves", "C": "keeps", "D": "hides"}, "A"),
        ("9", "A gondolier takes tourists around Venice in a ________.", {"A": "truck", "B": "gondola", "C": "submarine", "D": "tram"}, "B"),
        ("9", "Property in Venice is particularly ________.", {"A": "cheap", "B": "modern", "C": "expensive", "D": "quiet"}, "C"),
        ("9", "Many young people move away to more ________ cities.", {"A": "ancient", "B": "crowded", "C": "modern", "D": "narrow"}, "C"),
        ("9", "Good health is a ________ in life.", {"A": "gift", "B": "mission", "C": "loan", "D": "grid"}, "A"),
        ("9", "A challenge is something difficult you need to ________.", {"A": "face", "B": "launch", "C": "release", "D": "boil"}, "A"),
        ("9", "Venice has a high quality of life, but property is very ________.", {"A": "friendly", "B": "expensive", "C": "portable", "D": "traditional"}, "B"),
        ("9", "The city is beautiful, but crowds can be a ________.", {"A": "disadvantage", "B": "gift", "C": "guide", "D": "gondola"}, "A"),
        ("9", "Before we got home, we ________ dinner in a small restaurant.", {"A": "had had", "B": "have had", "C": "had", "D": "have"}, "A"),
        ("9", "Who ________ your glasses?", {"A": "broke", "B": "did broke", "C": "had broken", "D": "breaks"}, "A"),
        ("9", "What ________ the delay?", {"A": "did cause", "B": "cause", "C": "caused", "D": "had causing"}, "C"),
        ("9", "The museum was huge, but the biggest ________ was the long queue.", {"A": "increase", "B": "challenge", "C": "trader", "D": "gift"}, "B"),
        ("9", "By the time we saw the sunset, the musicians ________ already.", {"A": "left", "B": "had left", "C": "leave", "D": "have left"}, "B"),
        ("9", "A crowd means many people in the same ________.", {"A": "place", "B": "record", "C": "century", "D": "battery"}, "A"),
        ("9", "Who ________ me earlier today?", {"A": "called", "B": "did called", "C": "had call", "D": "calls"}, "A"),
        ("9", "After they ________ the tickets, they went into the theatre.", {"A": "buy", "B": "bought", "C": "had bought", "D": "have bought"}, "C"),
        ("9", "The city has many advantages, but housing prices have also ________.", {"A": "increased", "B": "launched", "C": "released", "D": "survived"}, "A"),
    ]

    unit10 = [
        ("10", "Millions of smartphones ________ every year.", {"A": "sell", "B": "are sold", "C": "sold", "D": "are selling"}, "B"),
        ("10", "The first Apple laptops ________ in 1999.", {"A": "produced", "B": "were produced", "C": "are produced", "D": "have produced"}, "B"),
        ("10", "Facebook ________ by Mark Zuckerberg.", {"A": "created", "B": "is created", "C": "was created", "D": "has creating"}, "C"),
        ("10", "Public transport ________ a lot in my country.", {"A": "uses", "B": "is used", "C": "used", "D": "using"}, "B"),
        ("10", "The logo ________ all over the world.", {"A": "recognizes", "B": "is recognized", "C": "recognized", "D": "has recognize"}, "B"),
        ("10", "I used to ________ to concerts every month.", {"A": "go", "B": "went", "C": "gone", "D": "going"}, "A"),
        ("10", "She didn't use to ________ coffee, but now she drinks it every day.", {"A": "liked", "B": "like", "C": "likes", "D": "liking"}, "B"),
        ("10", "Did you use to ________ a Walkman?", {"A": "owned", "B": "own", "C": "owns", "D": "owning"}, "B"),
        ("10", "The land around the wind farm is very ________.", {"A": "flat", "B": "huge", "C": "illegal", "D": "organic"}, "A"),
        ("10", "The farmer finally paid off the ________ on his machine.", {"A": "record", "B": "loan", "C": "screen", "D": "bridge"}, "B"),
        ("10", "A wind turbine must withstand very strong ________.", {"A": "sun", "B": "wind", "C": "rainbows", "D": "crowds"}, "B"),
        ("10", "Electricity from the turbine goes into the local ________.", {"A": "grid", "B": "park", "C": "market", "D": "tunnel"}, "A"),
        ("10", "A ton is a unit of ________.", {"A": "distance", "B": "weight", "C": "temperature", "D": "time"}, "B"),
        ("10", "Farmers grow ________ on the land.", {"A": "crops", "B": "tickets", "C": "bridges", "D": "signals"}, "A"),
        ("10", "A lot of money ________ on famous logos.", {"A": "spends", "B": "is spent", "C": "spent", "D": "spending"}, "B"),
        ("10", "New articles ________ for the website every week.", {"A": "write", "B": "wrote", "C": "are written", "D": "have write"}, "C"),
        ("10", "The old logo ________ back after many customers complained.", {"A": "changed", "B": "was changed", "C": "is changing", "D": "changes"}, "B"),
        ("10", "We used to ________ CDs, but now we stream music online.", {"A": "buy", "B": "bought", "C": "buys", "D": "buying"}, "A"),
        ("10", "He didn't use to ________ glasses when he was younger.", {"A": "wore", "B": "wear", "C": "wears", "D": "wearing"}, "B"),
        ("10", "The second turbine ________ to save more money for the school.", {"A": "built", "B": "was built", "C": "is building", "D": "has build"}, "B"),
        ("10", "YouTube ________ by over a billion people every month.", {"A": "use", "B": "is used", "C": "used", "D": "uses"}, "B"),
        ("10", "The first video ________ by Jawed Karim in 2005.", {"A": "made", "B": "was made", "C": "is made", "D": "making"}, "B"),
        ("10", "People used to ________ photos on film, not on phones.", {"A": "take", "B": "took", "C": "taken", "D": "takes"}, "A"),
        ("10", "The wind turbine can withstand 130 miles per ________.", {"A": "week", "B": "hour", "C": "minute", "D": "month"}, "B"),
        ("10", "A product is more attractive if its logo ________ easily.", {"A": "recognize", "B": "is recognized", "C": "recognized", "D": "recognizes"}, "B"),
    ]

    unit11 = [
        ("11", "She said that she ________ the film.", {"A": "loved", "B": "love", "C": "has loved", "D": "is loving"}, "A"),
        ("11", "He told me that he ________ help me later.", {"A": "will", "B": "would", "C": "can", "D": "has"}, "B"),
        ("11", "They said that they ________ seen anything like it before.", {"A": "never have", "B": "had never", "C": "never", "D": "were"}, "B"),
        ("11", "Julia said that she ________ there at noon.", {"A": "was going to be", "B": "is going to be", "C": "will be", "D": "goes"}, "A"),
        ("11", "If you use tell in reported speech, you need an ________.", {"A": "object", "B": "adjective", "C": "article", "D": "option"}, "A"),
        ("11", "Voyager 1 is a ________.", {"A": "market stall", "B": "spacecraft", "C": "gondola", "D": "loan"}, "B"),
        ("11", "The solar system is the collection of planets around one ________.", {"A": "star", "B": "sun", "C": "forest", "D": "river"}, "B"),
        ("11", "A mission is a particular job or ________.", {"A": "task", "B": "ticket", "C": "machine", "D": "cable"}, "A"),
        ("11", "Classical and jazz are kinds of ________.", {"A": "planets", "B": "music", "C": "engines", "D": "storms"}, "B"),
        ("11", "Voyager carries a message for other life forms in the ________.", {"A": "universe", "B": "tunnel", "C": "market", "D": "bridge"}, "A"),
        ("11", "She said, 'I am waiting for the bus.' -> She said that she ________ for the bus.", {"A": "waited", "B": "was waiting", "C": "has waited", "D": "waits"}, "B"),
        ("11", "He said, 'We missed our flight.' -> He said that they ________ their flight.", {"A": "miss", "B": "had missed", "C": "have missed", "D": "missed"}, "B"),
        ("11", "They said, 'We'll help you.' -> They said that they ________ help me.", {"A": "would", "B": "will", "C": "can", "D": "should"}, "A"),
        ("11", "The Golden Record was put on Voyager to represent the ________.", {"A": "desert", "B": "Earth", "C": "mountain", "D": "stadium"}, "B"),
        ("11", "The team chose photos, sounds and music for the Golden ________.", {"A": "grid", "B": "record", "C": "market", "D": "battery"}, "B"),
        ("11", "After said, you can use the word that, but you do not ________ to.", {"A": "must", "B": "have", "C": "want", "D": "say"}, "B"),
        ("11", "He told me that he ________ leaving that afternoon.", {"A": "is", "B": "was", "C": "has", "D": "would"}, "B"),
        ("11", "A spacecraft is launched when it is sent on a ________.", {"A": "journey", "B": "lesson", "C": "discount", "D": "salary"}, "A"),
        ("11", "The sound of a human heart was included on the Golden ________.", {"A": "record", "B": "tower", "C": "stall", "D": "guide"}, "A"),
        ("11", "He said, 'I bought my first game in 2010.' -> He said that he ________ his first game in 2010.", {"A": "had bought", "B": "has bought", "C": "buys", "D": "buying"}, "A"),
        ("11", "She said, 'I want a new Xbox.' -> She said that she ________ a new Xbox.", {"A": "wants", "B": "wanted", "C": "had wanted to", "D": "would want"}, "B"),
        ("11", "Voyager 1 first photographed Jupiter and ________.", {"A": "Venice", "B": "Saturn", "C": "Mars only", "D": "the Moon"}, "B"),
        ("11", "Reported speech often changes pronouns, time words and ________.", {"A": "possessives", "B": "crops", "C": "weights", "D": "bridges"}, "A"),
        ("11", "He said, 'We live here.' -> He said that they lived ________.", {"A": "here", "B": "there", "C": "everywhere", "D": "outside"}, "B"),
    ]

    unit12 = [
        ("12", "If I had more time, I ________ travel more.", {"A": "will", "B": "would", "C": "have", "D": "am"}, "B"),
        ("12", "If it ________ less, the land wouldn't be so dry.", {"A": "rained", "B": "rains", "C": "has rained", "D": "was raining"}, "A"),
        ("12", "What would you do if you ________ a tornado?", {"A": "see", "B": "saw", "C": "have seen", "D": "will see"}, "B"),
        ("12", "If the river flooded, we ________ leave our homes.", {"A": "had to", "B": "would have to", "C": "will have", "D": "must"}, "B"),
        ("12", "I can't find my keys ________.", {"A": "everywhere", "B": "anywhere", "C": "someone", "D": "something"}, "B"),
        ("12", "________ called for you, but he didn't leave his name.", {"A": "Nobody", "B": "Someone", "C": "Nowhere", "D": "Nothing"}, "B"),
        ("12", "There is ________ in my bag. It's empty.", {"A": "anything", "B": "nothing", "C": "someone", "D": "everywhere"}, "B"),
        ("12", "Would you like ________ to eat?", {"A": "anything", "B": "something", "C": "nothing", "D": "everywhere"}, "B"),
        ("12", "Everybody means the same as ________.", {"A": "nobody", "B": "someone", "C": "everyone", "D": "anything"}, "C"),
        ("12", "If I could meet someone famous, I ________ ask lots of questions.", {"A": "will", "B": "would", "C": "am", "D": "did"}, "B"),
        ("12", "A poacher is someone who catches animals ________ for money.", {"A": "legally", "B": "illegally", "C": "carefully", "D": "slowly"}, "B"),
        ("12", "A sponsor is a person or group that gives ________.", {"A": "weather", "B": "money", "C": "animals", "D": "powder"}, "B"),
        ("12", "To release an animal means to put it back into the ________.", {"A": "shop", "B": "wild", "C": "boat", "D": "hotel"}, "B"),
        ("12", "A victim is a person or animal affected by a bad ________.", {"A": "situation", "B": "record", "C": "journey", "D": "screen"}, "A"),
        ("12", "If animal parts are ground into powder, they are made into very small ________.", {"A": "bridges", "B": "pieces", "C": "forests", "D": "markets"}, "B"),
        ("12", "An endangered animal is in ________.", {"A": "fashion", "B": "danger", "C": "charge", "D": "control"}, "B"),
        ("12", "The Wilderness Protection Mobile Unit helps stop illegal animal ________.", {"A": "recording", "B": "poaching", "C": "farming", "D": "painting"}, "B"),
        ("12", "If we had a bigger house, we ________ keep more rescued animals.", {"A": "can", "B": "would", "C": "will", "D": "are"}, "B"),
        ("12", "I saw ________ near the rescue centre, but I don't know who it was.", {"A": "somebody", "B": "everything", "C": "nowhere", "D": "nothing"}, "A"),
        ("12", "There was ________ else in the room, so I left.", {"A": "anyone", "B": "no one", "C": "someone", "D": "everyone"}, "B"),
        ("12", "If the weather were warmer, we ________ outside.", {"A": "study", "B": "would study", "C": "will study", "D": "studied"}, "B"),
        ("12", "The rescue centre gives special care to rescued ________.", {"A": "animals", "B": "engines", "C": "lessons", "D": "bridges"}, "A"),
        ("12", "If nobody helped endangered animals, many species ________ disappear.", {"A": "must", "B": "would", "C": "can", "D": "did"}, "B"),
        ("12", "You can go ________ quieter if this place is too noisy.", {"A": "nowhere", "B": "somewhere", "C": "everyone", "D": "nothing"}, "B"),
        ("12", "I did ________ wrong, so I wasn't worried.", {"A": "anything", "B": "something", "C": "nothing", "D": "nowhere"}, "C"),
    ]

    for chapter, question, options, answer in unit7 + unit8 + unit9 + unit10 + unit11 + unit12:
        items.append(make_manual_question(source, chapter, question, options, answer))

    return items


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

    collected.extend(build_scoped_generated_questions())
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
