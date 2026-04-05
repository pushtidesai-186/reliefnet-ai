from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Dummy disaster data (AI-ready structure)
data_store = [
    {
        "id": 1,
        "area": "Surat",
        "lat": 21.1702,
        "lng": 72.8311,
        "need": "Food",
        "urgency": "High"
    },
    {
        "id": 2,
        "area": "Navsari",
        "lat": 20.9467,
        "lng": 72.9520,
        "need": "Medical",
        "urgency": "Medium"
    },
    {
        "id": 3,
        "area": "Ahmedabad",
        "lat": 23.0225,
        "lng": 72.5714,
        "need": "Clothes",
        "urgency": "Low"
    }
]

# 🔮 AI Prediction Logic (simple rule-based)
def predict(urgency):
    if urgency == "High":
        return "Immediate Assistance Required 🚨"
    elif urgency == "Medium":
        return "Support Needed Soon ⚠️"
    else:
        return "Stable Situation ✅"

# 🏠 Home Route (for testing)
@app.route("/")
def home():
    return "ReliefNet API Running 🚀"

# 📊 Get all data
@app.route("/api/data", methods=["GET"])
def get_data():
    enriched_data = []

    for item in data_store:
        item_copy = item.copy()
        item_copy["prediction"] = predict(item["urgency"])
        enriched_data.append(item_copy)

    return jsonify(enriched_data)

# ➕ Add new data
@app.route("/api/add", methods=["POST"])
def add_data():
    new_item = request.json
    new_item["id"] = len(data_store) + 1
    data_store.append(new_item)

    return jsonify({
        "message": "Data added successfully ✅",
        "data": new_item
    })

# 🚀 Run server (Railway compatible)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)