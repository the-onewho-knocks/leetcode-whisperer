# backend/app/patterns/corrector.py

from app.patterns.registry import DSAPattern


def correct_pattern(problem_statement: str, suggested_pattern: str) -> str:
    """
    Applies deterministic rules to correct or downgrade
    an LLM-suggested DSA pattern.

    Returns the final pattern to be used.
    """

    text = problem_statement.lower()
    pattern = suggested_pattern.lower()

    # --- Rule 1: Palindrome problems ---
    if "palindrome" in text:
        return DSAPattern.TWO_POINTERS.value

    # --- Rule 2: Simple symmetry or reverse traversal ---
    if any(word in text for word in ["reverse", "mirror", "symmetric"]):
        return DSAPattern.TWO_POINTERS.value

    # --- Rule 3: Explicit sliding window signals ---
    if any(word in text for word in ["substring", "subarray", "window"]):
        return DSAPattern.SLIDING_WINDOW.value

    # --- Rule 4: Recursion keywords ---
    if any(word in text for word in ["tree", "dfs", "recursion"]):
        return DSAPattern.RECURSION.value

    # --- Default: trust the model ---
    return pattern