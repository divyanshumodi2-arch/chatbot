from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq
import os

app = Flask(__name__)
CORS(app)
client = Groq(api_key="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")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # ← fixed

@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "dm_chat_2.html")  # ← fixed

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": user_message}]
    )
    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)