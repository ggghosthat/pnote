from sqlalchemy import Column, String, Integer, CHAR, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from base import Base, session
from datetime import datetime

class Note(Base):
    __tablename__ = "notes"

    nid = Column("nid", Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column("title", String)
    description = Column("description", String)
    created = Column("created", DateTime)
    checked = Column("checked", Boolean, default=False)

    def add_task(self, raw, timeset):
        try:
            task = Task(raw=raw, 
                        created=datetime.now(),
                        timeset=timeset,
                        note_id=self.nid)
            
            session.add(task)
            session.commit()
        except Exception as ex :
            # TODO rise exception within newly implemented logger
            pass    

    def remove_task(self, tid):
        try:
            session.query(Task).filter(Task.tid==tid).delete()
            session.commit()
        except Exception as ex :
            # TODO rise exception within newly implemented logger
            pass

    def update_task(self, 
                    task_id,
                    new_raw = None, 
                    new_note = None, 
                    new_priority = None):
        try:
            task = session.query(Task).filter(Task.tid==task_id).first()
            
            if new_raw != None:
                task.raw = new_raw
            if new_note != None:
                task.note_id = new_note
            if new_priority != None:
                task.priority = new_priority

            if (new_raw != None) or (new_note != None) or (new_priority != None):
                session.commit()
        except Exception as ex :
            # TODO rise exception within newly implemented logger
            pass
        
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

    note_id = Column(Integer, ForeignKey("notes.nid"), nullable=True)
    note = relationship("Note", foreign_keys=note_id)