### part2-sagemaker/README.md` (create this folder if not already)
```markdown
# Wine Quality Prediction (AWS SageMaker - Native Deployment)

This directory contains the code for training and deploying a linear regression model using AWS SageMaker **without** containerization.

## Contents

- `wine_quality_sagemaker.ipynb`: Notebook used for training, evaluation, and deploying via SKLearnModel.
- `predictor.py`: Custom inference script required by SageMaker.
- `model.tar.gz`: Serialized model + script, uploaded to S3 for deployment.

## Deployment Steps

1. Upload `model.tar.gz` to S3.
2. Use SKLearnModel to create a model and deploy it as an endpoint.
3. Use the endpoint to make predictions via SageMaker runtime.

## Highlights

- Uses SageMaker SDK for training and real-time deployment.
- Model is deployed without Docker.