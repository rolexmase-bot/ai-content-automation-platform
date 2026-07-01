from app.database.db import SessionLocal

from app.services.scraper import extract_content
from app.services.ai_service import generate_summary
from app.crud.article_crud import save_ai_result


def process_article(url):

    db = SessionLocal()

    try:
        print("Fetch started")

        article = extract_content(url)

        if not article:
            raise ValueError("Scraper returned empty article")

        title = article.get("title") or "No Title"
        content = article.get("content") or ""

        if not content.strip():
            print("WARNING: empty content, using title as fallback")
            content = title

        print("AI working")

        result = generate_summary(content)

        summary = result.get("summary", "")
        keywords = result.get("keywords", [])

        print("Writing into SQL")

        save_ai_result(
            db,
            url,
            title,
            content,
            summary,
            keywords
        )

        return {
            "title": title,
            "summary": summary,
            "keywords": keywords
        }

    finally:
        db.close()
