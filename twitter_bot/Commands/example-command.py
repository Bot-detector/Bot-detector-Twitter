import logging
def example_command(text):
    
    """
    text --> Indicates the string (XXXXXX) after the @Osrsbotdetector XXXXXXXX in a mention. Ex. (@osrsbotdetector 'predict ferrariic...')
    parent_tweet_id --> Indicates the tweet to reply to, this is needed to reply to the tweet that is sending the command.
    api --> Tweepy api, needed for config.
    """
    
    check = 'CommandTriggerWord'
    if text[:len(check)] == check: # Checks to see if the mention string starts with the command trigger word.
        message_content_after_trigger_word = text[len(check):] # All content after trigger word goes here.
        
        """
        Example tweet: "@osrsbotdetector predict Ferrariic"
        text= 'predict ferrariic'
        message_content_after_trigger_word (if check == 'predict') = '_ferrariic' (NOTE THE SPACE AT THE BEGINNING OF THE MSG CONTENT)
        """
        
        "...add logic here..."
        
        
        response = 'Put your response here.'
        return response
        # Give a response to the tweet that mentioned the account. 