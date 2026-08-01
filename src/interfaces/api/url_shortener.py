from fastapi import FastAPI, Depends, Request, APIRouter
from domain.schemas import UrlShortener


router = APIRouter()


@router.post("/shortener")
def create_url_shortener(url:UrlShortener):
    return {'url_shortened': 'https://shorturl/b89y',
            'message':'url shortener success'
           }