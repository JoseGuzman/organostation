"""
wsig.py

Created: Wed Dec  7 14:23:08 CET 2022

This is the Application entry point. It creates the app (myapp)
from organostation and runs it on port 8051.

To run this app you need the appropiate environment and type:
>>> python wsgi.py
"""
from organostation import create_app

myapp = create_app()

if __name__ == "__main__":
    myapp.run(port=8051)
