
from Commands import appeal, banned, help, predict, test, github, patreon, discord, website, linktree, stats

class Tweet:
    
    def __init__(self, tweet, client):
        self.tweet = tweet.text.lower()
        print(f'{self.tweet=}')
        self.parent_id = tweet.id
        self.client = client
        
        self.switch = {
            'predict': predict.predict,
            'banstatus':banned.banstatus,
            'appeal':appeal.appeal,
            'help':help.help,
            'test':test.test,
            'github':github.github,
            'patreon':patreon.patreon,
            'discord':discord.discord,
            'website':website.website,
            'linktree':linktree.linktree,
            'stats':stats.stats,
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
        loc = text.find(' ')
        if loc == -1:
            loc = len(text)
            
        # Takes key_word and query
        key_word = text[:loc]
        query = text[loc:].strip()
        
        print(f'{key_word=} {query=}')

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
        
        print(f'{response=}')
        
        self.client.create_tweet(in_reply_to_tweet_id=self.parent_id, text=response)