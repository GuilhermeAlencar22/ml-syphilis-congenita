# fastapi/main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from minio import Minio
from minio.error import S3Error
from typing import Optional
import os
import io

# =========================
# Configurações do MinIO
# =========================

MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "minio-syphilis:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ROOT_USER", "admin")
MINIO_SECRET_KEY = os.getenv("MINIO_ROOT_PASSWORD", "admin12345")
MINIO_BUCKET = os.getenv("MINIO_BUCKET", "syphilis-datasets")

minio_client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False,
)

# =========================
# App FastAPI
# =========================

app = FastAPI(
    title="API Sífilis Congênita",
    description="Camada de ingestão/serviço para o projeto de ML.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# Eventos de inicialização
# =========================

@app.on_event("startup")
def ensure_bucket_exists():
    try:
        if not minio_client.bucket_exists(MINIO_BUCKET):
            minio_client.make_bucket(MINIO_BUCKET)
            print(f"[MinIO] Bucket criado: {MINIO_BUCKET}")
        else:
            print(f"[MinIO] Bucket já existe: {MINIO_BUCKET}")
    except S3Error as e:
        print(f"[MinIO] Erro ao verificar/criar bucket: {e}")

# =========================
# Modelos
# =========================

class DummyInput(BaseModel):
    AGE: Optional[int] = None
    NUM_RES_HOUSEHOLD: Optional[int] = None
    NUM_LIV_CHILDREN: Optional[int] = None
    NUM_ABORTIONS: Optional[int] = None
    NUM_PREGNANCIES: Optional[int] = None

class DummyPrediction(BaseModel):
    message: str
    input: dict

# =========================
# Endpoints
# =========================

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "minio_endpoint": MINIO_ENDPOINT,
        "minio_bucket": MINIO_BUCKET,
    }

@app.post("/upload-dataset")
async def upload_dataset(
    file: UploadFile = File(...),
    folder: str = "raw",
):
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(status_code=400, detail="Apenas arquivos CSV são permitidos.")

    object_name = f"{folder}/{file.filename}"

    try:
        data = await file.read()
        file_size = len(data)

        if file_size == 0:
            raise HTTPException(status_code=400, detail="Arquivo vazio.")

        minio_client.put_object(
            bucket_name=MINIO_BUCKET,
            object_name=object_name,
            data=io.BytesIO(data),
            length=file_size,
            content_type="text/csv",
        )

        return {
            "message": "Upload realizado com sucesso.",
            "bucket": MINIO_BUCKET,
            "object_name": object_name,
            "size_bytes": file_size,
        }

    except S3Error as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao salvar no MinIO: {e}",
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro inesperado no upload: {e}",
        )

@app.post("/predict", response_model=DummyPrediction)
def predict(payload: DummyInput):
    return DummyPrediction(
        message="Modelo ainda não plugado. Esta é uma resposta de teste.",
        input=payload.dict(),
    )
