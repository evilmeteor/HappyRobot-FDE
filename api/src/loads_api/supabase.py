"""Supabase client helpers."""

from functools import lru_cache

from supabase import Client, create_client

from .config import get_settings


class SupabaseCredentialsError(RuntimeError):
    """Raised when Supabase credentials are missing."""


@lru_cache
def get_supabase_client() -> Client:
    """Initialises a Supabase client using cached settings."""
    settings = get_settings()
    if not settings.supabase_url or not settings.supabase_anon_key:
        raise SupabaseCredentialsError("Supabase credentials are missing. Set SUPABASE_URL and SUPABASE_ANON_KEY.")
    return create_client(settings.supabase_url, settings.supabase_anon_key)
