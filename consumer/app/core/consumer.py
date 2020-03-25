from kafka import KafkaConsumer
from emoji import UNICODE_EMOJI
from app.data import DbHandler

class Consumer():
    def __init__(self):
        self.conn = KafkaConsumer("TrendingOnTwitter", group_id="mygroup", bootstrap_servers=["localhost:9092"])
        self.handler = DbHandler()


    def start_consumer_loop(self):
        print("Starting consumer loop")
        for message in self.conn:
            tweet =  message.value.decode("utf-8")
            for emoji in UNICODE_EMOJI:
                emojicount = tweet.count(emoji)
                if(emojicount > 0):
                    twittertopic = message.key.decode("utf-8")
                    self.handler.increment(twittertopic, emoji)
                    
