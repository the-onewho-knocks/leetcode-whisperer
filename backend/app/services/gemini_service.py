# backend/app/services/gemini_service.py

from google import genai
from app.config import settings


class GeminiService:
    """
    Thin wrapper around Gemini API.
    ONLY sends prompts and returns raw text.
    """

    def __init__(self) -> None:
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )
        self.model = settings.GEMINI_MODEL

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )

        if response.text:
            return response.text.strip()

        raise RuntimeError("Gemini returned an empty response")