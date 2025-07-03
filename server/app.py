from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
import requests, hashlib, time
from datetime import datetime
from utils import parse_json_results, predict_next_result

app = Flask(__name__)
CORS(app)

MONGO_URI = "mongodb+srv://tirangaUser:yourStrongPassword123@cluster0.xep0rbi.mongodb.net/tiranga"
client = MongoClient(MONGO_URI)
db = client['tiranga']

MODES = ["WinGo_30S", "WinGo_1M", "WinGo_3M", "WinGo_5M"]

@app.route("/api/results/<mode>")
def get_results(mode):
    if mode not in MODES:
        return jsonify({"error": "Invalid mode"}), 400
    url = f"https://draw.ar-lottery01.com/WinGo/{mode}.json?ts={int(time.time()*1000)}"
    try:
        res = requests.get(url)
        raw_json = res.json()
        parsed = parse_json_results(raw_json)
        db[mode].insert_many(parsed)
        return jsonify(parsed)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/api/predict/<mode>")
def predict(mode):
    if mode not in MODES:
        return jsonify({"error": "Invalid mode"}), 400
    history = list(db[mode].find().sort("period", -1).limit(100))
    prediction = predict_next_result(history)
    return jsonify(prediction)

@app.route("/static/popup.js")
def serve_popup():
    return send_from_directory("static", "popup.js")

@app.route("/")
def home():
    return jsonify({"message": "Tiranga Smart Predictor API"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
