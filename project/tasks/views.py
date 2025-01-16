from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from tasks.sample_tasks import create_task

from celery.result import AsyncResult

def home(request):
    return render(request, "home.html")


@csrf_exempt
def run_task(request):
    if request.POST:
        task_type = request.POST.get("type")
        # the returned task is of type AsyncResult
        task = create_task.delay(int(task_type))
        print(f'received request for task: {task.id}')
        return JsonResponse({"task_id": task.id}, status=202)


@csrf_exempt
def get_status(request, task_id):
    print(f'requested status for task: {task_id}')
    # to retrieve a result from celery call AsyncResult(task_id)
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
    return JsonResponse(result, status=200)
