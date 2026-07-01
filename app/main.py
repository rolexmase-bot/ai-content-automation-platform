from fastapi import FastAPI

from app.api.content import router as content_router
from app.api.history import router as history_router
from app.api.web import router as web_router
from app.api.n8n import router as n8n_router

from app.database.db import Base, engine
import app.models.article  

app = FastAPI()

app.include_router(content_router)
app.include_router(history_router)
app.include_router(web_router)
app.include_router(n8n_router)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
