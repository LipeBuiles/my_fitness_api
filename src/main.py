import sentry_sdk
from fastapi import FastAPI
from core.config import settings
from src.api import (
    type_training,
    users,
    health,
    training,
    cadence,
    dream,
    heart_rate,
    objetives_day,
    pace,
    pace_for_km,
    stride_cm
)

# Inicializar Sentry
if settings.SENTRY_API_KEY:
    sentry_sdk.init(
        dsn=settings.SENTRY_API_KEY,
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
    )

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

app.include_router(type_training.router)
app.include_router(users.router)
app.include_router(health.router)
app.include_router(training.router)
app.include_router(cadence.router)
app.include_router(dream.router)
app.include_router(heart_rate.router)
app.include_router(objetives_day.router)
app.include_router(pace.router)
app.include_router(pace_for_km.router)
app.include_router(stride_cm.router)

@app.get("/", include_in_schema=False)
def read_root():
    return {"message": "¡Bienvenido a Mi API de Fitness!"}

