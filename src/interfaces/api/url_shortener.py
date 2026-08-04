from fastapi import FastAPI, Depends, Request, APIRouter
from domain.schemas import UrlShortener
from infra.database import get_db
from application.shortener_app import shortener_url
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/shortener")
def create_url_shortener(body: UrlShortener, db: Session = Depends(get_db)):
    return {'url_shortened': shortener_url(url=body.url,db=db),
            'message':'url shortener success'
           }