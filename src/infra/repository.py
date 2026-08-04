from sqlalchemy.orm import Session
from domain.models import ShortUrl
import base62


class ShortUrlRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_short_code(self, short_code: str) -> ShortUrl | None:
        return (
            self.db.query(ShortUrl)
            .filter(ShortUrl.short_code == short_code)
            .first()
        )

    def create(self, original_url: str) -> ShortUrl:
        entry = ShortUrl(original_url=original_url)
        self.db.add(entry)
        
        self.db.flush()

        entry.short_code = base62.encode(entry.id_short_url)

        self.db.commit()
        self.db.refresh(entry)

        return entry