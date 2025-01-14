#!/bin/sh

# start the project
docker compose up -d --build

# execute in the web container the command 'python -m pytest' which will run the pytest module
docker compose exec web python -m pytest

# stop the project
docker compose down