import re
import json
import logging

def filter_mentions(status):
        json_str = json.loads(json.dumps(status._json))
        raw_text = json_str['text']
        text = raw_text[raw_text.rfind('@OSRSBotDetector')+17:].lower()
        parent_tweet_id = json_str['id']
        return parent_tweet_id, text
    
    
def is_valid_rsn(rsn):
        return re.fullmatch("[\w\d _-]{1,12}", rsn)

def send_tweet(api, response, parent_tweet_id):
        try:
                api.update_status(status=response, in_reply_to_status_id=parent_tweet_id, auto_populate_reply_metadata=True)
        except Exception as e:
                logging.debug(f'Status update error. {e}')