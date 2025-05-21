from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("wine_quality_model.pkl")

@app.route("/")
def home():
    return "Wine Quality Prediction API. Send a POST to /predict with your data."

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data
        data = request.get_json(force=True)

        # Extract the 11 features in order
        features = [
            data["fixed_acidity"],
            data["volatile_acidity"],
            data["citric_acid"],
            data["residual_sugar"],
            data["chlorides"],
            data["free_sulfur_dioxide"],
            data["total_sulfur_dioxide"],
            data["density"],
            data["pH"],
            data["sulfates"],
            data["alcohol"]
        ]

        # Convert to 2D array for model input
        prediction = model.predict([features])[0][0]

        return jsonify({
            "predicted_quality": round(prediction, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)