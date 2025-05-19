# Backend (FastAPI)

This folder contains the FastAPI backend for InsightLens.

## Setup
1. Create a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

## Structure
- `main.py` - FastAPI entrypoint
- `api/` - API routes
- `services/` - Business logic and AI integration
- `models/` - Pydantic models
- `db/` - Database models and connection
- `tasks/` - Celery tasks for async processing
