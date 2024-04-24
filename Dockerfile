# Use the official Python image as a parent image
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install NLTK and download stopwords
RUN pip install --no-cache-dir nltk && \
    python -m nltk.downloader stopwords

# Run the Python script when the container launches
CMD ["python", "./removing_stopwords_app.py"]