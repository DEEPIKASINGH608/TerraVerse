import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "TerraVerse AI"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "TERRAVERSE_SECRET_KEY_SIH_2026_PRODUCTION_MODE_KEY_32"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 Days

    # Database Connection
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "terraverse_db")

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    # Directory Paths
    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    STORAGE_DIR: Path = BASE_DIR / "storage"
    RAW_STORAGE_DIR: Path = STORAGE_DIR / "raw"
    NORMALIZED_STORAGE_DIR: Path = STORAGE_DIR / "normalized"
    PROCESSED_STORAGE_DIR: Path = STORAGE_DIR / "processed"
    HARMONIZED_STORAGE_DIR: Path = STORAGE_DIR / "harmonized"

    
    TARGET_CRS: str = "EPSG:4326"
    DEFAULT_BUFFER_DISTANCE: float = 0.00005

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env", extra="ignore")

settings = Settings()

for directory in [
    settings.STORAGE_DIR,
    settings.RAW_STORAGE_DIR,
    settings.NORMALIZED_STORAGE_DIR,
    settings.PROCESSED_STORAGE_DIR,
    settings.HARMONIZED_STORAGE_DIR
]:
    directory.mkdir(parents=True, exist_ok=True)