# backend/app/utils/parser.py

import re


SECTION_PATTERN = {
    "pattern": r"Pattern:\s*(.+)",
    "explanation": r"Simple Explanation:\s*([\s\S]*?)Hint Level 1:",
    "h1": r"Hint Level 1:\s*([\s\S]*?)Hint Level 2:",
    "h2": r"Hint Level 2:\s*([\s\S]*?)Hint Level 3:",
    "h3": r"Hint Level 3:\s*([\s\S]*)",
}


def parse_whisper_response(text: str) -> dict:
    def extract(key: str) -> str:
        match = re.search(SECTION_PATTERN[key], text)
        if not match:
            raise ValueError(f"Missing section: {key}")
        return match.group(1).strip()
    return {
    "pattern": extract("pattern"),
    "simple_explanation": extract("explanation"),
    "hints": {
        "level_1": extract("h1"),
        "level_2": extract("h2"),
        "level_3": extract("h3"),
    },
}