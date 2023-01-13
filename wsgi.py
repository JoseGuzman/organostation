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
    if myapp.config["FLASK_ENV"] == "development":
        myapp.run(debug=True, port=8051)
    elif myapp.config["FLASK_ENV"] == "production":
        myapp.run(host="0.0.0.0", port=80)
    else:
        myapp.run(port=8051)
