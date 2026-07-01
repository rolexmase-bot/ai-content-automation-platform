from sqlalchemy.orm import Session

from app.models.article import Article


def get_articles(
    db: Session
):

    return (
        db
        .query(Article)
        .order_by(
            Article.id.desc()
        )
        .all()
    )


def get_article_by_id(
    db: Session,
    article_id: int
):

    return (
        db
        .query(Article)
        .filter(
            Article.id == article_id
        )
        .first()
    )
