from fastapi import FastAPI
from src.api import type_training

app = FastAPI(title="My Fitness API")

app.include_router(type_training.router)

@app.get("/", include_in_schema=False)
def read_root():
    return {"message": "¡Bienvenido a Mi API de Fitness!"}