from fastapi import FastAPI
from src.api import (
    type_training,
    users,
    health,
    training,
    cadence,
    dream,
    heart_rate,
    objetives_day
)

app = FastAPI(title="My Fitness API")

app.include_router(type_training.router)
app.include_router(users.router)
app.include_router(health.router)
app.include_router(training.router)
app.include_router(cadence.router)
app.include_router(dream.router)
app.include_router(heart_rate.router)
app.include_router(objetives_day.router)

@app.get("/", include_in_schema=False)
def read_root():
    return {"message": "¡Bienvenido a Mi API de Fitness!"}

