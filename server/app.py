from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from database import get_history, save_round
from predictor import predict_next_round
from streaks import analyze_streaks
from hash_decoder import decode_hash

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('admin.html')

@app.route('/api/history', methods=['GET'])
def history():
    return jsonify(get_history())

@app.route('/api/report', methods=['POST'])
def report():
    data = request.json
    decoded = decode_hash(data.get("hash"))
    save_round(data | decoded)
    return jsonify({"status": "ok"})

@app.route('/api/predict', methods=['GET'])
def predict():
    prediction = predict_next_round()
    return jsonify(prediction)

@app.route('/api/streaks', methods=['GET'])
def streaks():
    return jsonify(analyze_streaks())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
