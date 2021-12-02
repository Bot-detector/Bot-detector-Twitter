import logging
import pickle
import time
import os

import tweepy

from config import *
from Tweet.Tweet import Tweet

logger = logging.getLogger(__name__)

client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret, return_type='dict', wait_on_rate_limit=True)

with open(os.path.join(os.curdir + r"/pickle-jar/last_tweet.pickle"), "rb") as input_file:
    try:
        newest_tweet = pickle.load(input_file)
    except EOFError:
        newest_tweet = None


if __name__ == '__main__':
    while True:
        Responses = client.get_users_mentions(1385386880464822274, max_results=100, since_id=newest_tweet)
        
        if Responses.meta['result_count'] == 0: # No new tweets
            logger.debug("Sleeping.")
            time.sleep(100) # Sleep for 100 seconds, and then continue
            continue
        
        logger.debug(f'{Responses}')
        newest_tweet = Responses.meta['newest_id']

        with open(os.path.join(os.curdir + r"/pickle-jar/last_tweet.pickle"), "wb") as output_file:
            pickle.dump(newest_tweet, output_file)
        
        for tweet in Responses.data:
            m = Tweet(tweet, client)
            m.reply()