from flask import Flask, jsonify
import psycopg2, os

app = Flask(__name__)
DB_URL = os.getenv("DATABASE_URL")

@app.route("/")
def home():
    return "ElFroggo API is alive!"

@app.route("/frogs")
def frogs():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute("SELECT id, name, scientificname, color FROM Frogs;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id":r[0],"name":r[1],"scientificName":r[2],"color":r[3]} for r in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
