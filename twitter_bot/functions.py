import re
import json

def filter_mentions(status):
        json_str = json.loads(json.dumps(status._json))
        text = json_str['text']
        text_removed_at = text[text.rfind('@OSRSBotDetector')+17:].lower()
        parent_tweet_id = json_str['id']
        return parent_tweet_id, text_removed_at
    
    
def is_valid_rsn(rsn):
    return re.fullmatch("[\w\d _-]{1,12}", rsn)
