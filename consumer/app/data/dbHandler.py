from pymongo import MongoClient

class DbHandler:
    client = MongoClient("localhost:27017")
    def __init__(self):
        self.db = self.client["changestream"]
        self.collection = self.db["emojicount"]

    def increment(self, topic, emoji):
        print("incrementing " + emoji)
        try:
            self.collection.update_one(
                {"topic": topic},
                {"$inc":{emoji: 1}},
                upsert=False
            )
        except Exception as e:
            print("Error incrementing " + emoji)