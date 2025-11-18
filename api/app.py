from flask import Flask, jsonify, render_template
import json, os

app = Flask(__name__, template_folder="../web")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# API 상태 확인 (JSON)
@app.get("/api/status")
def api_status():
    return jsonify({"message": "Mozik API 서버가 실행 중입니다."})

# API 라우트들
@app.route("/")
def home():
    return render_template("main.html")

@app.route("/subject")
def subject():
    return render_template("subject.html")

@app.route("/rationale")
def rationale():
    return render_template("rationale.html")

@app.route("/features")
def features():
    return render_template("features.html")

@app.route("/environment")
def environment():
    return render_template("environment.html")

@app.route("/team")
def team():
    return render_template("team.html")

@app.get("/api/all")
def get_all():
    data = load_data()
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)