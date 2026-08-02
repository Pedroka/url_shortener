from fastapi import FastAPI, Depends, Request, APIRouter
from fastapi.responses import RedirectResponse


router = APIRouter()

@router.get("/{short_url}",status_code=301)
def redirect() -> str:
    return RedirectResponse(url='https://www.uol.com.br/',status_code=301)