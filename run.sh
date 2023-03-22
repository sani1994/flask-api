#!/bin/bash

if [ ! -d ".env" ]
then
  python3 -m venv .env
  source .env/bin/activate
  pip install -r requirements.txt
else
  source .env/bin/activate
fi
echo "Virtual environment activated"
echo "Testing..."
python3 -m unittest test.py
echo "Test Completed."
python3 app.py