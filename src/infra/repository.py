from sqlalchemy.orm import Session
from domain.models import ShortUrl


class ShortUrlRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_short_code(self, short_code: str) -> ShortUrl | None:
        return (
            self.db.query(ShortUrl)
            .filter(ShortUrl.short_code == short_code)
            .first()
        )

    def create(self, short_code: str, original_url: str) -> ShortUrl:
        entry = ShortUrl(short_code=short_code, original_url=original_url)
        self.db.add(entry)
        self.db.commit()
        self.db.refresh(entry)
        return entry