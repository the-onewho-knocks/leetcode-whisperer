# backend/app/services/whisper_service.py

from app.services.gemini_service import GeminiService
from app.services.prompt_builder import build_whisper_prompt
from app.utils.guards import enforce_no_code_policy


class WhisperService:
    """
    Orchestrates the LeetCode Whisperer flow:
    prompt -> Gemini -> guarded response
    """

    def __init__(self) -> None:
        self.gemini = GeminiService()

    def whisper(
        self,
        problem_statement: str,
        user_code: str | None = None,
    ) -> str:
        """
        Generates guided hints for a LeetCode problem.
        Returns raw, guarded text (still human-readable).
        """

        prompt = build_whisper_prompt(
            problem_statement=problem_statement,
            user_code=user_code,
        )

        raw_response = self.gemini.generate(prompt)

        # Enforce safety: no code, no full solutions
        safe_response = enforce_no_code_policy(raw_response)

        return safe_response