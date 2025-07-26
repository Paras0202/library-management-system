from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    DB_USER: str
    DB_PASS: str = Field(alias="DB_PASSWORD")
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
print("✅ DB Loaded:", settings.DB_USER, settings.DB_PASS)
