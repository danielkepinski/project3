FROM python:3.12-slim

# Install dependencies including netcat
RUN apt-get update && apt-get install -y netcat-openbsd gcc libpq-dev && \
    pip install --upgrade pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
