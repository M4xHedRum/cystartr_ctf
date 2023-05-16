# Base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app files into the container
COPY app.py .
COPY /templates templates/
COPY /static static/
COPY /wsgi.py .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Run the Flask app using Gunicorn when the container starts
CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:5000"]
