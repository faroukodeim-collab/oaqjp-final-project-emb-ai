# import request and json
import requests, json

def emotion_detector(text_to_analyse):
    ''' This function takes a text to be analyzed and return the outcome of Watson NLP Library as text
    '''
    # Inputs for request
    URL= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    # perform request and store response object
    response = requests.post(URL, json = input_json, headers=headers)
    # in case of status_code = 400, retrun dictionary with values of all keys being None
    if response.status_code == 400:
        result_dict = {
        "anger": None, 
        "disgust": None, 
        "fear": None, 
        "joy": None, 
        "sadness": None,
        "dominant_emotion": None
        }  
        return result_dict
    
    # Convert the response text into a dictionary using the json library functions
    response_dict = json.loads(response.text)
    # Extract the required set of emotions, including anger, disgust, fear, joy and sadness, along with their scores
    anger_score = response_dict["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = response_dict["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = response_dict["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = response_dict["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = response_dict["emotionPredictions"][0]["emotion"]["sadness"]
    # Form result dictionary, at first without dominant emotion
    result_dict = {
        "anger":anger_score, 
        "disgust":disgust_score, 
        "fear":fear_score, 
        "joy":joy_score, 
        "sadness":sadness_score
        }
    # Find highest score and return domnant emotion    
    scores = list(result_dict.values())
    emotions = list(result_dict.keys())
    max_score= max(scores)
    max_score_index = scores.index(max_score)
    dominant_emotion = emotions[max_score_index]
    # append dominant emotion to results dictionary
    result_dict["dominant_emotion"] = dominant_emotion
    # return the text attribute of the response
    return result_dict
