from fastapi import FastAPI

from app.api.content import router as content_router

app = FastAPI(
    title="AI Content Automation Platform",
    version="1.0.0"
)

app.include_router(content_router)

@app.get("/")
def root():
    return {
        "message": "AI Content Automation Platform Running"
    }
