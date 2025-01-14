#!/bin/sh

echo 'POST type=0 to http://localhost:1337/tasks/ ...'
curl -F type=0 http://localhost:1337/tasks/