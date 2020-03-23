import requests
import json
from requests_oauthlib import OAuth1
import os


class Streamer():
    url = "https://stream.twitter.com/1.1/statuses/filter.json"
    session = requests.Session()
    auth = OAuth1(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_KEY_SECRET"),
                    os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
    # def __init__(self, topic):
    #     self.conn = self.session.post(self.url, data={'track': topic}, auth=self.auth, stream=True)
        
    def get_stream(self, topic):
        conn = self.session.post(self.url, data={'track': topic}, auth=self.auth, stream=True)
        print(conn.status_code)
        for line in conn.iter_lines():
            if line: # filter out keep-alive new lines
                response = json.loads(line)
                if "text" in response:
                    print(json.loads(line)["text"])
                    yield json.loads(line)["text"]
