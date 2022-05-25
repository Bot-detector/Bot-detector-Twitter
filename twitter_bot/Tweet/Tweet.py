from Commands import (
    appeal,
    banned,
    help,
    predict,
    test,
    github,
    patreon,
    discord,
    website,
    linktree,
    stats,
    kc,
)
import logging
import tweepy


class Tweet:
    def __init__(self, tweet, client):
        self.tweet = tweet.text.lower()
        logging.info(f"{self.tweet=}")
        self.parent_id = tweet.id
        self.client = client

        self.switch = {
            "predict": predict.predict,
            "banstatus": banned.banstatus,
            "appeal": appeal.appeal,
            "help": help.help,
            "test": test.test,
            "github": github.github,
            "patreon": patreon.patreon,
            "discord": discord.discord,
            "website": website.website,
            "linktree": linktree.linktree,
            "stats": stats.stats,
            "kc": kc.kc,
        }

    def __parser(self):
        # Tag processing
        tag = "@OSRSbotdetector"
        tag = tag.lower()
        tag_position = self.tweet.rfind(tag) + len(tag)
        text = self.tweet[tag_position:]

        # Corrects Text
        text = text.strip()

        # Delimiter for keyword  | query combos
        loc = text.find(" ")
        if loc == -1:
            loc = len(text)

        # Takes key_word and query
        key_word = text[:loc]
        query = text[loc:].strip()

        logging.info(f"{key_word=} {query=}")

        # Gets function from switch
        func = self.switch.get(key_word)

        if func is None:
            return

        # Gets Response
        response = func(query)
        return response

    def reply(self):
        response = self.__parser()
        if response is None:
            return

        logging.info(f"{response=}")

        try:
            self.client.create_tweet(in_reply_to_tweet_id=self.parent_id, text=response)
        except tweepy.Forbidden:
            logging.warning(f"Forbidden Error: {self.tweet=} {self.parent_id=}")
