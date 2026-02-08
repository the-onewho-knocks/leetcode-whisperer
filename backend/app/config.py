from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GEMINI_API_KEY: str
    GEMINI_MODEL: str = "models/gemini-2.5-flash"

    class Config:
        env_file = ".env"

settings = Settings()