# Inherit from a base image
FROM python:3.12-slim

# Setting working directory
WORKDIR /app

# Update pip version
RUN pip install --upgrade pip

# Copy requirements.txt to the container
COPY requirements.txt requirements.txt

# Install packages
RUN pip install -r requirements.txt

# Copy the rest of the project
COPY . .

# Run project
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]