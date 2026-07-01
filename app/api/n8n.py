from fastapi import APIRouter
from pydantic import BaseModel
from app.services.scraper import extract_content
from app.services.ai_service import generate_summary

router = APIRouter()

class UrlRequest(BaseModel):
    url: str


@router.post("/n8n/summarize")
def summarize(req: UrlRequest):

    print("URL:", req.url)

    data = extract_content(req.url)
    print("SCRAPER RESULT:", data)

    if not data:
        return {"error": "scraper failed"}

    if "content" not in data:
        return {"error": "no content field", "data": data}

    result = generate_summary(data["content"])
    print("AI RESULT:", result)

    return {
        "title": data.get("title"),
        "summary": result.get("summary"),
        "keywords": result.get("keywords")
    }
