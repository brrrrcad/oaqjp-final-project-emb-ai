import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

def emotion_detector(text_to_analyze):
    data = json.dumps({ "raw_document": { "text": text_to_analyze } })
    response = requests.post(url=URL, headers=HEADERS, data=data)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    response_json = json.loads(response.text)
    emotions_dict = response_json["emotionPredictions"][0]["emotion"]
    max_value = max(emotions_dict.values())
    for emotion in emotions_dict.keys():
        if emotions_dict[emotion] == max_value:
            dominant_emotion = emotion
    emotions_dict["dominant_emotion"] = dominant_emotion
    return emotions_dict

