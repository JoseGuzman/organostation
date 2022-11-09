"""
layout.py

Layouts for the visualoid dashboard

"""
from dash import Dash, html
import dash_bootstrap_components as dbc

# application imports
from . import dropdown, bar_chart


def simple_callback(dashboard: Dash) -> html.Div:
    """
    Basic layout to test basic components in a layout 
    and its callbacks
    """

    mydiv = html.Div(
        className = "app-div",
        children = [
            html.H1(dashboard.title),
            html.Hr(),
            html.Div(
                className = "dropbox-container", 
                children = [dropdown.render(dashboard, title='Test')]
            ),
            bar_chart.render(dashboard)
        ]
    )
    return mydiv

def simple_test(dashboard: Dash) -> html.Div:
    """
    Simple layout for testing pourposes
    """

    # define a simple layout with a dbc container
    return dbc.Container(
        children = [
            html.Br(),
            html.H1(dashboard.title),
            html.Hr(),
            html.H3("Simple_test"),
            html.Br()
        ]
    )