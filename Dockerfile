# Use an official Python runtime as a base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask is running on
EXPOSE 5000

# Set the entry point for the container
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]