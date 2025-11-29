FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

# Diretório base da aplicação
WORKDIR /app

# Instala dependências compartilhadas do projeto
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da API FastAPI
COPY fastapi /app/fastapi

# Trabalhar dentro da pasta da API
WORKDIR /app/fastapi

EXPOSE 8000

# Comando padrão (o docker-compose também define command, mas não tem problema)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
