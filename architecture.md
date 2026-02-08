backend/
├── app/
│   ├── main.py                  # FastAPI entry point
│   ├── config.py                # Environment variables, Gemini key
│   ├── deps.py                  # Common dependencies (DB, settings)
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── whisper.py           # /whisper endpoint (core logic)
│   │   └── health.py            # /health check
│   │
│   ├── schemas/
│   │   ├── whisper.py           # Request/Response models
│   │   └── history.py           # Solved problem schema
│   │
│   ├── services/
│   │   ├── gemini_service.py    # Gemini API interaction (STRICT)
│   │   ├── whisper_service.py   # Pattern + hint orchestration
│   │   └── prompt_builder.py    # Prompt templates (brain of system)
│   │
│   ├── patterns/
│   │   ├── registry.py          # Canonical DSA pattern list
│   │   └── chess_map.py         # Pattern → chess analogy
│   │
│   ├── storage/
│   │   ├── database.py          # SQLite connection
│   │   └── repository.py        # Save/retrieve attempts
│   │
│   └── utils/
│       ├── sanitizer.py         # Prevent code leakage
│       └── guards.py            # “No full solution” enforcement
│
├── tests/
│   └── test_whisper.py
│
├── requirements.txt
└── README.md