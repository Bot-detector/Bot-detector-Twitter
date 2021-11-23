import json
import logging
import functions
import requests
from config import token

logger = logging.getLogger(__name__)

def kc(rsn):
    def get_global_banrate():
        global_stat_data = requests.get('https://www.osrsbotdetector.com/dev/site/dashboard/projectstats').text
        global_stat_data = json.loads(global_stat_data)
        accounts = global_stat_data['total_accounts']
        bans = global_stat_data['total_bans']
        
        if bans != 0:
            global_ban_percent = round((bans/accounts)*100,2)
        else:
            global_ban_percent = int(11) # Defaults to 11 if global average can't be found. This is a fine estimation and is good enough for posting if api dies.
            logging.debug('Api is dead. Defaulted global_ban_percentage as all values are 0.')
            
        return global_ban_percent
    
    def get_report_data(rsn):
        url = f'https://www.osrsbotdetector.com/dev/v1/stats/contributions/{rsn}'
        report_data = requests.get(url).json()
        bans = report_data['total']['bans']
        reports = report_data['total']['reports']
        manual_reports = report_data['manual']['reports']
        manual_incorrect = report_data['manual']['incorrect_reports']
        return bans, reports, manual_reports, manual_incorrect
    
    def form_response(global_ban_percent, accuracy, bans, reports):
        local_ban_percent = round((bans/reports)*100,2)
        bans = "{:,}".format(bans)
        reports = "{:,}".format(reports)
        
        shifted_ban_percent = round((local_ban_percent - global_ban_percent), 2)
        
        arrow = '⬇️'
        inc_dec = 'decrease'
        plus_minus = '-'
        if shifted_ban_percent >= 0:
            arrow = '⬆️'
            inc_dec = 'increase'
            plus_minus = '+'
            
        shifted_statement = f'This is a {plus_minus}{shifted_ban_percent}%{arrow} {inc_dec} compared to the global average of {global_ban_percent}%.'
        response = f'🧙 {local_ban_percent}% ({bans}/{reports}) of accounts encountered by {rsn} have been banned. {shifted_statement}{accuracy}'
        return response
            
    response = None
    if not functions.is_valid_rsn(rsn):
        response = "The system could not detect a valid RSN. Please send your message again using a valid RSN."
        return response
    
    global_ban_percent = get_global_banrate()
    bans, reports, manual_reports, manual_incorrect = get_report_data(rsn)

    if reports == 0:
        response = "There was an error collecting your data. Make sure anonymous mode has been turned off and verify that you have kc through the plugin."
        return response

    accuracy = ''
    if manual_reports != 0:
        report_accuracy = str(round((manual_reports-manual_incorrect)/(manual_reports)*100, 2))
        accuracy = " They have a report accuracy of " + report_accuracy + "%."
    
    response = form_response(global_ban_percent, accuracy, bans, reports)
    return response
