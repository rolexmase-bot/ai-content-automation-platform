from fastapi import (
    APIRouter,
    HTTPException
)

from pydantic import (
    BaseModel
)

from app.workflows.process_article import (
    process_article
)

router = APIRouter()


class SummarizeRequest(
    BaseModel
):
    url: str


@router.post(
    "/summarize"
)
def summarize(
    request:
    SummarizeRequest
):

    try:

        return process_article(
            request.url
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
