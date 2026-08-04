from urllib.parse import urlparse
from infra.repository import ShortUrlRepository
from sqlalchemy.orm import Session
from fastapi import HTTPException
    

def shortener_url(url:str, db: Session) -> str:
    if not is_url(url):
        raise HTTPException(status_code=400, detail="URL inválida")
    
    repo = ShortUrlRepository(db=db)
    new_url = repo.create(original_url=url)

    return f'localhost:8000/{new_url.short_code}'

def is_url(url: str) -> bool:
    result = urlparse(url)
    return bool(result.scheme and result.netloc)