"""
Application entry point.

To run this app type python wsgi.py
"""
from organostation import init_app

myapp = init_app()

if __name__ == "__main__":
    myapp.run(port=8051)
