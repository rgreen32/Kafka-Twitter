from kafka import KafkaProducer
from kafka.errors import KafkaError
from logging import log
from app.core import Streamer

class Producer():
    
    def __init__(self):
        self.conn = KafkaProducer(security_protocol="PLAINTEXT", bootstrap_servers=["localhost:9092"])
        self.streamer = Streamer()
        
    def start_producer_loop(self, topic):
        print("Starting producer loop for twittertopic: " + topic)
        stream = self.streamer.get_stream(topic)
        for tweet in stream:
            self.conn.send("TrendingOnTwitter",tweet.encode(), topic.encode()).add_errback(on_send_error)


def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)