"""
__init__.py

Author: Jose Guzman
Created: Mon Aug 15 21:38:23 EDT 2022
"""
from flask import Flask

from dash import Dash, html, dcc
from dash_bootstrap_components.themes import BOOTSTRAP

import plotly.express as px
import pandas as pd

# custom layouts


def create_dashboard(flask_app:Flask) -> Dash:
    """
    Creates a dashboard inside a Flask application
    """

    # dash applicaton
    mydash = Dash( server = flask_app, 
        name = 'configurator', 
        url_base_pathname = '/configurator/',
        external_stylesheets=[BOOTSTRAP]
        )

    mydash.title = "Configurator"

    # dash layout
    #mydash.layout = layout.basic(dashboard = mydash) 
    #mydash.layout = layout.test_layout(dashboard = mydash) 
    mydash.layout = html.Div(children=[
        html.H1(children='Customize page'),

        html.Div(children='''
            Dash: A web application framework for your data.
        ''')
        ])

    return mydash 
