"""
Visualoid Dash app

Author: Jose Guzman
Created: Sun Aug 14 00:28:22 EDT 2022

Visit https://github.com/okomarov/dash_on_flask for details

This dashboard runs under flask

Check this video: https://www.youtube.com/watch?v=XOFrvzWFM7Y
"""
from flask import Flask

from dash import Dash, html, dcc
from dash_bootstrap_components.themes import BOOTSTRAP

import plotly.express as px
import pandas as pd

# custom layouts
from .src.components import layout

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

def create_dashboard(flask_app:Flask) -> Dash:
    """
    Creates a dashboard inside a Flask application
    """

    # dash applicaton
    mydash = Dash( server = flask_app, 
        name = 'visualoid', 
        url_base_pathname = '/visualoid/',
        external_stylesheets=[BOOTSTRAP]
        )

    mydash.title = "Visualoid"

    # dash layout
    mydash.layout = layout.basic(dashboard = mydash) 

    return mydash 

def test(flask_app) -> Dash:
    '''
    creates dash application inside the flask application and 
    renders it in /visualoid
    '''
    # dash application
    dash_app = Dash(server = flask_app, name = 'visualoid', url_base_pathname = '/visualoid/')

    # dash layout
    myfig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    dash_app.layout = html.Div(children=[
        html.H1(children='Visualoid Dash'),

        html.Div(children='''
            Dash: A web application framework for your data.
        '''),

        dcc.Graph(id='example-graph',figure = myfig)
        ])

    return dash_app 

"""
if __name__ == '__main__':
    app.run_server(debug=True) # hot reloading
"""
