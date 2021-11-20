import logging
def help(text):
    check = 'help'
    if text[:len(check)] == check:
        response = "Command List: 'predict', 'banstatus', 'appeal', 'test', 'help'. Example: @Osrsbotdetector predict Ferrariic"
        return response