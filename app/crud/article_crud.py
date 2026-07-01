from app.models.article import (
    Article
)


def save_ai_result(
    db,
    url,
    title,
    content,
    summary,
    keywords
):

    article = Article(
        url=url,
        title=title,
        content=content,
        summary=summary,
        keywords=",".join(
            keywords
        )
    )

    db.add(article)

    db.commit()

    db.refresh(article)

    return article
