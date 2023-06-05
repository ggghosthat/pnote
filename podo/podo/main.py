from datetime import datetime
from models.types import Note, Task
from base import session

class Dashboard:
    pool = session.query(Note).order_by(Note.created.desc())
    pool_count = len(pool)
    step = 10
    position = 0

    def get_single(self, id):
        try:
            note = self.pool.filter(Note.nid==id).first()
            return note
        except Exception as ex :
            # TODO rise exception within newly implemented logger
            pass

    def get_notes(self):
        try:
            if self.position > self.pool_count:
                return
            notes = self.pool.limit(self.step).offset(self.position)
            self.position = self.position + self.step
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
        except Exception as ex :
            # TODO rise exception within newly implemented logger
            pass