from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Final project")

@app.route("/")
def display_index():
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]
    result_text = (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': "
        f"{fear}, 'joy': {joy} and 'sadness': "
        f"{sadness}. The dominant emotion is {dominant}."
    )
    return result_text, 200

if __name__ == "__main__":
    app.run(host='localhost', port=5000)