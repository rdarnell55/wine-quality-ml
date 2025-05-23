# Use an official Python runtime as a base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose 5000 (optional, for local Docker testing)
EXPOSE 5000

# Use shell form so Heroku’s $PORT is picked up at runtime
CMD gunicorn --bind 0.0.0.0:$PORT app:app