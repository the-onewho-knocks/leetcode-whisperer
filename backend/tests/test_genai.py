from google import genai
from app.config import settings  # or adjust import if needed

client = genai.Client(
    api_key=settings.GEMINI_API_KEY,
    http_options={"api_version": "v1alpha"},
)

models = client.models.list()

print("MODELS AVAILABLE TO THIS KEY:")
for m in models:
    print(m.name)