"""
Application entry point. 

To run this app simply execute the run.sh script attached 
to this repository.
"""
from organostation import init_app

app = init_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8051)

