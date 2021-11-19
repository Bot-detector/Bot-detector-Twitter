def appeal(text_removed_at, parent_tweet_id, api):
    check = 'appeal'
    if text_removed_at[:len(check)] == check:
        response = 'Appeal your ban here: http://jgx.game/Ban - Note: Our system does not have the amount and depth of data that Jagex has on hand, and therefore cannot be used as evidence to dispute rule-breaking behavior.'
        try:
            api.update_status(status=response, in_reply_to_status_id=parent_tweet_id, auto_populate_reply_metadata=True)
        except Exception as e:
            print(f'Status update error. {e}')