#!/bin/sh

echo "python in web application container"
docker-compose run web /usr/src/app/manage.py shell
