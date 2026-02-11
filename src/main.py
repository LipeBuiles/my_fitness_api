from fastapi import FastAPI
from src.api import (
    type_training,
    users,
    health,
    training,
    cadence
)

app = FastAPI(title="My Fitness API")

app.include_router(type_training.router)
app.include_router(users.router)
app.include_router(health.router)
app.include_router(training.router)
app.include_router(cadence.router)

@app.get("/", include_in_schema=False)
def read_root():
    return {"message": "¡Bienvenido a Mi API de Fitness!"}

