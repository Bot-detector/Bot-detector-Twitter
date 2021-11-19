import logging
def appeal(text, parent_tweet_id, api):
    check = 'appeal'
    if text[:len(check)] == check:
        response = 'Appeal your ban here: http://jgx.game/Ban - Note: Our system does not have the amount and depth of data that Jagex has on hand, and therefore cannot be used as evidence to dispute rule-breaking behavior.'
        return response