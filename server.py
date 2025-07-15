import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

app = Flask(__name__)

@app.route('/gemini-convert', methods=['POST'])
def gemini_convert():
    data = request.get_json()
    subject = data.get('subject')
    activity = data.get('activity')
    prompt = f"학생 활동기록: {activity}\n과목: {subject}\n위 내용을 교과 세부특기사항으로 변환해줘."

    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }
    response = requests.post(
        f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
        headers=headers,
        json=payload
    )
    if response.ok:
        result = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        return jsonify({"result": result})
    else:
        return jsonify({"result": "Gemini API 오류"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
