import requests
import os
from app.core import Streamer, Producer

consumer_key = os.getenv("CONSUMER_KEY")
consumer_key_secret = os.getenv("CONSUMER_KEY_SECRET")

access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# streamer = Streamer()

producer = Producer()

producer.start_producer_loop("coronavirus")


