import os
from pathlib import Path
from typing import Optional

import psycopg2
from dotenv import load_dotenv

# Load the repository-level .env file without committing it to version control.
ENV_FILE = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(ENV_FILE)


def connect_to_database() -> Optional[psycopg2.extensions.connection]:
    """Create a PostgreSQL connection using environment-based settings."""
    try:
        connection = psycopg2.connect(
            host=os.getenv("BANK_DB_HOST", "localhost"),
            port=os.getenv("BANK_DB_PORT", "5432"),
            database=os.getenv("BANK_DB_NAME", "BankData"),
            user=os.getenv("BANK_DB_USER", "postgres"),
            password=os.getenv("BANK_DB_PASSWORD", ""),
            connect_timeout=5,
        )
        print("Connected to PostgreSQL database.")
        return connection
    except psycopg2.Error as error:
        print(f"Could not connect to PostgreSQL. Check your .env settings and server: {error}")
        return None


if __name__ == "__main__":
    connection = connect_to_database()
    if connection:
        connection.close()
        print("Connection closed.")
