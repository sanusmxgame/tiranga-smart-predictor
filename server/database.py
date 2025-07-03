import os, json
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://tirangaUser:yourStrongPassword123@cluster0.xep0rbi.mongodb.net/tiranga")
client = MongoClient(MONGO_URI)
db = client["tiranga"]
collection = db["results"]

def save_round(round_data):
    collection.update_one(
        {"period": round_data["period"], "_source": round_data["_source"]},
        {"$set": round_data},
        upsert=True
    )

def get_history():
    return list(collection.find({}, {"_id": 0}))[-100:]
