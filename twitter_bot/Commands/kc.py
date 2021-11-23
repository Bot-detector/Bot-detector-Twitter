import json
import logging
import functions
import requests as req
from config import token

logger = logging.getLogger(__name__)

def kc(rsn):
    def get_global_banrate():
        r = req.get('https://www.osrsbotdetector.com/dev/site/dashboard/projectstats').text
        r = json.loads(r)
        accounts = r['total_accounts']
        bans = r['total_bans']
        global_ban_percent = round((bans/accounts)*100,2)
        return global_ban_percent
    
    response = None
    if functions.is_valid_rsn(rsn):
        
        try:
            url = f'https://www.osrsbotdetector.com/dev/v1/stats/contributions/{rsn}'
            r = json.loads(req.get(url).text)
            
            bans = r['total']['bans']
            reports = r['total']['reports']
            if reports == 0:
                response = "There was an error collecting your data. Make sure anonymous mode has been turned off and verify that you have kc through the plugin."
                return response
            
            local_ban_percent = round((bans/reports)*100,2)
            bans = "{:,}".format(bans)
            reports = "{:,}".format(reports)

            manual_reports = r['manual']['reports']
            if manual_reports == 0:
                accuracy = ''
            else:
                manual_incorrect = r['manual']['incorrect_reports']
                accuracy = " They have a report accuracy of " + str(round((manual_reports-manual_incorrect)/(manual_reports)*100, 2)) + "%"
                
            if reports == 0:
                return response
            
            try:
                global_ban_percent = get_global_banrate()
                shifted_ban_percent = round((local_ban_percent - global_ban_percent), 2)
                if shifted_ban_percent >= 0:
                    arrow = '⬆️'
                    inc_dec = 'increase'
                    plus_minus = '+'
                else:
                    arrow = '⬇️'
                    inc_dec = 'decrease'
                    plus_minus = '-'
                shifted_statement = f'This is a {plus_minus}{shifted_ban_percent}%{arrow} {inc_dec} compared to the global average of {global_ban_percent}%'
                response = f'🧙 {local_ban_percent}% ({bans}/{reports}) of accounts encountered by {rsn} have been banned. {shifted_statement}.{accuracy}.'
            except:
                response = f'🧙 {local_ban_percent}% ({bans}/{reports}) of accounts encountered by {rsn} have been banned.{accuracy}.'
                
            return response
        
        except Exception as e:
            logger.debug(f'Getting Data Error or API status update error. {e}')
            
    else:
        response = "The system could not detect a valid RSN. Please send your message again using a valid RSN."
        return response