# backend/app/schemas/whisper.py

from pydantic import BaseModel, Field
from typing import Optional


class WhisperRequest(BaseModel):
    problem_statement: str = Field(..., min_length=10)
    user_code: Optional[str] = None


class HintLevels(BaseModel):
    level_1: str
    level_2: str
    level_3: str

class WhisperResponse(BaseModel):
    pattern: str
    simple_explanation: str
    hints: HintLevels