import psycopg2
import os


if __name__ == '__main__':
    postgres_user = os.getenv('POSTGRES_USER')
    postgres_password = os.getenv('POSTGRES_PASSWORD')
    postgres_db = os.getenv('POSTGRES_DB')
    host = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT')

    conn = psycopg2.connect(
        dbname=postgres_db,
        user=postgres_user,
        password=postgres_password,
        host=host,
        port=port
    )
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(64) NOT NULL,
                first_name VARCHAR(64) NOT NULL,
                last_name VARCHAR(64) NOT NULL,
                birthdate TIMESTAMP NULL
            );
        """)
    conn.commit()