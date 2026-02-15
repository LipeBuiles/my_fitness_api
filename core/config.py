from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "My Fitness API"
    PROJECT_VERSION: str = "1.0.0"
    DATABASE_URL: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore")
    
try:
    settings = Settings()
except Exception as e:
    print(f"Error loading settings: {e}")
    raise