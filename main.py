from fastapi import FastAPI, Depends
from app.db.deps import get_db
from app.models.user import User

from app.routes import user_route
from app.routes import project_route

app = FastAPI()
app.include_router(user_route.router)
app.include_router(project_route.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=5000)