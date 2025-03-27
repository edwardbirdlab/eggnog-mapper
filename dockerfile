FROM python:3.9-slim

# Set environment variables for eggNOG-mapper and data directory
ENV EGGNOG_DIR=/opt/eggnog-mapper \
    EGGNOG_DATA_DIR=/opt/eggnog-mapper-data \
    PATH="/opt/eggnog-mapper:/opt/eggnog-mapper/eggnogmapper/bin:$PATH"

# Install required system packages
RUN apt-get update && apt-get install -y \
    tar \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Copy the repository (assuming this Dockerfile is at the repo root)
COPY . $EGGNOG_DIR

WORKDIR $EGGNOG_DIR

# Upgrade setuptools to avoid the psutil error, then install using setup.py
RUN pip install --upgrade setuptools && python setup.py install

# Set the default working directory at runtime
WORKDIR /data

# Use emapper.py as the container's entrypoint
ENTRYPOINT ["emapper.py"]
