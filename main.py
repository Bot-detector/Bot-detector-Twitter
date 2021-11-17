import pandas as pd
import numpy as np
import requests as req
import tweepy
import time
from dotenv import load_dotenv
import os

load_dotenv()
ck = os.getenv("consumer_key")
cs = os.getenv("consumer_secret")
at = os.getenv("access_token")
ats = os.getenv("access_token_secret")

auth = tweepy.OAuthHandler(ck, cs)
auth.set_access_token(at, ats)

api = tweepy.API(auth)

current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
number_of_bans = 12479
s = f"""More than {number_of_bans} Accounts were Banned by Jagex Anti-Cheat Today on {current_time}."""
if len(s) > 280:
    print("Cannot send, over character limit.")
else:
    api.update_status(s)