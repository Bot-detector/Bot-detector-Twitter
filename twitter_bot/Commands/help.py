import logging
def help(text, parent_tweet_id, api):
    check = 'help'
    if text[:len(check)] == check:
        response = "Commands: 'predict'+<RSN>,'banstatus'+<RSN>,'appeal'. Example: @Osrsbotdetector predict Ferrariic"
        return response