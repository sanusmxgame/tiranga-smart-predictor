import os, json
from pymongo import MongoClient

USE_MONGO = os.environ.get("mongodb+srv://tirangaUser:yourStrongPassword123@cluster0.xep0rbi.mongodb.net/tiranga") is not None
if USE_MONGO:
    client = MongoClient(os.environ["mongodb+srv://tirangaUser:yourStrongPassword123@cluster0.xep0rbi.mongodb.net/tiranga"])
    db = client["tiranga"]
    coll = db["history"]
else:
    JSON_PATH = "history.json"
    if not os.path.exists(JSON_PATH):
        with open(JSON_PATH, 'w') as f: json.dump([], f)

def save_round(round_data):
    if USE_MONGO:
        coll.insert_one(round_data)
    else:
        with open(JSON_PATH, 'r+') as f:
            data = json.load(f)
            data.append(round_data)
            f.seek(0)
            json.dump(data[-100:], f)

def get_history():
    if USE_MONGO:
        return list(coll.find({}, {"_id": 0}))[-100:]
    else:
        with open(JSON_PATH) as f:
            return json.load(f)
