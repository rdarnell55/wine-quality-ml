from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("wine_quality_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Grab form values
        features = [float(request.form.get(f)) for f in [
            "fixed_acidity", "volatile_acidity", "citric_acid",
            "residual_sugar", "chlorides", "free_sulfur_dioxide",
            "total_sulfur_dioxide", "density", "pH", "sulfates", "alcohol"
        ]]
        prediction = model.predict([features])[0]
        return render_template("result.html", prediction=round(prediction, 2))
    except:
        return "Something went wrong. Please check your input. And your life choices."

if __name__ == "__main__":
    app.run(debug=True)