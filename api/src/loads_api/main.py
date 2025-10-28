"""FastAPI application definition for HappyRobot."""

from fastapi import FastAPI, HTTPException

from .supabase import SupabaseCredentialsError, get_supabase_client

app = FastAPI(title="HappyRobot API", version="0.1.0")


@app.get("/")
def read_root() -> dict[str, str]:
    """Simple welcome endpoint."""
    return {"message": "HappyRobot API is running"}


@app.get("/healthz")
def health_check() -> dict[str, str]:
    """Health probe used for uptime checks."""
    return {"status": "ok"}


@app.get("/projects")
async def list_projects() -> dict[str, list[dict]]:
    """Example endpoint that fetches data from Supabase."""
    try:
        supabase = get_supabase_client()
    except SupabaseCredentialsError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc

    response = supabase.table("projects").select("*").limit(50).execute()
    return {"items": response.data or []}
