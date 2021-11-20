import json
import logging
import functions
import requests as req
from config import token

def predict(text):
    check = 'predict'
    if text[:len(check)] == check:
        rsn = text[len(check):][1:13].lower()
        
        if functions.is_valid_rsn(rsn):
            
            try:
                url = f'https://osrsbotdetector.com/dev/v1/prediction?token={token}&name={rsn}'
                response = json.loads(req.get(url).text)[0]
                response = f"""{rsn} has a {response['Predicted_confidence']}% likelihood of being a {response['Prediction'].replace('_',' ')}."""
                logging.info(f"Prediction Sent for {rsn}.")
                return response
            except Exception as e:
                logging.debug(f'Getting Data Error or API status update error. {e}')
                
        else:
            response = "The system could not detect a valid RSN. Please send your message again using a valid RSN."
            return response
