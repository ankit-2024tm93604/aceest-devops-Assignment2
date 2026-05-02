from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)

DB_NAME = "aceest.db"

# ---------- DATABASE ----------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            name TEXT PRIMARY KEY,
            age INTEGER,
            weight REAL,
            program TEXT,
            calories INTEGER
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT,
            week TEXT,
            adherence INTEGER
        )
    """)

    conn.commit()
    conn.close()

init_db()

# ---------- PROGRAM DATA ----------
programs = {
    "Fat Loss": 22,
    "Muscle Gain": 35,
    "Beginner": 26
}

# ---------- ROUTES ----------

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/clients", methods=["POST"])
def add_client():
    data = request.json

    name = data["name"]
    age = data["age"]
    weight = data["weight"]
    program = data["program"]

    if program not in programs:
        return jsonify({"error": "Invalid program"}), 400

    calories = int(weight * programs[program])

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        INSERT OR REPLACE INTO clients (name, age, weight, program, calories)
        VALUES (?, ?, ?, ?, ?)
    """, (name, age, weight, program, calories))

    conn.commit()
    conn.close()

    return jsonify({
        "message": "Client saved",
        "calories": calories
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)