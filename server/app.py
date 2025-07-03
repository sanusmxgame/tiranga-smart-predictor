from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
import requests
import hashlib
import time
from threading import Thread

app = Flask(__name__, static_folder="static")  # Flask will now serve static files from the "static" folder
CORS(app)

MONGO_URI = "mongodb+srv://tirangaUser:yourStrongPassword123@cluster0.xep0rbi.mongodb.net/tiranga"
client = MongoClient(MONGO_URI)
db = client["tiranga"]
collection = db["results"]

DATA_URLS = {
    "30S": "https://draw.ar-lottery01.com/WinGo/WinGo_30S.json",
    "1M":  "https://draw.ar-lottery01.com/WinGo/WinGo_1M.json",
    "3M":  "https://draw.ar-lottery01.com/WinGo/WinGo_3M.json",
    "5M":  "https://draw.ar-lottery01.com/WinGo/WinGo_5M.json"
}

# Other functions remain unchanged


def extract_result(entry):
    num = int(entry["number"])
    color = "green" if num == 0 else "red" if num % 2 else "purple"
    size = "big" if num >= 5 else "small"
    return {
        "period": entry["period"],
        "number": num,
        "color": color,
        "size": size,
        "time": entry["time"]
    }

def fetch_all_results():
    all_data = {}
    for label, url in DATA_URLS.items():
        try:
            resp = requests.get(url)
            json_data = resp.json()
            results = [extract_result(entry) for entry in json_data[:100]]
            all_data[label] = results
            # Save to MongoDB
            for result in results:
                result["_source"] = label
                collection.update_one(
                    {"period": result["period"], "_source": label},
                    {"$set": result},
                    upsert=True
                )
        except Exception as e:
            print(f"Error fetching {label}: {e}")
    return all_data

@app.route("/api/results")
def get_results():
    return jsonify(fetch_all_results())

@app.route("/static/popup.js")
def serve_popup():
    return send_from_directory("static", "popup.js")

if __name__ == "__main__":
    # Start WebSocket sniffer in a separate thread
    Thread(target=capture_websocket, daemon=True).start()
    app.run(host="0.0.0.0", port=8080)
