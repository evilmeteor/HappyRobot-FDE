# Happy Robot Forward Deployed Engineer Assessment Monorepo

This workspace hosts the two main HappyRobot applications:

- `api/` – FastAPI backend that talks to Supabase.
- `dashboard/` – SolidJS dashboard built with Vite.

Both projects are intentionally lightweight scaffolds so the team can start wiring features immediately.

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+ and npm

### Backend (FastAPI)

```bash
cd api
python -m venv .venv
source .venv/bin/activate
pip install -e .
cp .env.example .env  # update Supabase credentials
uvicorn happyrobot_api.main:app --reload
```

Visit `http://localhost:8000/docs` for interactive API docs. The `/projects` endpoint currently demonstrates Supabase access.

### Dashboard (SolidJS)

```bash
cd dashboard
npm install
npm run dev
```

The app is available at `http://localhost:5173`. Replace the placeholder counter component with your dashboard widgets as the API evolves.

## Repo Scripts

| Area      | Command (from project dir)             | Purpose               |
|-----------|----------------------------------------|-----------------------|
| Backend   | `dev-server` (via `python -m happyrobot_api`) | Run FastAPI dev server |
| Dashboard | `npm run build`                        | Build production bundle |
| Dashboard | `npm run lint`                         | Run ESLint on the UI   |

## Conventions

- Use `.env` files for local secrets; never commit them.
- API code lives under `api/src`.
- Dashboard components live under `dashboard/src`.
- Keep shared documentation in this README unless a project-specific guide is required.
