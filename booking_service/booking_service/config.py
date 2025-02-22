from pydantic_settings import BaseSettings, SettingsConfigDict

from pathlib import Path

PROJECT_DIR = Path(__file__).absolute().parent.parent.parent

class EnvBaseSettings(BaseSettings):
    #model_config = SettingsConfigDict(env_file=PROJECT_DIR.joinpath('.env'), env_file_encoding="utf-8", extra="ignore")
    class Config:
        env_file = ".env"


class DjangoSettings(EnvBaseSettings):
    DJANGO_SECRET: str
    DJANGO_DEBUG: bool

class PostgreSettings(EnvBaseSettings):
    DB_HOST: str
    DB_PORT: int = 5432
    DB_USER: str
    DB_PASS: str
    DB_NAME: str


class Settings(DjangoSettings, PostgreSettings):
    pass

settings = Settings()
