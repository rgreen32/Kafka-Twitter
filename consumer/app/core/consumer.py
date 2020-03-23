from kafka import KafkaConsumer

class Consumer():
    def __init__(self):
        conn = KafkaConsumer("TrendingOnTwitter",group_id="mygroup", bootstrap_servers=["localhost:9092"])
        for message in conn:
            # message value and key are raw bytes -- decode if necessary!
            # e.g., for unicode: `message.value.decode('utf-8')`
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))