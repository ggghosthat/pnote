from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, CHAR, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    tid = Column("tid", Integer, primary_key=True, autoincrement=True)
    raw = Column("raw", String)
    created = Column("created", DateTime)
    isCompleted = Column("is-completed", Boolean)
    completed = Column("completed", DateTime)
    note_id = relationship(Integer, ForeignKey("notes.nid"), nullable=False)

    def __init__(self, raw, created, isCompleted=False, completed=datetime.min):
        self.raw = raw
        self.created = created
        self.isCompleted = isCompleted
        self.completed = completed

    