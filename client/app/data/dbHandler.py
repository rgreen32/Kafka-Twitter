from pymongo import MongoClient

class DbHandler:
    client = MongoClient("localhost:27017")
    db = client["changestream"]
    collection = db["emojicount"]
    def __init__(self):
        self.get_twitter_topics()
        # self.db = self.client["changestream"]
        # self.collection = self.db["emojicount"]

    def get_twitter_topics(self):
        documents = self.collection.find()
        topics = {} 
        for document in documents:
            topics[document["_id"]] = document["topic"]
        self.topics = topics

     