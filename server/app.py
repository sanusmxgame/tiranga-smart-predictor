from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pymongo import MongoClient
from utils import analyze_and_predict
import os
import datetime

app = Flask(__name__)
CORS(app)

# MongoDB setup
MONGO_URI = "mongodb+srv://tirangaUser:yourStrongPassword123@cluster0.xep0rbi.mongodb.net/tiranga"
client = MongoClient(MONGO_URI)
db = client["tiranga"]
collection = db["results"]

@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.json
    try:
        last_results = data.get("results", [])
        prediction = analyze_and_predict(last_results)

        # Store result
        collection.insert_one({
            "timestamp": datetime.datetime.utcnow(),
            "input": last_results,
            "prediction": prediction
        })
        return jsonify(prediction)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/history", methods=["GET"])
def history():
    try:
        records = list(collection.find().sort("timestamp", -1).limit(100))
        for r in records:
            r["_id"] = str(r["_id"])
        return jsonify(records)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/static/popup.js")
def popup_js():
    return send_from_directory("static", "popup.js")

@app.route("/")
def home():
    return "Tiranga Smart Predictor Running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
