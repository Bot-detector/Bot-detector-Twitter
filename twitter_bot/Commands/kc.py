import logging
import functions
import requests

logger = logging.getLogger(__name__)

def web_request(url):
    data = requests.get(url)
    return data.json()

def kc(rsn):
    response = None
    if not functions.is_valid_rsn(rsn):
        response = "The system could not detect a valid RSN. Please send your message again using a valid RSN."
        return response

    # get the project stats
    data = web_request('https://www.osrsbotdetector.com/dev/site/dashboard/projectstats')
    project_ban_pct = 11
    if data['total_bans'] != 0:
        project_ban_pct = round((data['total_accounts']/data['total_bans'])*100,2)

    # get the player stats
    data = web_request(f'https://www.osrsbotdetector.com/dev/v1/stats/contributions/{rsn}')
    total = data['total']
    manual = data['manual']
    bans, reports, manual_reports, manual_incorrect = total['bans'], total['reports'], manual['reports'], manual['incorrect_reports']

    # player has no stats
    if total['reports'] == 0:
        response = "There was an error collecting your data. Make sure anonymous mode has been turned off and verify that you have kc through the plugin."
        return response

    # calculate the player accuracy
    accuracy = ''
    if manual_reports != 0:
        accuracy = round((manual_reports - manual_incorrect)/(manual_reports)*100, 2)
        accuracy = f" You have a report accuracy of {str(accuracy)}%"
       
    # parse 
    player_ban_pct = round((bans/reports)*100,2)
    bans = "{:,}".format(bans)
    reports = "{:,}".format(reports)
    
    relative_ban_pct = round((player_ban_pct - project_ban_pct), 2)
    
    arrow, inc_dec, plus_minus = '⬇️', 'decrease', '-'
    if relative_ban_pct >= 0:
        arrow, inc_dec, plus_minus = '⬆️', 'increase', '+'
        
    shifted_statement = f'This is a {plus_minus}{relative_ban_pct}%{arrow} {inc_dec} compared to the global average of {project_ban_pct}%.'
    response = f'🧙 {player_ban_pct}% ({bans}/{reports}) of accounts encountered by {rsn} have been banned. {shifted_statement}{accuracy}'
    return response
