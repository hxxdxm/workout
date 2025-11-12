from flask import Flask, jsonify
import json, os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/api/subject")
def get_subject():
    data = load_data()
    return jsonify(data["subject"])

@app.get("/api/rationale")
def get_rationale():
    data = load_data()
    return jsonify(data["rationale"])

@app.get("/api/features")
def get_features():
    data = load_data()
    return jsonify(data["features"])

@app.get("/api/environment")
def get_environment():
    data = load_data()
    return jsonify(data["environment"])

@app.get("/api/team")
def get_team():
    data = load_data()
    return jsonify(data["team"])

@app.get("/api/all")
def get_all():
    data = load_data()
    return jsonify(data)

@app.get("/")
def index():
    return jsonify({"message": "Mozik API 서버가 실행 중입니다."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)