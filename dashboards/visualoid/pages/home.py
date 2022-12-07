"""
manager.py

Created: Thu Dec  1 13:32:18 CET 2022
Author: Jose Guzman, sjm.guzman@gmail.com

Contains the File Manager pages for the Visualoid App.

This file requires a dash.register_page(__name__) together with
a Layout to run. Check https://dash.plotly.com/urls for details.

This file must contain a function or a variable called layout
"""
import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

import pandas as pd

dash.register_page(__name__, path='/visualoid')

def layout(dashboard:Dash, data = pd.DataFrame) -> html.Div:
    """
    Home page
    """
    return html.Div([html.H1('Home Page')])