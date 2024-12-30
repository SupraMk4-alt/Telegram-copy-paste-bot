# Use the official Python image as the base image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port if the application uses one (modify if necessary)
EXPOSE 8080

# Define the command to run the application (adjust if necessary)
CMD ["python", "main.py"]
