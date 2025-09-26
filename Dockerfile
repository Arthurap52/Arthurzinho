FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    make \
    libc-dev \
    libc6-dev \
    libffi-dev \
    libssl-dev \
    python3-dev \
    pkg-config \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip wheel setuptools \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
