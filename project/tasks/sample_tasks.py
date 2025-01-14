import time

from celery import shared_task

# celery task function (auto discovered by configuration in core/celery.py)
# it will be executed by the celery worker not by the web application
@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True
