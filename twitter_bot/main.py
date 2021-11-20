import logging
import pickle
import time

import tweepy

import functions
from Commands import appeal, banned, help, predict, test, github, patreon, discord, website, linktree, stats
from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True) # DO NOT DISABLE WAIT ON RATE LIMIT = TRUE, The app will get suspended and we'll probably lose the account lol

logging.basicConfig(filename='log.log', level=logging.DEBUG)

with open(r"seen_tweets.pickle", "rb") as input_file:
    seen_tweets = pickle.load(input_file)
    
# Logs tweets that were seen previously, to help prevent hitting daily 1k update_status limit or 300/hr limit
# Should probably write seen tweets to a file, and remove earliest in list of 100, api.mentions_timeline can pull 800 or so, but
# in reality we probably only need to hold 100 and pull 30 at a time. 100K mentions_timeline pulls can be performed / 24 hr period, so this is
# not a limiting factor.

print(f'Loaded {len(seen_tweets)} tweets')

while True:
    logging.info(f"Waiting for mentions {time.time()}")
    print("Processing Mentions")
    for status in api.mentions_timeline(count=30):
        
        parent_tweet_id, text = functions.filter_mentions(status)

        if parent_tweet_id in seen_tweets:
            continue
        seen_tweets.append(parent_tweet_id)
        
        # Stores seen tweets so that they won't be run for the future, preventing API spam.
        with open(r"seen_tweets.pickle", "wb") as output_file:
            pickle.dump(seen_tweets, output_file)
        
        """
            Commands
        """
        # Testing Response
        response = test.test(text)
        if response is not None:
            functions.send_tweet(api, response, parent_tweet_id)
            
        # Help Command
        response = help.help(text)
        if response is not None:
            functions.send_tweet(api, response, parent_tweet_id)
            
        # Github Link
        response = github.github(text)
        if response is not None:
            functions.send_tweet(api, response, parent_tweet_id)
            
        # Patreon Link
        response = patreon.patreon(text)
        if response is not None:
            functions.send_tweet(api, response, parent_tweet_id)
            
        # Discord Link
        response = discord.discord(text)
        if response is not None:
            functions.send_tweet(api, response, parent_tweet_id)
        
        # Website Link
        response = website.website(text)
        if response is not None:
            functions.send_tweet(api, response, parent_tweet_id)
            
        # LInktree Link
        response = linktree.linktree(text)
        if response is not None:
            functions.send_tweet(api, response, parent_tweet_id)
            
        # Jagex appeal command
        response = appeal.appeal(text)
        if response is not None:
            functions.send_tweet(api, response, parent_tweet_id)
            
        # Stats command
        response = stats.stats(text)
        if response is not None:
            functions.send_tweet(api, response, parent_tweet_id)
            
        # Predict command
        response = predict.predict(text)
        if response is not None:
            functions.send_tweet(api, response, parent_tweet_id)
            
        # Banstatus command
        response = banned.banstatus(text)
        if response is not None:
            functions.send_tweet(api, response, parent_tweet_id)
            
    print("Sleeping...")
    time.sleep(100) # Check every 100 seconds.