from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from app.database.db import Base 
class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    url = Column(Text, nullable=False)
    title = Column(String(300))
    content = Column(Text)
    summary = Column(Text)
    keywords = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
