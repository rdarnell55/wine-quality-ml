# Part 2b: AWS SageMaker with Container

This part of the project demonstrates how to deploy a machine learning model to AWS SageMaker **using a custom container**. Unlike Part 2a, this approach allows for full control over the serving logic and dependencies by defining a container image.

## Overview

- **Model Used:** Linear Regression (`sklearn.linear_model.LinearRegression`)
- **Framework:** Scikit-learn (within a Flask app in Docker)
- **Deployment Method:** SageMaker with custom container image hosted on Amazon ECR
- The **Custom container** includes Flask-based logic for inference. The image was built using  AWS CodeBuild (with a buildspec.yml) a  Docker build and pushed to ECR with a v2, schema-2 manifest to satisfy SageMaker requirements.

---
## Model Description

The deployed model is a **Linear Regression** model trained to predict wine quality scores based on physicochemical features from the UCI Wine Quality dataset. The model is serialized with `joblib`, baked into a Docker image, and deployed using SageMaker's hosting services.

The container includes a simple Flask application that handles inference requests at `/invocations`.

## Endpoint Information

- **SageMaker Endpoint Name:** `wine-quality-endpoint-1748125390`
- **Model Artifact:** `wine_quality_model.pkl`
- **Deployment Notebook:** `wine_deploy_container.ipynb`

---
## Project Structure

| File | Description |
|------|-------------|
| `Dockerfile` | Defines the environment and entrypoint for the model container |
| `serve` / `serve.py` | Entrypoint Flask app used by SageMaker to serve predictions |
| `predictor.py` | Python script/module to call the deployed endpoint |
| `requirements.txt` | Required packages for the Flask app |
| `wine_quality_model.pkl` | Serialized trained model |
| `wine_deploy_container.ipynb` | Jupyter notebook that builds, pushes, and deploys the container |
| `README.md` | This documentation file |


## The Endpoint is tested inline and shown in: `wine_deploy_sagemaker_sdk.ipynb` 

## Repository

- **Main project repository:** [https://github.com/rdarnell55/wine-quality-ml](https://github.com/rdarnell55/wine-quality-ml)
- **Part 2b repository folder:** [`part2b-sagemaker-container`](https://github.com/rdarnell55/wine-quality-ml/tree/main/part2b-sagemaker-container)