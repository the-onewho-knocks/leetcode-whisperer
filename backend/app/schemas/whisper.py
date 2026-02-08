# backend/app/schemas/whisper.py

from pydantic import BaseModel, Field
from typing import Optional


class WhisperRequest(BaseModel):
    problem_statement: str = Field(..., min_length=10)
    user_code: Optional[str] = None


class WhisperResponse(BaseModel):
    hints: str