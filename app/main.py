from app.infra.init_db import init_db
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="ProjectManagement API", version="1.0.0")


@app.on_event("startup")
def on_startup():
    init_db()


app.include_router(router)

