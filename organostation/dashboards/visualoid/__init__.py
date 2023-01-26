"""
Visualoid Dash app

Author: Jose Guzman
Created: Sun Aug 14 00:28:22 EDT 2022

This dashboard runs under flask
Visit https://github.com/okomarov/dash_on_flask for details
Check this video: https://www.youtube.com/watch?v=XOFrvzWFM7Y

This file creates the dash application and will serve as the entry
point for the multi-page app.
The Flask application will call the dashboards defined here
(i.e, the Dash object). The Dash object is the argument of a layout.
Layouts contain pre-designed components and callbacks and are
defined in .scr.components
"""
import dash_bootstrap_components as dbc  # for themes
from dash import Dash
from flask import Flask

# layouts take Dash object as an  argument
from .src.components import layout
from .src.components.menu import main_menu


def test_dashboard(flask_app: Flask) -> Dash:
    """
    Creates a test dashboard inside a Flask application
    """
    # main Dash applicaton
    mydashboard = Dash(
        server=flask_app,
        name="Visualoid",
        url_base_pathname="/visualoid/",
        external_stylesheets=[dbc.themes.SOLAR],
    )
    mydashboard.title = "Visualoid"
    # dash layout in src/components/layout
    # mydashboard.layout = layout.simple_layout(dashboard = mydashboard)
    mydashboard.layout = layout.error_404(dashboard=mydashboard)
    return mydashboard.server


def test(flask_app: Flask) -> Dash:
    """
    Creates a simple callback
    """
    mydashboard = Dash(
        server=flask_app,
        name="Visualoid",
        url_base_pathname="/visualoid/",
        external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP],
    )
    mydashboard.title = "Visualoid"
    # mymenu = main_menu(mydashboard)
    container = dbc.Container([main_menu(mydashboard)], fluid=True)
    mydashboard.layout = container
    return mydashboard.server


def test_side_bar(flask_app: Flask) -> Dash:
    """
    Test the side bar
    """
    mydashboard = Dash(
        server=flask_app,
        name="Visualoid",
        url_base_pathname="/visualoid/",
        external_stylesheets=[dbc.themes.BOOTSTRAP],
    )
    mydashboard.title = "Visualoid"
    mydashboard.layout = layout.main_side_bar(dashboard=mydashboard)
    return mydashboard
