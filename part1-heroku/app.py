from flask import Flask, request, render_template
import joblib
import os
import traceback

app = Flask(__name__)

# Load model
model_path = os.path.join(os.path.dirname(__file__), 'wine_quality_model.pkl')
model = joblib.load(model_path)

# Map form-friendly snake_case to model-required labels
key_map = {
    "fixed_acidity": "fixed acidity",
    "volatile_acidity": "volatile acidity",
    "citric_acid": "citric acid",
    "residual_sugar": "residual sugar",
    "chlorides": "chlorides",
    "free_sulfur_dioxide": "free sulfur dioxide",
    "total_sulfur_dioxide": "total sulfur dioxide",
    "density": "density",
    "pH": "pH",
    "sulfates": "sulfates",
    "alcohol": "alcohol"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form_data = request.form
        print("💡 Raw form data:", form_data)

        input_data = {key_map[k]: float(v) for k, v in form_data.items()}
        print("🔧 Formatted input for model:", input_data)

        features = [input_data[k] for k in key_map.values()]
        print("🚀 Feature list for prediction:", features)

        prediction = model.predict([features])
        quality = round(float(prediction[0]), 2)
        print("🍷 Predicted quality:", quality)

        return render_template('index.html', prediction=f'Predicted wine quality: {quality}')
    
    except Exception as e:
        print("🔥 Prediction error:", str(e))
        return render_template('index.html', prediction="Something went wrong. Please check your input. And your life choices.")

if __name__ == '__main__':
    app.run(debug=True)