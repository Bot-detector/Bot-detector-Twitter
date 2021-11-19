import json
import time

import tweepy
import logging

from Commands import banned, help, predict, appeal
from config import *
import functions

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

logging.basicConfig(filename='log.log', level=logging.DEBUG)

seen_tweets = [1461731543500525568]
# Logs tweets that were seen previously, to help prevent hitting daily 1k update_status limit or 300/hr limit
# Should probably write seen tweets to a file, and remove earliest in list of 100, api.mentions_timeline can pull 800 or so, but
# in reality we probably only need to hold 100 and pull 30 at a time. 100K mentions_timeline pulls can be performed / 24 hr period, so this is
# not a limiting factor.

while True:
    logging.info(f"Waiting for mentions {time.time()}")
    for status in api.mentions_timeline(count=20, since_ids=max(seen_tweets)):
        parent_tweet_id, text = functions.filter_mentions(status)

        if parent_tweet_id in seen_tweets:
            continue
        seen_tweets.append(parent_tweet_id)
        
        print(text)
        
        """
            Commands
        """
        response = help.help(text, parent_tweet_id, api)
        if response is not None:
            functions.send_tweet(api, response, parent_tweet_id)
            
            
        response = appeal.appeal(text, parent_tweet_id, api)
        if response is not None:
            functions.send_tweet(api, response, parent_tweet_id)
            
            
        response = predict.predict(text, parent_tweet_id, api)
        if response is not None:
            functions.send_tweet(api, response, parent_tweet_id)
            
            
        response = banned.banstatus(text, parent_tweet_id, api)
        if response is not None:
            functions.send_tweet(api, response, parent_tweet_id)
        

                    
    time.sleep(20) # Must sleep for 20 seconds or things will go very...very poorly.