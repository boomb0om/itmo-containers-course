FROM python:3.12-slim

WORKDIR /app

VOLUME /app/some_data

ARG PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=on

RUN apt-get update && apt-get install -y gcc
RUN python -m pip install --upgrade --no-cache-dir pip

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . ./

ENV PYTHONPATH="${PYTHONPATH}:/code/"

CMD ["uvicorn", "demo_service.api:app", "--port", "8080", "--host", "0.0.0.0"]