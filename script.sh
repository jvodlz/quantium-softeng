#!/bin/bash
. .venv/Scripts/activate

pytest --webdriver Firefox -k unit_test.py

#Exit status of last task
EXIT_CODE=$?
if [ $EXIT_CODE -eq 0 ]
then
  exit 0
else
  exit 1
fi
