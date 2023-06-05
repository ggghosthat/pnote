from datetime import datetime
from models.types import Note, Task
from base import session, Base, engine

class Dashboard:
    notes_pool = session.query(Note).order_by(Note.created.desc())
    tasks_pool = session.query(Task).order_by(Task.created.desc())

    step = 10
    notes_position = 0
    tasks_position = 0

    def __init__(self):
        Base.metadata.create_all(bind=engine)


    #notes manipulation methods

    def get_single_note(self, id):
        try:
            note = self.notes_pool.filter(Note.nid==id).first()
            return note
        except Exception as ex :
            # TODO rise exception within newly implemented logger
            pass

    def get_notes(self):
        try:
            if self.notes_position > self.notes_pool.count():
                return
            notes = self.notes_pool.limit(self.step).offset(self.notes_position)
            self.notes_position = self.notes_position + self.step
            return notes
        except Exception as ex :
            # TODO rise exception within newly implemented logger
            pass
    
    def add_note(self, 
                 new_title,
                 new_description):
        try:
            note = Note(title=new_title,
                        description=new_description, 
                        created=datetime.now())
            session.add(note)
            session.commit()
            return note.nid
        except Exception as ex :
            # TODO rise exception within newly implemented logger
            pass

    def remove_note(self, id):
        try:
            note = session.query(Note).filter(Note.nid==id).one()
            session.delete(note)
            session.commit()
        except Exception as ex :
            # TODO rise exception within newly implemented logger
            pass

    def update_note(self,
                    id,
                    new_title = None,
                    new_description = None):        
        try:
            note = session.query(Note).filter(Note.nid==id).first()

            if new_title != None:
                note.title = new_title
            if new_description != None:
                note.new_description = new_description

            if (new_title != None) or (new_description != None):
                session.commit()
                return note.nid
        except Exception as ex :
            # TODO rise exception within newly implemented logger
            pass
    
    #tasks manipulation methods

    def get_single_task(self, id):
        try:
            task = self.tasks_pool.filter(Task.tid==id).first()
            return task
        except Exception as ex :
            # TODO rise exception within newly implemented logger
            pass

    def get_tasks(self):
        try:
            if self.tasks_position > self.tasks_pool.count():
                return
            tasks = self.tasks_pool.limit(self.step).offset(self.tasks_position)
            self.tasks_position = self.tasks_position + self.step
            return tasks
        except Exception as ex :
            # TODO rise exception within newly implemented logger
            pass

    def add_task(self, nid, raw, timeset):
        try:
            task = Task(raw=raw, 
                        created=datetime.now(),
                        timeset=timeset,
                        note_id=nid)
            
            session.add(task)
            session.commit()
            return task.tid
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
                return task.tid
        except Exception as ex :
            # TODO rise exception within newly implemented logger
            pass