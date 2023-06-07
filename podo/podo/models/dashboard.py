from datetime import datetime
from models.types import Plan, Task
from base import session, Base, engine, logger
import sys, os

class Dashboard:
    plans_pool = session.query(Plan).order_by(Plan.created.desc())
    tasks_pool = session.query(Task).order_by(Task.created.desc())

    step = 10
    plans_position = 0
    tasks_position = 0

    def __init__(self):
        Base.metadata.create_all(bind=engine)


    #notes manipulation methods

    def get_single_plan(self, id):
        try:
            return self.plans_pool.filter(Plan.pid==id).first()
        except Exception as ex :
            self.hit_error(str(ex))
            pass

    def get_plans(self):
        try:
            if self.plans_position > self.plans_pool.count():
                return
            plans = self.plans_pool.limit(self.step).offset(self.plans_position)
            self.plans_position = self.plans_position + self.step
            return plans
        except Exception as ex :
            self.hit_error(str(ex))
    
    def add_plan(self, 
                 new_title,
                 new_description):
        try:
            plan = Plan(title=new_title,
                        description=new_description, 
                        created=datetime.now())
            session.add(plan)
            session.commit()
            return plan.pid
        except Exception as ex :
            self.hit_error(str(ex))
            pass

    def remove_plan(self, id):
        try:
            plan = session.query(Plan).filter(Plan.pid==id).one()
            session.delete(plan)
            session.commit()
        except Exception as ex :
            self.hit_error(str(ex))
            pass

    def update_plan(self,
                    id,
                    new_title = None,
                    new_description = None):        
        try:
            plan = session.query(Plan).filter(Plan.pid==id).first()

            if new_title != None:
                plan.title = new_title
            if new_description != None:
                plan.new_description = new_description

            if (new_title != None) or (new_description != None):
                session.commit()
                return plan.pid
        except Exception as ex :
            self.hit_error(str(ex))
            pass
    
    #tasks manipulation methods

    def get_single_task(self, id):
        try:
            task = self.tasks_pool.filter(Task.tid==id).first()
            return task
        except Exception as ex :
            self.hit_error(str(ex))
            pass

    def get_tasks(self):
        try:
            if self.tasks_position > self.tasks_pool.count():
                return
            tasks = self.tasks_pool.limit(self.step).offset(self.tasks_position)
            self.tasks_position = self.tasks_position + self.step
            return tasks
        except Exception as ex :
            self.hit_error(str(ex))
            pass

    def add_task(self, pid, raw, timeset):
        try:
            task = Task(raw=raw, 
                        created=datetime.now(),
                        timeset=timeset,
                        note_id=pid)
            
            session.add(task)
            session.commit()
            return task.tid
        except Exception as ex :
            self.hit_error(str(ex))
            pass    

    def remove_task(self, tid):
        try:
            session.query(Task).filter(Task.tid==tid).delete()
            session.commit()
        except Exception as ex :
            self.hit_error(str(ex))
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
            self.hit_error(str(ex))
            pass

    def hit_error(self, msg):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        metadata = f'{exc_type} {fname} {exc_tb.tb_lineno}'
        logger.error(f'{msg} ({metadata})')