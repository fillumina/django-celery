import time

from celery import shared_task
from core.celery import logger

# celery task function (auto discovered by configuration in core/celery.py and core/settings.py)
# it will be executed by the celery worker not by the web application
# - use create_task() to call this method from django web application (will return True)
# - use create_task.delay() to call this method from Celery (will return an AsyncResult)
#   (see views.py run_task(request))
#   the actual result can be retrieved by invoking AsyncResult(task_id)
#
# there is another annotation available which is @app.task where app is the
# one variable defined in `/core/celery.py`. By this way many Python process can use the
# same worker each with its own settings. If different processes should share the same
# task you have two annotation choices:
# - @app.task(shared = True) use the settings provided by the `app` application
# - @shared_task use the settings of the application that calls it
# see: https://stackoverflow.com/questions/21233089/how-do-i-use-the-shared-task-decorator-for-class-based-tasks?answertab=votes#tab-top
@shared_task
def create_task(task_type):
    logger.info('worker executing task')
    time.sleep(int(task_type) * 5)
    return 'this is the result'
