import os
import psycopg2

def db_dsn() -> str:
    host = os.getenv("POSTGRES_HOST", "localhost")
    port = int(os.getenv("POSTGRES_PORT", "5432"))
    db = os.getenv("POSTGRES_DB", "expenses")
    user = os.getenv("POSTGRES_USER", "expenses_user")
    pwd = os.getenv("POSTGRES_PASSWORD", "change_me")
    return f"host={host} port={port} dbname={db} user={user} password={pwd}"

def check_db() -> bool:
    try:
        with psycopg2.connect(db_dsn(), connect_timeout=2) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1;")
                cur.fetchone()
        return True
    except Exception:
        return False
