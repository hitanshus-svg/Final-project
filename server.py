from flask import Flask , request , render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask ("Emotion Detector Web Application")

@app.route('/emotionDetector')

def emotion_detection_analysis():

    text_to_analyze = request.args.get('textToAnalyze')
    json = emotion_detector(text_to_analyze)
    return f"For the given statement, the system response is 'anger': {json['anger']}, 'disgust': {json['disgust']}, 'fear': {json['fear']}, 'joy': {json['joy']} and 'sadness': {json['sadness']}. The dominant emotion is {json['dominant_emotion']}."

@app.route("/")

def render_html():

    return render_template("index.html")

if __name__ == "__main__" :
    app.run()