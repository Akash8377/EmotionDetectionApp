from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return "Emotion Detection Application"

@app.route("/emotionDetector")
def detect_emotion():
    text = request.args.get("text")

    response = emotion_detector(text)

    if "error" in response:
        return "Invalid input! Try again."

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(debug=True)
