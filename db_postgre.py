import os

import bcrypt
import psycopg



def get_connection():
    return psycopg.connect(
        dbname=os.getenv("POSTGRES_DB", "backend_db"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=os.getenv("POSTGRES_PORT", "5433"),
    )


def initialize_database():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS user_data (
                id SERIAL PRIMARY KEY,
                username VARCHAR(100) UNIQUE NOT NULL,
                user_email VARCHAR(100) UNIQUE NOT NULL,
                user_password VARCHAR(100) NOT NULL
            )
            """
        )


def create_user(username, email, password):
    if isinstance(password, bytes):
        password = password.decode("ascii")

    with get_connection() as connection:
        connection.execute(
            """
            INSERT INTO user_data (username, user_email, user_password)
            VALUES (%s, %s, %s)
            """,
            (username, email, password),
        )


def authenticate_user(username, password):
    with get_connection() as connection:
        user = connection.execute(
            """
            SELECT username, user_password
            FROM user_data
            WHERE username = %s
            """,
            (username,),
        ).fetchone()

    if user is None:
        return False

    stored_password = user[1]

    try:
        if stored_password.startswith(r"\x"):
            hashed_password = bytes.fromhex(stored_password[2:])
        else:
            hashed_password = stored_password.encode("ascii")
    except (ValueError, UnicodeEncodeError):
        return False

    try:
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
    except (ValueError, UnicodeEncodeError):
        return False
