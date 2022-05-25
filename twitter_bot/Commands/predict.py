import json
import logging
import functions
import requests as req
from config import token

logger = logging.getLogger(__name__)


def predict(rsn):
    if functions.is_valid_rsn(rsn):

        try:
            url = f"https://osrsbotdetector.com/dev/v1/prediction?token={token}&name={rsn}"
            response = json.loads(req.get(url).text)[0]
            response = f"""🧙 {rsn} has a {response['Predicted_confidence']}% likelihood of being a {response['Prediction'].replace('_',' ')}."""
            logger.info(f"Prediction Sent for {rsn}.")
            return response
        except Exception as e:
            logger.debug(f"Getting Data Error or API status update error. {e}")

    else:
        response = "The system could not detect a valid RSN. Please send your message again using a valid RSN."
        return response
