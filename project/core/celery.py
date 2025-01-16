import os

# if the web application doesn't find celery rebuild it
# with 'docker compose up -d --build'
# or use 'pip install celery' from inside the container
from celery import Celery
from celery.utils.log import get_task_logger

# celery needs to know where to find the django project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# create a new celery instance
# the first argument is the name of the current module
# app = Celery('tasks', backend='redis://localhost', broker='pyamqp://')
# the other arguments can be defined in the settings
app = Celery("core")
# load default settings (option named CELERY_xxx)
app.config_from_object("django.conf:settings", namespace="CELERY")
# look for celery tasks (annotated with @shared_task)
app.autodiscover_tasks()

# define a logger
logger = get_task_logger("core")

