from sqlalchemy import Column, String, Integer, CHAR, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from base import Base, session
from datetime import datetime

class Note(Base):
    __tablename__ = "notes"

    nid = Column("nid", Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column("title", String)
    created = Column("created", DateTime)

    def add_task(self, raw, timeset):
        task = Task(raw=raw, 
                    created=datetime.now(),
                    timeset=timeset,
                    note_id=self.nid)
        
        session.add(task)
        session.commit()

class Task(Base):
    __tablename__ = 'tasks'

    tid = Column("tid", Integer, primary_key=True, autoincrement=True, nullable=False)
    raw = Column("raw", String)
    created = Column("created", DateTime)
    timeset = Column("timeset", DateTime)
    isCompleted = Column("is-completed", Boolean)
    completed = Column("completed", DateTime)

    note_id = Column(Integer, ForeignKey("notes.nid"))
    note = relationship("Note", foreign_keys=note_id)
