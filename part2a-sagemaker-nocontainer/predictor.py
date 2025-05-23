# Predictor.py
import joblib
import os

def model_fn(model_dir):
    model_path = os.path.join(model_dir, "wine_quality_model.pkl")
    return joblib.load(model_path)

def predict_fn(input_data, model):
    return model.predict(input_data)