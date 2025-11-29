# fastapi/main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="API Sífilis Congênita",
    description="Camada de ingestão/serviço para o projeto de ML.",
    version="0.1.0",
)

class DummyInput(BaseModel):
    AGE: int | None = None
    NUM_RES_HOUSEHOLD: int | None = None
    NUM_LIV_CHILDREN: int | None = None
    NUM_ABORTIONS: int | None = None
    NUM_PREGNANCIES: int | None = None

class DummyPrediction(BaseModel):
    message: str
    input: dict

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict", response_model=DummyPrediction)
def predict(payload: DummyInput):
    """
    Endpoint de predição MOCK.
    Depois a gente pluga o modelo real (best_model_rf.pkl).
    """
    return DummyPrediction(
        message="Modelo ainda não plugado. Esta é uma resposta de teste.",
        input=payload.dict()
    )
