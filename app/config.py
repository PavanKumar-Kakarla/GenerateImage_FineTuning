from pathlib import Path
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    REPLICATE_API_KEY: str

    class Config:
        env_file = Path(__file__).resolve().parent.parent / ".env" 

settings = Settings()