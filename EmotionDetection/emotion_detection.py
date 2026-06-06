import requests,json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url , json = my_obj , headers = header)
    for_response = json.loads(response.text)

    anger_score = for_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = for_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = for_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = for_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = for_response['emotionPredictions'][0]['emotion']['sadness']

    emotions_dic = {"anger": anger_score, "disgust": disgust_score, "fear": fear_score, "joy": joy_score, "sadness": sadness_score}

    dominant_emotion = max(emotions_dic, key=emotions_dic.get)

    return {'anger' : anger_score , 'disgust' : disgust_score , 'fear': fear_score  , 'joy' : joy_score , 'sadness' : sadness_score , 'dominant_emotion' : dominant_emotion}