# HappyRobot API

FastAPI service that powers the HappyRobot platform. The service exposes REST endpoints and connects to Supabase for persistence.

## Local development

1. Create a Python virtual environment (3.10+ is recommended).
2. Install dependencies:

   ```bash
   pip install -e . 
   ```

3. Create an `.env` file using `.env.example` as a reference.
4. Run the development server:

   ```bash
   uvicorn loads_api.main:app --reload
   ```

The `dev-server` script declared in `pyproject.toml` is also available:

```bash
python -m loads_api
```

## Environment variables

- `SUPABASE_URL` – Supabase Project URL.
- `SUPABASE_ANON_KEY` – Supabase anon/public API key with access to the required tables.

The service uses [`pydantic-settings`](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) so the variables can be provided via `.env` file, shell environment, or any Pydantic-supported source.
