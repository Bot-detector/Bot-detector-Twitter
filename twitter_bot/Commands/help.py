import logging
def help(text):
    check = 'help'
    if text[:len(check)] == check:
        response = "Commands: 'predict'+<RSN>,'banstatus'+<RSN>,'appeal'. Example: @Osrsbotdetector predict Ferrariic"
        return response