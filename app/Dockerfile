FROM python:3.13.7-slim

WORKDIR /app

COPY app/requirements.txt /tmp/requirements_app.txt
COPY shared/requirements.txt /tmp/requirements_shared.txt
COPY infrastructure/requirements.txt /tmp/requirements_infrastructure.txt

RUN pip install --no-cache-dir -r /tmp/requirements_app.txt
RUN pip install --no-cache-dir -r /tmp/requirements_shared.txt
RUN pip install --no-cache-dir -r /tmp/requirements_infrastructure.txt

COPY app app
COPY shared shared
COPY infrastructure infrastructure

# for don't create __pycache__ folders inside docker

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/app

CMD ["python", "-m", "app.main"]