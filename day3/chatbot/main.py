from flask import Flask, request, jsonify, render_template
from google import genai

client = genai.Client(api_key='AlzaSyBOsI3P9rYr7bD2XhdXWUjslxWD8PiGXD8')
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat",methods=["POST"])
def chat():
    prompt = request.json["message"]
    response = client.models.generate_content(
        model='gemini-3-pro-preview',
        contents=prompt
    )
    return jsonify({"reply":response.text})

app.run(port=8080)
