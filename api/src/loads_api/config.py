"""Application configuration loading helpers."""

from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Loads configuration from environment, .env files, or other sources."""

    supabase_url: Optional[str] = None
    supabase_anon_key: Optional[str] = None

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    """Returns cached settings to avoid re-parsing on every request."""
    return Settings()
