# backend/app/utils/guards.py

import re

# Block fenced code blocks ONLY (```code```)
CODE_BLOCK_PATTERN = re.compile(r"```[\s\S]*?```", re.MULTILINE)


def enforce_no_code_policy(text: str) -> str:
    """
    Allows inline backticks for emphasis.
    Blocks fenced code blocks to prevent full solutions.
    """

    if CODE_BLOCK_PATTERN.search(text):
        raise ValueError("Policy violation: code blocks detected")

    return text