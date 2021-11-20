import json
import logging
import functions
import requests as req
from config import token

logger = logging.getLogger(__name__)

def kc(rsn):
    if functions.is_valid_rsn(rsn):
        
        try:
            url = f'https://www.osrsbotdetector.com/dev/v1/stats/contributions/{rsn}'
            r = json.loads(req.get(url).text)
            
            bans = r['total']['bans']
            reports = r['total']['reports']
            ban_percent = round((bans/reports)*100,2)
            bans = "{:,}".format(bans)
            reports = "{:,}".format(reports)

            manual_bans = r['manual']['bans']
            manual_reports = r['manual']['reports']
            manual_incorrect = r['manual']['incorrect_reports']
            accuracy = " They have a report accuracy of " + str(round((manual_reports-manual_incorrect)/(manual_reports)*100, 2)) + "%"

            if manual_reports == 0:
                accuracy = ''

            response = f'{ban_percent}% ({bans}/{reports}) of accounts encountered by {rsn} have been banned.{accuracy}'
            return response
        except Exception as e:
            logger.debug(f'Getting Data Error or API status update error. {e}')
            
    else:
        response = "The system could not detect a valid RSN. Please send your message again using a valid RSN."
        return response