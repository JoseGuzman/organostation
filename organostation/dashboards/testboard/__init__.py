"""
__init__.py

Author: Jose Guzman
Created: Mon Aug 15 21:38:23 EDT 2022

Dash tests based on this video:
https://www.youtube.com/watch?v=7m0Bq1EGPPg
"""

import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
from dash import dcc
from flask import Flask

from .src.components import layout


# must return a Dash object
def test_layout(flask_app: Flask) -> None:

    layout.simple_graph(flask_app)
