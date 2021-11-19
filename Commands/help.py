def help(text_removed_at, parent_tweet_id, api):
    check = 'help'
    if text_removed_at[:len(check)] == check:
        response = "Command format: @Osrsbotdetector <'predict','banstatus'> <RSN>. Example: @Osrsbotdetector predict Ferrariic"
        try:
            api.update_status(status=response, in_reply_to_status_id=parent_tweet_id, auto_populate_reply_metadata=True)
        except Exception as e:
            print(f'Status update error. {e}')