from pydantic import BaseModel


class ArticleResponse(
    BaseModel
):

    id: int

    url: str

    title: str | None

    content: str | None

    summary: str | None

    keywords: str | None


    class Config:

        from_attributes = True
