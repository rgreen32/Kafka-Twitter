from pymongo import MongoClient, UpdateOne

class DbHandler:
    client = MongoClient("localhost:27017")
    def __init__(self):
        self.db = self.client["local"]
        self.collection = self.db["emojicounts"]

    def increment(self, topic, emoji):
        self.collection.update_one(
            {"topic": topic},
            {"$inc":{emoji: 1}}
        )