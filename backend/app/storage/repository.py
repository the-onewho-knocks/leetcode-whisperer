from app.storage.database import get_connection


def save_attempt(problem: str, pattern: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            problem TEXT,
            pattern TEXT
        )
        """
    )

    cur.execute(
        "INSERT INTO attempts (problem, pattern) VALUES (?, ?)",
        (problem, pattern),
    )

    conn.commit()
    conn.close()