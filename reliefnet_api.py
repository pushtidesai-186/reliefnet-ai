from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

needs_data = [
    {"id": 1, "area": "Surat", "need": "Food", "urgency": "High", "lat": 21.1702, "lng": 72.8311},
    {"id": 2, "area": "Navsari", "need": "Medical", "urgency": "Medium", "lat": 20.9467, "lng": 72.952},
    {"id": 3, "area": "Ahmedabad", "need": "Clothes", "urgency": "Low", "lat": 23.0225, "lng": 72.5714}
]

def predict(urgency):
    if urgency == "High":
        return "Immediate Assistance Required 🚨"
    elif urgency == "Medium":
        return "Support Needed Soon ⚠️"
    return "Stable Situation ✅"

@app.route("/")
def home():
    return "ReliefNet API Running 🚀"

@app.route("/api/data")
def get_data():
    return jsonify([
        {**item, "prediction": predict(item["urgency"])}
        for item in needs_data
    ])

@app.route("/api/add", methods=["POST"])
def add_data():
    new_item = request.json
    new_item["id"] = len(needs_data) + 1
    new_item["lat"] = 22.9734
    new_item["lng"] = 78.6569
    needs_data.append(new_item)
    return jsonify({"message": "Added successfully"})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)