FROM python:3.9-slim

ENV EGGNOG_DIR=/opt/eggnog-mapper \
    PATH="/opt:/opt/eggnogmapper/bin:$PATH"

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    tar \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt
COPY . .
RUN pip install -r requirements.txt

WORKDIR /data

CMD ["emapper.py"]
