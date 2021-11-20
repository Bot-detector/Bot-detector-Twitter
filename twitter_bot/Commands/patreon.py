def patreon(text):
    check = 'patreon'
    if text[:len(check)] == check:
        response = "Come support us for just $1 on Patreon! https://www.patreon.com/bot_detector"
        return response