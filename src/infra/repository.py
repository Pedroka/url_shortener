from sqlalchemy.orm import Session
from domain.models import ShortUrl
import base62
from hashids import Hashids

class ConvertBase62:
    def __init__(self, id):
        self.hash_ids = Hashids(salt='my_secret_key', alphabet='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.id = id
    
    def convert(self):
        return self.hash_ids.encode(self.id)


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

        entry.short_code = ConvertBase62(id=entry.id_short_url).convert()

        self.db.commit()
        self.db.refresh(entry)

        return entry