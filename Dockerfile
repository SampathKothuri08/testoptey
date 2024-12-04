# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev-compat \
    libmariadb-dev \
    gcc \
    python3-dev \
    musl-dev \
    libglib2.0-0 \
    libgl1-mesa-glx \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your application will run on
EXPOSE 8000

# Specify the default command to run your application
CMD ["gunicorn", "-b", "0.0.0.0:8000", "edunet_site.wsgi:application"]

