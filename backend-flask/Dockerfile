# Use the official Ubuntu image from the Docker Hub
FROM ubuntu:22.04

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt .

# Install system dependencies including mysql-server
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    mysql-server \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install the dependencies specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables
ENV MYSQL_HOST=172.22.0.2
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=
ENV MYSQL_DB=flaskapp

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define the command to run the application
CMD ["python3", "backend.py"]
