FROM python:3.10-slim

RUN pip install --no-cache-dir flask scikit-learn pandas joblib

WORKDIR /opt/program
COPY . .

ENV PYTHONUNBUFFERED=TRUE
ENTRYPOINT ["python3"]
CMD ["serve.py"]