import time

from celery import shared_task

# celery task function (auto discovered by configuration in core/celery.py)
# it will be executed by the celery worker not by the web application
# - use create_task() to call this method from django web application (will return True)
# - use create_task.delay() to call this method from Celery (will return an AsyncResult)
#   (see views.py run_task(request))
#   the actual result can be retrieved by invoking AsyncResult(task_id)
@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 5)
    return 'this is the result'
