# backend/app/services/prompt_builder.py

from app.patterns.registry import all_patterns
from app.patterns.chess_map import get_chess_analogy
from app.patterns.registry import DSAPattern


def build_whisper_prompt(
    problem_statement: str,
    user_code: str | None = None,
) -> str:
    """
    Builds a strict prompt for Gemini that enforces:
    - pattern identification
    - chess analogy explanation
    - progressive hints
    - no code / no full solution
    """

    allowed_patterns = ", ".join(all_patterns())

    base_instructions = f"""
You are LeetCode Whisperer.

RULES (ABSOLUTE):
- Do NOT provide full solutions.
- Do NOT write code.
- Do NOT give step-by-step implementations.
- You MUST choose exactly ONE pattern from this list:
  [{allowed_patterns}]
- If unsure, choose the closest valid pattern.

OUTPUT FORMAT (FOLLOW STRICTLY):

Pattern:
<pattern_name>

Chess Analogy:
<chess analogy for the chosen pattern>

Hint Level 1:
<conceptual nudge>

Hint Level 2:
<structural insight>

Hint Level 3:
<near-solution idea, still no code>

Stop after Hint Level 3.
"""

    problem_block = f"""
LeetCode Problem:
{problem_statement}
"""

    code_block = ""
    if user_code:
        code_block = f"""
User's Current Attempt (for context only, do not debug line-by-line):
{user_code}
"""

    return (
        base_instructions.strip()
        + "\n\n"
        + problem_block.strip()
        + "\n\n"
        + code_block.strip()
    )


def chess_context_for_pattern(pattern: DSAPattern) -> str:
    """
    Returns chess analogy text for a given pattern.
    Useful for validation or UI display later.
    """
    return get_chess_analogy(pattern)