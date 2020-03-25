from pymongo import MongoClient
from bson.json_util import dumps

client = MongoClient("localhost:27017")

# print(client.changestream.collections.insert_one({"hello": "world"}).inserted_id)

change_stream = client.changestream.collections.watch()

# for change in change_stream:
#     print(dumps(change))
#     print('') # for readability only