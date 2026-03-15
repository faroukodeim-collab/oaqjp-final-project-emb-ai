''' This module deploy emotion detecor app
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detecor_app():
    ''' This is the emotion detecor function
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    analysis_result = emotion_detector(text_to_analyze)
    if analysis_result["dominant_emotion"] is None:
        return 'Invalid text! Please try again!'
    output_text = f'''
    For the given statement, the system response is 
    'anger': {analysis_result["anger"]}, 
    'disgust': {analysis_result["disgust"]}, 
    'fear': {analysis_result["fear"]},
    'joy': {analysis_result["joy"]} and 
    'sadness': {analysis_result["sadness"]}. 
    The dominant emotion is {analysis_result["dominant_emotion"]}.'''
    return output_text

@app.route("/")
def home_page():
    ''' This function shows the home page
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
