import json

import functions
import requests as req
from config import token

def predict(text_removed_at, parent_tweet_id, api):
    check = 'predict'
    if text_removed_at[:len(check)] == check:
        predict_text = text_removed_at[len(check):]
        rsn = predict_text[1:13].lower()

        print(f"Forming a prediction for {rsn}")

        if functions.is_valid_rsn(rsn):
            try:
                url = f'https://osrsbotdetector.com/dev/v1/prediction?token={token}&name={rsn}'
                response = json.loads(req.get(url).text)[0]
                prediction_response = f"""{rsn} has a {response['Predicted_confidence']}% likelihood of being a {response['Prediction'].replace('_',' ')}."""
                api.update_status(status=prediction_response, in_reply_to_status_id=parent_tweet_id, auto_populate_reply_metadata=True)
                print(f"Prediction Sent for {rsn}.")
            except Exception as e:
                print(f'Getting Data Error or API status update error. {e}')
        else:
            try:
                print("Not a valid rsn")
                api.update_status(status = "The system could not detect a valid RSN. Please send your message again using a valid RSN.", in_reply_to_status_id=parent_tweet_id, auto_populate_reply_metadata=True)
            except Exception as e:
                print(f'Could not detect valid RSN error, posting error. {e}')
