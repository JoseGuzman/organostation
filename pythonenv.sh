#!/bin/bash
# With python environments

if [ -d ".flaskenv" ]
then
    source .flaskenv/bin/activate
    python3 -m pip install --upgrade pip
    #python3 wsgi.py
else
    python3 -m venv .flaskenv
    source .flaskenv/bin/activate
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    #python3 wsgi.py
fi
