def github(text):
    check = 'github'
    if text[:len(check)] == check:
        response = "Check out our code on github! https://github.com/Bot-detector"
        return response