import json
import time

import tweepy

from Commands import banned, help, predict, appeal
from config import *
import functions

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

seen_tweets = [1461731543500525568] 
# Logs tweets that were seen previously, to help prevent hitting daily 1k update_status limit or 300/hr limit
# Should probably write seen tweets to a file, and remove earliest in list of 100, api.mentions_timeline can pull 800 or so, but
# in reality we probably only need to hold 100 and pull 30 at a time. 100K mentions_timeline pulls can be performed / 24 hr period, so this is
# not a limiting factor.

while True:
    print("Waiting for mentions...")
    for status in api.mentions_timeline(count=1, since_ids=max(seen_tweets)):
        parent_tweet_id, text_removed_at = functions.filter_mentions(status)

        if parent_tweet_id in seen_tweets:
            continue
        seen_tweets.append(parent_tweet_id)
        
        """
            Commands
        """
        help.help(text_removed_at, parent_tweet_id, api)
        appeal.appeal(text_removed_at, parent_tweet_id, api)
        predict.predict(text_removed_at, parent_tweet_id, api)
        banned.banstatus(text_removed_at, parent_tweet_id, api)
                    
    time.sleep(20) # Must sleep for 20 seconds or things will go very...very poorly.