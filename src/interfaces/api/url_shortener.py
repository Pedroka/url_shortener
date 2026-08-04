from fastapi import FastAPI, Depends, Request, APIRouter
from domain.schemas import UrlShortener

from application.shortener_app import shortener_url


router = APIRouter()


@router.post("/shortener")
def create_url_shortener(body: UrlShortener):
    return {'url_shortened': shortener_url(url=body.url),
            'message':'url shortener success'
           }