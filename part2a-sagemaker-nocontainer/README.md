# Part 2a - Wine Quality Prediction (SageMaker without Containers)

## Description

This project trains a linear regression model to predict wine quality scores using AWS SageMaker *without* custom containers.

Used:
- Scikit-learn for model training
- SageMaker Studio Lab or SageMaker Notebook
- Native SageMaker functionality to deploy a model endpoint

---

## Files

- `wine_quality_notebook.ipynb` – Notebook that loads the dataset, trains the model, saves the `.pkl`, and optionally creates a `.tar.gz`.
- `wine_quality_model.pkl` – Trained model file
- `model.tar.gz` – (Optional) tar-gzipped model file for S3 upload
- `sample_prediction.py` – (Optional) simple script to query the deployed endpoint

---

## Deployment Info

If you deployed a SageMaker endpoint, include:

- **Endpoint Name**: `wine-quality-endpoint-<timestamp>`
- **Test Output**: Predicted wine quality for `[11.2, 0.28, 0.56, 1.9, 0.075, 17.0, 60.0, 0.998, 3.16, 0.58, 9.8]` was `5.1`

---

## Notes

- No containers or custom images were used.
- Deployed using built-in SageMaker sklearn image.