import os
from dotenv import load_dotenv
import logging
import sys

load_dotenv()
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
bearer_token = os.getenv('bearer_token')
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")
token = os.getenv("token")


# setup logging
file_handler = logging.FileHandler(filename="log.log", mode='a')
stream_handler = logging.StreamHandler(sys.stdout)

# # log formatting
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

handlers = [
    file_handler,
    stream_handler
]

logging.basicConfig(level=logging.DEBUG, handlers=handlers)
logging.getLogger("tweepy.client").setLevel(logging.WARNING)
logging.getLogger("urllib3.connectionpool").setLevel(logging.WARNING)
logging.getLogger("requests_oauthlib.oauth1_auth").setLevel(logging.WARNING)
logging.getLogger("oauthlib").setLevel(logging.WARNING)