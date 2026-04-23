from flask import Flask, request, jsonify
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

# Home
@app.route("/")
def home():
    return "ACEest Fitness API Running"

# Add Client
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

# Get Client
@app.route("/clients/<name>", methods=["GET"])
def get_client(name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT * FROM clients WHERE name=?", (name,))
    row = cur.fetchone()

    conn.close()

    if row:
        return jsonify({
            "name": row[0],
            "age": row[1],
            "weight": row[2],
            "program": row[3],
            "calories": row[4]
        })

    return jsonify({"error": "Client not found"}), 404

# Add Progress
@app.route("/progress", methods=["POST"])
def add_progress():
    data = request.json

    name = data["name"]
    adherence = data["adherence"]
    week = datetime.now().strftime("Week %U - %Y")

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO progress (client_name, week, adherence)
        VALUES (?, ?, ?)
    """, (name, week, adherence))

    conn.commit()
    conn.close()

    return jsonify({"message": "Progress saved"})

# Get Progress
@app.route("/progress/<name>", methods=["GET"])
def get_progress(name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT week, adherence FROM progress WHERE client_name=?", (name,))
    rows = cur.fetchall()

    conn.close()

    return jsonify([
        {"week": r[0], "adherence": r[1]} for r in rows
    ])

# Health check (important for CI/CD)
@app.route("/health")
def health():
    return jsonify({"status": "OK"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)