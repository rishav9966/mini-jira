from fastapi import FastAPI, Depends
from app.db.deps import get_db
from app.models.user import User

from app.routes import users
from app.routes import projects

app = FastAPI()
app.include_router(users.router)
app.include_router(projects.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)