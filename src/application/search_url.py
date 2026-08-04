from infra.repository import ShortUrlRepository
from sqlalchemy.orm import Session
from fastapi import HTTPException

def search_short_code(short_code_url: str, db: Session):
    repo = ShortUrlRepository(db=db)

    url_to_redirect = repo.get_by_short_code(short_code=short_code_url)

    if not url_to_redirect:
        raise HTTPException(status_code=404,detail="URL nao encontrada")
    
    return url_to_redirect.original_url