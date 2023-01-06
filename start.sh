#!/bin/bash

if [ -d ".venv" ]
then
    pipenv shell
    pipenv update
    python3 wsgi.py
else
    python3 -m pip install --upgrade pip
    pip install pipenv
    pipenv install 
    pipenv shell
    python3 wsgi.py
fi
