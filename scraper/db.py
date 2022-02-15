# Video: https://www.youtube.com/watch?v=rE_bJl2GAY8&ab_channel=TechWithTim

from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

import time
from bson.objectid import ObjectId

cluster = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
client = MongoClient(cluster)

db = client.moodalarm
twitter_collection = db.tweeter

client = MongoClient()


def check_db_ready():
    try:
        # The ping command is cheap and does not require auth.
        client.admin.command("ping")
    except ConnectionFailure:
        raise "Server not available"


post1 = {"_id": 3, "name": "dada", "content": "lorem ipsum sasasa kak"}
post2 = {"_id": 4, "name": "era", "title": "lorem ipsum sasasa kak"}

# collection.insert_one(post1)

# collection.insert_many([post1, post2])

# result = twitter_collection.find({"name": "gaga"})
# print(f"{[x for x in result]}")

# certain_date = datetime.datetime.now()
# collection.find({"date": {"$gt": certain_date }}).sort("name") # gt = greater than, lt = less than

# mode query operators at: https://docs.mongodb.com/manual/reference/operator/query/

# result = twitter_collection.find({"title": {"$regex": "^lorem"}})
# print(f"{[x for x in result]=}")

# collection.delete_many({})

# collection.update_one({"_id": 3}, {"$set": {"name": "pupu"}})


# doc_count = collection.count_documents({"name": "pupu"})
# doc_count = twitter_collection.count_documents({})  # count all docs
# print(doc_count)

# If you need to call the IDs that mongo supplyes
# result = collection.find_one({"_id": ObjectId("2348573934534ffdf")})
