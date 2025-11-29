FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

# Dependências básicas
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# JupyterLab
RUN pip install --no-cache-dir jupyterlab

WORKDIR /workspace

# Instala dependências do projeto
COPY requirements.txt /workspace/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888
