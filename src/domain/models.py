from sqlalchemy import Column, Integer, String, DateTime, func
from infra.database import Base
from datetime import datetime
from sqlalchemy import Sequence, func
from sqlalchemy.orm import Mapped, mapped_column


class ShortUrl(Base):
    __tablename__ = 'short_urls'

    id = Mapped[int] = mapped_column(
        Integer, 
        Sequence("short_url_id_seq", start=1000), 
        primary_key=True
    )
    short_code = Column(String(10), unique=True, index=True, nullable=False)
    original_url = Column(String(2048), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())