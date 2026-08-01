from fastapi import FastAPI, Depends, Request, APIRouter


router = APIRouter()

@router.get("/search_url")
def search_url(url: str) -> str:
    return {'url': 'http:/urlshort/bju8',
            'message': 'url encontrada'}