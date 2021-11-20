import requests as req
import json
import time

def stats(text):
    r = req.get('https://www.osrsbotdetector.com/dev/site/dashboard/projectstats').text
    r = json.loads(r)

    accounts = r['total_accounts']
    bans = r['total_bans']
    faccounts = "{:,}".format(accounts)
    fbans = "{:,}".format(bans)
    days_since_start = int((time.time() - 1614470400)/(60*60*24))

    response = f'We have seen {faccounts} accounts in-game since we started tracking {days_since_start} days ago. Of which, at least {fbans} accounts have been banned off of the Hiscores. This comes out to at least {round((bans/accounts)*100,2)}% of the Playerbase being banned.'
    return response