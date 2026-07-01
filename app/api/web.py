from fastapi import (
    APIRouter,
    Request,
    Form
)

from fastapi.responses import (
    HTMLResponse
)

from fastapi.templating import (
    Jinja2Templates
)

import asyncio
import requests

from app.workflows.process_article import (
    process_article
)

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


N8N_WEBHOOK = "http://n8n:5678/webhook/ai-content"


@router.get(
    "/",
    response_class=HTMLResponse
)
async def home(
    request: Request
):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": None
        }
    )


@router.post(
    "/",
    response_class=HTMLResponse
)
async def generate(
    request: Request,
    url: str = Form(...)
):


    result = await asyncio.to_thread(
        process_article,
        url
    )


    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": result
        }
    )
