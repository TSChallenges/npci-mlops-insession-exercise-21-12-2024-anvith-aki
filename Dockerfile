# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt ./
COPY app/ ./app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Gradio
EXPOSE 7860

# Command to run the app
CMD ["python", "app/main.py"]
