import logging
import time

import tweepy

from config import *
from Tweet.Tweet import Tweet

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret, return_type='dict', wait_on_rate_limit=True)

logging.basicConfig(filename='log.log', level=logging.DEBUG)

newest_tweet = 1462125811104890885
while True:
    print("Waiting on mentions.")
    
    Responses = client.get_users_mentions(1385386880464822274, max_results=100, since_id=newest_tweet)
    
    if Responses.meta['result_count'] == 0: # No new tweets
        time.sleep(100) # Sleep for 100 seconds, and then continue
        continue
    
    print(f'{Responses}')
    newest_tweet = Responses.meta['newest_id']
    
    for tweet in Responses.data:
        m = Tweet(tweet, client)
        m.reply()
        
    print("Sleeping...")
    time.sleep(100) # Check every 100 seconds.
