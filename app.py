from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

# Get database connection information from environment variables
db_host = os.getenv("POSTGRES_HOST", "localhost")
db_name = os.getenv("POSTGRES_DB", "demo")
db_user = os.getenv("POSTGRES_USER", "user")
db_pass = os.getenv("POSTGRES_PASSWORD", "password")


def get_db_connection():
    conn = psycopg2.connect(
        host=db_host, database=db_name, user=db_user, password=db_pass
    )
    return conn


@app.route("/")
def home():
    return "Welcome to the Compose Advanced Demo!"


@app.route("/initdb")
def initdb():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS items (id SERIAL PRIMARY KEY, name TEXT NOT NULL);"
    )
    cur.execute(
        "INSERT INTO items (name) VALUES ('Docker'), ('Compose'), ('PostgreSQL');"
    )
    conn.commit()
    cur.close()
    conn.close()
    return "Database initialized and seeded!"


@app.route("/items")
def items():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM items;")
    items = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(items)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
