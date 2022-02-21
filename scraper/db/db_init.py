# Video: https://www.youtube.com/watch?v=rE_bJl2GAY8&ab_channel=TechWithTim
import os
import platform
from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson.objectid import ObjectId
import urllib.parse

if "alfred-linux-ubuntu" in str(platform.uname()):
    username = urllib.parse.quote_plus(os.getenv("MONGO_REMOTE_USERNAME"))
    password = urllib.parse.quote_plus(os.getenv("MONGO_REMOTE_PASSWORD"))

    # Access: https://cloud.mongodb.com/v2/61e5da26dc2df969bee3c620#clusters  => alfreds@atappon.com / google login
    cluster = f"mongodb+srv://{username}:{password}@cluster0.eoafk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    # cluster = "mongodb://localhost:27017"
else:
    cluster = (
        "mongodb://"
        + os.getenv("MONGODB_USERNAME")
        + ":"
        + os.getenv("MONGODB_PASSWORD")
        + "@"
        + os.getenv("MONGODB_HOSTNAME")
        + ":27017"
    )

client = MongoClient(cluster)

db = client.moodalarm
twitter_collection = db.tweeter
google_collection = db.google
reddit_collection = db.reddit
dailymotion_collection = db.dailymotion

# client = MongoClient()


def check_db_ready():
    try:
        # The ping command is cheap and does not require auth.
        client.admin.command("ping")
    except ConnectionFailure:
        raise "Server not available"


post1 = {"name": "dada", "content": "lorem ipsum sasasa kak"}
post2 = {"name": "era", "title": "lorem ipsum sasasa kak"}

twitter_collection.insert_one(post1)

# twitter_collection.insert_many([post1, post2])

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
