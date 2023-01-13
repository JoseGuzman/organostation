# OrganoStation

[![CodeFactor](https://www.codefactor.io/repository/github/joseguzman/organostation/badge)](https://www.codefactor.io/repository/github/joseguzman/organostation)

The [OrganoStation](http://www.organostation.com) is a customized system to obtain neurophysiological signals (e.g., EEG)
in brain organoids or other in vitro preparations.
It also contains a visualization app to document and analyze electrical or fluorescence signals.

## List of contents of directories 
```
.
|-- Pipfile
|-- Pipfile.lock
|-- README.md
|-- organostation
|   |-- __init__.py
|   |-- assets.py
|   |-- models.py
|   |-- dashboards
|   |   |-- testboard
|   |   `-- visualoid
|   |-- home
|   |   |-- views.py
|   |   |-- forms.py
|   |   |-- static
|   |   `-- templates
|   |-- tutorials 
|   |   |-- views.py
|   |   |-- static
|   |   `-- templates
|   |-- static
|   `-- templates
|       |-- blueprintinfo.jinja2
|       |-- footer.jinja2
|       |-- home.jinja2
|       |-- layout.jinja2
|       `-- navigation.jinja2
|-- env_example 
|-- config.py
|-- requirements.txt
|-- run.sh
|-- start.sh
`-- wsgi.py
```

## Installation
 * For the development version, we need [Node.js](https://nodejs.org/en/download/) and less with `npm install less`
 * Create a file called .evn in your home directory to run the forms (rename env_example) 

### Installation with 'requirements.txt'
Type `bash run.sh`

### Installation via [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)

You can simply type `bash start.sh` or install manually:

Type `pip install pipenv` to install pipenv and create an environment
using 

```shell
$ git clone https//github.com/JoseGuzman/organostation.git
$ cd organostation
$ mv env_example .env
$ mkdir .venv
$ pipenv shell --python path/to/python # (e.g., /usr/bin/python3.8)
$ pipenv update 
$ python wsgi.py
```

## Docker 
