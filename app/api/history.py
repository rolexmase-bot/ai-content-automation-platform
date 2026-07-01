from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.db import (
    SessionLocal
)

from app.crud.article_history import (
    get_articles,
    get_article_by_id
)

from app.schemas.article import (
    ArticleResponse
)

router = APIRouter()


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


@router.get(
    "/articles",
    response_model=list[
        ArticleResponse
    ]
)
def list_articles(
    db: Session = Depends(
        get_db
    )
):

    return (
        get_articles(
            db
        )
    )


@router.get(
    "/articles/{id}",
    response_model=ArticleResponse
)
def detail(
    id: int,
    db: Session = Depends(
        get_db
    )
):

    article = (
        get_article_by_id(
            db,
            id
        )
    )

    if not article:

        raise HTTPException(
            404,
            "article not found"
        )

    return article
