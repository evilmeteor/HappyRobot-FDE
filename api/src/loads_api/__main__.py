"""Executable module that runs the development server."""

from uvicorn import run


def run_app() -> None:
    """Starts a reload-enabled development server."""
    run("loads_api.main:app", host="0.0.0.0", port=8000, reload=True)


def run() -> None:
    """Entry point exposed via `pyproject.toml` script name."""
    run_app()


if __name__ == "__main__":
    run_app()
