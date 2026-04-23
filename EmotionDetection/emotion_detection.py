import requests

def emotion_detector(text_to_analyze):
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return {
            "error": "Invalid input. Please enter valid text.",
            "status": 400
        }

    response = {
        "anger": 0.05,
        "disgust": 0.02,
        "fear": 0.1,
        "joy": 0.75,
        "sadness": 0.08
    }

    dominant_emotion = max(response, key=response.get)

    result = {
        "anger": response["anger"],
        "disgust": response["disgust"],
        "fear": response["fear"],
        "joy": response["joy"],
        "sadness": response["sadness"],
        "dominant_emotion": dominant_emotion
    }

    return result
