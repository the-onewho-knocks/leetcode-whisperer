# backend/app/main.py

from fastapi import FastAPI
from app.api.whisper import router as whisper_router
from app.api.health import router as health_router

app = FastAPI(title="LeetCode Whisperer")

app.include_router(health_router)
app.include_router(whisper_router)