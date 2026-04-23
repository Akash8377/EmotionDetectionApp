from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Emotion Detection API Running"

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text = request.args.get("text")

    if text is None or text.strip() == "":
        return jsonify({
            "error": "Invalid input"
        }), 400

    result = emotion_detector(text)
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(debug=True)
