from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os

app = Flask(__name__)
CORS(app)
client = Groq(api_key=os.environ.get("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"))

@app.route("/")
def index():
    with open("dm_chat_2.html", "r") as f:
        return f.read()

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
