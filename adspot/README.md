# AdSpot — beginner React + Django + SQLite project

A small learning project that displays sample advertisements. React renders the page, Django provides a JSON API, and SQLite stores the advertisements. Docker Compose starts the frontend and backend together.

## Requirements
- Docker Desktop installed and running
- Docker Compose available (`docker compose version`)

## Run it
From this folder, run:

```bash
docker compose up --build
```

Open:
- Frontend: http://localhost:5173
- API: http://localhost:8000/api/ads/
- Django health check: http://localhost:8000/api/health/

Stop with `Ctrl+C`, then optionally run `docker compose down`.

The SQLite database is stored in the Docker named volume `adspot_db`, so it persists when containers are recreated. To remove the database too, run `docker compose down -v` (this deletes the saved database data).

## Folder guide
- `frontend/`: React UI built with Vite
- `backend/`: Django API and SQLite database model
- `compose.yaml`: starts both services

## Learning notes
- The frontend requests data from Django at `http://localhost:8000/api/ads/`.
- The backend returns JSON; it does not serve the React page.
- The `seed_ads` command inserts three sample ads only when the database is empty.
- This is a local learning setup, not production deployment. Before publishing online, configure production settings, secure allowed hosts/CORS, use a production server, and decide whether SQLite is appropriate for the expected traffic.
