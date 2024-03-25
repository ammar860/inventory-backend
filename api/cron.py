# myapp/cron.py
from datetime import datetime

from background_task import background


@background(schedule=60)  # Schedule the task to run every 60 seconds
def your_background_task():
    # Your background task implementation goes here
    your_task_function()


# myapp/tasks.py

def your_task_function():
    print(datetime.now().date())
    # Your task implementation goes here
    pass
