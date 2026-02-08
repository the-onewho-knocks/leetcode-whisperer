# backend/app/utils/guards.py

import re


CODE_BLOCK_PATTERN = re.compile(r"```")
INLINE_CODE_PATTERN = re.compile(r"`.+?`")


def enforce_no_code_policy(text: str) -> str:
    """
    Blocks responses that contain code blocks or inline code.
    This is a safety net in case the model disobeys instructions.
    """

    if CODE_BLOCK_PATTERN.search(text):
        raise ValueError("Policy violation: code blocks detected")

    if INLINE_CODE_PATTERN.search(text):
        raise ValueError("Policy violation: inline code detected")

    return text