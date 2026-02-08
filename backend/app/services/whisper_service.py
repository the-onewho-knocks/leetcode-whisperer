from app.services.gemini_service import GeminiService
from app.services.prompt_builder import build_whisper_prompt
from app.utils.guards import enforce_no_code_policy
from app.utils.parser import parse_whisper_response
from app.patterns.registry import DSAPattern


class WhisperService:
    def __init__(self) -> None:
        self.gemini = GeminiService()

    def whisper(self, problem_statement: str, user_code: str | None = None) -> dict:
        prompt = build_whisper_prompt(problem_statement, user_code)
        raw = self.gemini.generate(prompt)
        safe = enforce_no_code_policy(raw)

        parsed = parse_whisper_response(safe)

        # Normalize pattern
        parsed["pattern"] = parsed["pattern"].strip().lower()

        return parsed