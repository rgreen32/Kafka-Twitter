from pymongo import MongoClient
from app.data import DbHandler


handler = DbHandler()
collection = handler.collection
change_stream = collection.watch()

while(True):
    try:
        for change in change_stream:

            twittertopic = handler.topics.get(change["documentKey"]["_id"])
            emojicount = {"twittertopic": twittertopic, "emoji": list(change["updateDescription"]["updatedFields"].keys())[0], "count": list(change["updateDescription"]["updatedFields"].values())[0]}
            print(emojicount)
            # emojicount
    except Exception as e:
        print(e)