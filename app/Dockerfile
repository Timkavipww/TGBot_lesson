FROM python:3.13.7-slim

WORKDIR /app

COPY app/requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY app app
COPY infrastructure infrastructure
COPY domain domain
COPY application application


# for don't create __pycache__ folders inside docker

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

CMD ["python", "-m", "app.main"]