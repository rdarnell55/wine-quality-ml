import os
from sagemaker.predictor import Predictor
from sagemaker.serializers import JSONSerializer
from sagemaker.deserializers import JSONDeserializer
import pandas as pd

def get_predictor(endpoint_name: str = None) -> Predictor:
    """
    Return a SageMaker Predictor for the given endpoint name.
    If no endpoint_name is passed, will read from the ENDPOINT_NAME env var.
    """
    if endpoint_name is None:
        endpoint_name = os.environ.get("ENDPOINT_NAME")
        if endpoint_name is None:
            raise ValueError("Must pass endpoint_name or set ENDPOINT_NAME env var")
    return Predictor(
        endpoint_name=endpoint_name,
        serializer=JSONSerializer(),
        deserializer=JSONDeserializer()
    )

def predict_wine_quality(
    df: pd.DataFrame,
    predictor: Predictor = None
) -> list:
    """
    Given a DataFrame of wine features (one or more rows),
    calls the SageMaker endpoint and returns a list of predictions.
    """
    if predictor is None:
        predictor = get_predictor()
    payload = df.to_dict(orient="records")
    result = predictor.predict(payload)
    if isinstance(result, list) and result and isinstance(result[0], list):
        return [r[0] for r in result]
    return result








