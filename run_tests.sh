#!/bin/bash
source venv/Scripts/activate
pytest test_visualiser.py

if [ $? -eq 0 ]; then
  echo "Tests passed! Returning exit code 0."
  exit 0
else
  echo "Tests failed! Returning exit code 1."
  exit 1
fi