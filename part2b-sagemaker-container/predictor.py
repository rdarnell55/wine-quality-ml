import joblib
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)
model = joblib.load("wine_quality_model.pkl")

@app.route("/ping", methods=["GET"])
def ping():
    return "Model is ready!", 200

@app.route("/invocations", methods=["POST"])
def predict():
    input_data = request.get_json()
    features = pd.DataFrame(input_data)
    predictions = model.predict(features)
    return jsonify(predictions.tolist())