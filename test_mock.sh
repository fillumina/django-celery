#!/bin/sh

# execute in the web container the command 'python -m pytest' which will run the pytest module
docker compose exec web python -m pytest -k "test_mock_task"
