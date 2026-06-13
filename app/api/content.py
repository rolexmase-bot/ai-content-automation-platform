from fastapi import APIRouter

router = APIRouter()

@router.get("/content")
def get_content():

    return {
        "status": "ok"
    }
