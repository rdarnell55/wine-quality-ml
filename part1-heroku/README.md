# Wine Quality Prediction App (Heroku Deployment)

This folder contains the Flask web app for predicting wine quality using a linear regression model.

## Contents

- `app.py`: Flask app to serve the ML model.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Docker configuration for containerized deployment.
- `Procfile`: Tells Heroku how to run the app.
- `.dockerignore`: Keeps build context clean.
- `wine_quality_model.pkl`: The trained model.

## Deployment Instructions

1. Ensure Docker and Heroku CLI are installed.
2. Log in to Heroku container registry:
   ```bash
   heroku container:login