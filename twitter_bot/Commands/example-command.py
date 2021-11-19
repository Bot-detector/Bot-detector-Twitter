def example_command(text_removed_at, parent_tweet_id, api):
    
    """
    text_removed_at --> Indicates the string (XXXXXX) after the @Osrsbotdetector XXXXXXXX in a mention. Ex. (@osrsbotdetector 'predict ferrariic...')
    parent_tweet_id --> Indicates the tweet to reply to, this is needed to reply to the tweet that is sending the command.
    api --> Tweepy api, needed for config.
    """
    
    check = 'CommandTriggerWord'
    if text_removed_at[:len(check)] == check: # Checks to see if the mention string starts with the command trigger word.
        message_content_after_trigger_word = text_removed_at[len(check):] # All content after trigger word goes here.
        
        """
        Example tweet: "@osrsbotdetector predict Ferrariic"
        text_removed_at = 'predict ferrariic'
        message_content_after_trigger_word (if check == 'predict') = '_ferrariic' (NOTE THE SPACE AT THE BEGINNING OF THE MSG CONTENT)
        """
        
        "...add logic here..."
        
        
        response_text = 'Put your response here.'
        # Give a response to the tweet that mentioned the account. 
        if len(response_text < 280):
            try:
                api.update_status(status=response_text, in_reply_to_status_id=parent_tweet_id, auto_populate_reply_metadata=True)
            except Exception as e:
                print(f'Status update error. {e}')