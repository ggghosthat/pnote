from datetime import datetime
from models.types import Note, Task
from base import session, Base, engine


# note1 = Note(title="Hello World", created=datetime.now())
# Base.metadata.create_all(bind=engine)
# session.add(note1)
# session.commit()

# note = session.query(Note).first()
# note.add_task(raw="wake up", timeset=datetime.now())

notes = session.query(Task).all()

print("--------------")
for task in notes:
    print(task.raw)
    print(task.note.title)

print(len(notes))