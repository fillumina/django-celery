import os

# if the web application doesn't find celery rebuild it
# with 'docker compose up -d --build'
# or use 'pip install celery' from inside the container
from celery import Celery

# celery needs to know where to find the django project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# create a new celery instance
app = Celery("core")
# load default settings (option named CELERY_xxx)
app.config_from_object("django.conf:settings", namespace="CELERY")
# look for celery tasks (annotated with @shared_task)
app.autodiscover_tasks()