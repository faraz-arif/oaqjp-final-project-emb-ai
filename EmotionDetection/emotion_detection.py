import requests
import json

def emotion_detector(text_to_analyze):
    # Handle blank or empty input before sending request
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Set the headers with the required model ID for the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create the payload dictionary with the text to analyze
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=headers)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Parse the response from the API
        formatted_response = json.loads(response.text)
        
        # Extract the dictionary of emotions
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        anger_score = emotions.get('anger')
        disgust_score = emotions.get('disgust')
        fear_score = emotions.get('fear')
        joy_score = emotions.get('joy')
        sadness_score = emotions.get('sadness')
        
        # Calculate the dominant emotion (key with highest score)
        dominant_emotion = max(emotions, key=emotions.get)
    else:   # For any other unexpected status codes, set label and score to None
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    # Return the label and score in a dictionary
    return {'anger': anger_score, 'disgust': disgust_score,'fear': fear_score,'joy': joy_score,'sadness': sadness_score,'dominant_emotion': dominant_emotion}
