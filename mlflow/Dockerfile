FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN pip install --no-cache-dir mlflow

WORKDIR /mlflow
VOLUME ["/mlruns"]

EXPOSE 5000
