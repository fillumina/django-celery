from django.urls import reverse
from tasks import sample_tasks
from unittest.mock import patch
import json

def test_home(client):
    url = reverse("home")
    response = client.get(url)
    assert response.status_code == 200

def test_task():
    # .run() runs the task directly without using Celery .delay()
    assert sample_tasks.create_task.run(1)
    assert sample_tasks.create_task.run(2)
    assert sample_tasks.create_task.run(3)

@patch("tasks.sample_tasks.create_task.run")
def test_mock_task(mock_run):
    assert sample_tasks.create_task.run(1)
    sample_tasks.create_task.run.assert_called_once_with(1)

    assert sample_tasks.create_task.run(2)
    sample_tasks.create_task.run.assert_called_call_count = 2

    assert sample_tasks.create_task.run(3)
    sample_tasks.create_task.run.assert_called_call_count = 3

# full integration test
# it uses the default Celery configuration, otherwise configure a new
# one with:
# app = celery.Celery('tests', broker=CELERY_TEST_BROKER, backend=CELERY_TEST_BACKEND)
def test_task_status(client):
    response = client.post(reverse("run_task"), {"type": 0})
    content = json.loads(response.content)
    task_id = content["task_id"]
    assert response.status_code == 202
    assert task_id

    response = client.get(reverse("get_status", args=[task_id]))
    content = json.loads(response.content)
    assert content == {"task_id": task_id, "task_status": "PENDING", "task_result": None}
    assert response.status_code == 200

    while content["task_status"] == "PENDING":
        response = client.get(reverse("get_status", args=[task_id]))
        content = json.loads(response.content)
    assert content == {"task_id": task_id, "task_status": "SUCCESS", "task_result": "this is the result"}