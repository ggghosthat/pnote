from sqlalchemy import create_engine, Column, String, Integer, CHAR, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base()

class Note(Base):
    __tablename__ = "notes"

    nid = Column("nid", Integer, primary_key=True, autoincrement=True)
    title = Column("title", String)
    created = Column("created", DateTime)
    tasks = relationship("Task", backref="note", lazy=True)

    def __init__(self, title, created):
        self.title = title
        self.created = created