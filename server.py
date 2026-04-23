from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Emotion Detection API is running!"

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text = request.args.get("text")

    if text is None or text.strip() == "":
        return jsonify({
            "error": "Invalid input. Please enter some text."
        }), 400

    result = emotion_detector(text)
    return jsonify(result), 200

if __name__ == "__main__":
    app.run(debug=True)
