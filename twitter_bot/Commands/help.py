import logging
def help(text):
    check = 'help'
    if text[:len(check)] == check:
        response = "Command List: 'predict', 'banstatus', 'appeal', 'test', 'help', 'discord', 'patreon', 'github', 'website', 'linktree', 'stats'."
        return response