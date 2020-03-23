from kafka import KafkaProducer
from kafka.errors import KafkaError
from logging import log
from app.core import Streamer

class Producer():
    
    def __init__(self):
        self.conn = KafkaProducer(security_protocol="PLAINTEXT", bootstrap_servers=["localhost:9092"])
        self.streamer = Streamer()
        # promise = self.conn.send("testTopic", b"testing2" )
        # try:
        #     record_metadata = promise.get(timeout=10)
        #     print (record_metadata.topic)
        #     print (record_metadata.partition)
        #     print (record_metadata.offset)

        # except KafkaError:
        #    # Decide what to do if produce request failed...
        #     log.exception()
        #     pass
    def start_main_loop(self, topic):
        print("Starting producer loop for topic: " + topic)
        stream = self.streamer.get_stream(topic)
        for tweet in stream:
            self.conn.send("TrendingOnTwitter", topic.encode(), tweet.encode()).add_errback(on_send_error)

# def on_send_success(record_metadata):
    # print(record_metadata.topic)
    # print(record_metadata.partition)
    # print(record_metadata.offset)

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)