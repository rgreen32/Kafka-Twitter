import requests
import json
from requests_oauthlib import OAuth1
import os

class Streamer():
    url = "https://stream.twitter.com/1.1/statuses/filter.json"
    session = requests.Session()
    auth = OAuth1(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_KEY_SECRET"),
                    os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
    def __init__(self):
        self.conn = self.session.post(self.url, data={'track': 'requests'}, auth=self.auth, stream=True)
        self.start_main_loop()
    def start_main_loop(self):
        print(self.conn.status_code)
        for line in self.conn.iter_lines():
            if line: # filter out keep-alive new lines
                print(json.loads(line))
