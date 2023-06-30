from sqlalchemy import Column, String, Integer, CHAR, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime
from .base import Base, session

class Site(Base):
    __tablename__ = "sites"
    
    lid = Column("lid", Integer, primary_key=True, autoincrement=True, nullable=False)
    url = Column("url", String)
    created = Column("created", DateTime)
    title = Column("title", String)
    description = Column("description", String)