from fastapi import FastAPI, Depends, Request, APIRouter
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from infra.database import get_db
from application.search_url import search_short_code


router = APIRouter()

@router.get("/{short_url}",status_code=301)
def redirect(short_url, db: Session = Depends(get_db)) -> RedirectResponse:
    return RedirectResponse(url=search_short_code(short_code_url=short_url,db=db),status_code=301)