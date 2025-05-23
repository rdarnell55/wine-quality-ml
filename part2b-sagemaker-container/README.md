# Wine Quality Prediction (AWS SageMaker - Container Deployment)

This directory contains the Docker-based deployment for running the wine quality model on SageMaker using Bring Your Own Container (BYOC).

## Structure

- `Dockerfile`: Defines the container environment.
- `train.py`: Script to train the model inside the container.
- `serve.py` or `inference.py`: Custom handler for inference.
- `predictor.py`: Used in model loading and prediction.
- `model.tar.gz`: Contains the saved model and inference code.

## Steps

1. Build and test Docker image locally.
2. Push image to Amazon ECR.
3. Deploy image as a SageMaker model.
4. Create endpoint and test predictions.

## Requirements

- Docker and AWS CLI configured.
- SageMaker Execution Role with ECR and S3 access.