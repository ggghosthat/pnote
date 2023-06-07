from models.dashboard import Dashboard
from datetime import datetime
from base import logger

dash = Dashboard()
# dash.add_plan(new_title='hello', new_description='dayline')
plans = dash.get_plans()
for p in plans:
    print(p.title)