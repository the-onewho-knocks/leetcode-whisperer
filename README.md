# LeetCode Whisperer

LeetCode Whisperer is an AI-powered learning assistant designed to help users solve Data Structures and Algorithms problems without giving away full solutions. It focuses on guiding thinking through patterns, simplified explanations, and progressively revealed hints.

The goal is to help users think like problem solvers, not copy answers.

---

## Features

- Identifies the core DSA pattern behind a problem  
- Explains the problem in simple, beginner-friendly language  
- Provides multi-level hints that unlock progressively  
- Strictly avoids full solutions or code leakage  
- Clean, minimal, distraction-free UI  
- Fully deployed backend and frontend  

---

## How It Works

1. The user pastes a LeetCode problem statement
2. The backend processes the input using an LLM (Gemini API)
3. The system:
   - Detects the underlying DSA pattern
   - Generates a simplified explanation
   - Produces structured hints (Level 1 → Level 3)
4. The frontend displays hints interactively without exposing solutions

---

## Tech Stack

### Backend
- FastAPI
- Python
- Google Gemini API
- Pydantic
- SQLite
- Uvicorn

### Frontend
- HTML
- CSS
- Vanilla JavaScript

### Deployment
- Backend: Render
- Frontend: Netlify

---

## Project Architecture
```text
backend/
├── app/
│ ├── main.py
│ ├── config.py
│ ├── deps.py
│ ├── api/
│ │ ├── whisper.py
│ │ └── health.py
│ ├── schemas/
│ │ └── whisper.py
│ ├── services/
│ │ ├── gemini_service.py
│ │ ├── whisper_service.py
│ │ └── prompt_builder.py
│ ├── patterns/
│ │ └── registry.py
│ ├── utils/
│ │ ├── sanitizer.py
│ │ └── guards.py
│ └── storage/
│ ├── database.py
│ └── repository.py
├── requirements.txt
└── tests/

frontend/
├── index.html
├── style.css
└── app.js
```


---

## API Endpoint

### POST `/whisper/`

#### Request Body
```json
{
  "problem_statement": "string",
  "user_code": "string"
}

{
  "pattern": "string",
  "explanation": "string",
  "hints": {
    "level_1": "string",
    "level_2": "string",
    "level_3": "string"
  }
}

```

## Local Setup
### Backend Setup
for this project the backend is hosted on render
```code
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Backend runs at:
```text
http://127.0.0.1:8000
```

### Frontend Setup
for this project the frontend is hosted on netlify
```
Open frontend/index.html directly in the browser
or use a simple live server extension.
```

## Learning Philosophy

- No direct solutions

- Pattern-first problem solving

- Progressive hint system

- Interview-oriented thinking

- Ethical and responsible AI usage

## Author
**Hardik Borse** | [LinkedIn](https://www.linkedin.com/in/hardik-borse-aa7729324/) | [Email](mailto:borsehardik@gmail.com)

## License
This project is licensed under the **Apache License 2.0**.
