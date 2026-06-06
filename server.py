"""Emotion detection Flask application."""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector Web Application")

@app.route("/emotionDetector")
def emotion_detection_analysis():
    """Analyze the emotion of the provided text."""

    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response == {"dominant_emotion": None}:
        return "Invalid text! Please try again!."

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is "
        f"{response['dominant_emotion']}."
    )


@app.route("/")
def render_html():
    """Render the main HTML page."""

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
    