# Mini Jira

A small FastAPI project for learning backend development with SQLAlchemy and Alembic.

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Create a `.env` file:

```env
DATABASE_URL=sqlite:///./miniJira.db
```

Run database migrations:

```powershell
alembic upgrade head
```

Start the API:

```powershell
uvicorn main:app --reload
```

The app will be available at `http://127.0.0.1:8000`.
