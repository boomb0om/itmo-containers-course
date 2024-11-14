FROM python:3.12-slim

WORKDIR /app

COPY migrate.py /app/migrate.py
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python3", "migrate.py"]