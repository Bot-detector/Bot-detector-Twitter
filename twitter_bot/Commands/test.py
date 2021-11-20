import logging
import time
def test(text):
    check = 'test'
    if text[:len(check)] == check:
        response = f"Twitter Bot is Active and Alive! Read at {time.time()}."
        return response