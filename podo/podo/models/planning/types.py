from sqlalchemy import Column, String, Integer, CHAR, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from base import Base, session
from datetime import datetime

class Plan(Base):
    __tablename__ = "plans"

    pid = Column("pid", Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column("title", String)
    description = Column("description", String)
    created = Column("created", DateTime)
    checked = Column("checked", Boolean, default=False)
        
    def check(self):
        if self.checked == False:
            self.checked = True
        else:
            self.checked = False

class Task(Base):
    __tablename__ = 'tasks'

    tid = Column("tid", Integer, primary_key=True, autoincrement=True, nullable=False)
    raw = Column("raw", String)
    created = Column("created", DateTime)
    timeset = Column("timeset", DateTime)
    isCompleted = Column("is-completed", Boolean)
    completed = Column("completed", DateTime)
    priority = Column("priority", Integer)

    note_id = Column(Integer, ForeignKey("plans.pid"), nullable=True)
    note = relationship("Plan", foreign_keys=note_id)