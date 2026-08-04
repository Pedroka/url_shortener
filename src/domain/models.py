from sqlalchemy import Column, Integer, String, DateTime, func, Identity
from infra.database import Base
from datetime import datetime
from sqlalchemy import Sequence, func
from sqlalchemy.orm import Mapped, mapped_column


class ShortUrl(Base):
    __tablename__ = 'short_urls'

    id_short_url = Column(Integer, Identity(start=15000), primary_key=True, autoincrement=True)
    short_code = Column(String(10), unique=True, index=True, nullable=True)
    original_url = Column(String(2048), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())