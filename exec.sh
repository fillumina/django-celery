#!/bin/sh

# execute in the web container the given command
docker compose exec web $*
