# Part 2a: AWS SageMaker (No Container)

This part of the project demonstrates how to train and deploy a machine learning model using AWS SageMaker **without custom containerization**. The model is trained locally and then deployed using SageMaker's built-in hosting capabilities.

## Overview

- **Model Used:** Linear Regression (`sklearn.linear_model.LinearRegression`)
- **Framework:** Scikit-learn
- **Deployment Method:** SageMaker SDK, no container customization
- **Repository Folder:** [`part2a-sagemaker-nocontainer`](https://github.com/rdarnell55/wine-quality-ml/tree/main/part2a-sagemaker-nocontainer)


## Model Description

The model used is a **Linear Regression** model trained to predict wine quality scores based on physicochemical features from the UCI Wine Quality dataset. The model is serialized using `joblib` and uploaded to SageMaker, where it is deployed as a REST API endpoint.

## Endpoint Information

- **SageMaker Endpoint Name:** `wine-quality-endpoint-1748042764`
- **Model Artifact:** `wine_quality_model.pkl`
- **Deployment Script:** `wine_deploy_sagemaker_sdk.ipynb`

The endpoint accepts POST requests with input data in JSON format and returns the predicted wine quality.

---

## Project Structure

| File | Description |
|------|-------------|
| `train_wine_model.ipynb` | Notebook used to preprocess the dataset and train the linear regression model |
| `wine_quality_model.pkl` | Serialized model file saved using `joblib` |
| `model.tar.gz` | Tarball containing the model for SageMaker deployment |
| `predictor.py` | Python module to send requests to the SageMaker endpoint |
| `wine_deploy_sagemaker_sdk.ipynb` | Notebook that creates and tests the deployed model on SageMaker |
| `README.md` | This documentation file |

---

## The Endpoint is tested inline and shown in: `wine_deploy_sagemaker_sdk.ipynb` 

## Repository

- **Main project repository:** [https://github.com/rdarnell55/wine-quality-ml](https://github.com/rdarnell55/wine-quality-ml)
- **Part 2a repository folder:** [`part2a-sagemaker-nocontainer`](https://github.com/rdarnell55/wine-quality-ml/tree/main/part2a-sagemaker-nocontainer)