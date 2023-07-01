# Base image
FROM python:3.9-slim-buster

# Install Tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr

ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata

# Download Turkish language data
RUN apt-get install -y wget && \
    wget https://github.com/tesseract-ocr/tessdata/raw/main/tur.traineddata -P $TESSDATA_PREFIX

# Set working directory
WORKDIR /

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
