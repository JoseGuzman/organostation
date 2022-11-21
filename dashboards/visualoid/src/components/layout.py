"""
layout.py

Layouts for dash app return html.Div or dbc.Container objects
to be appended to a dash application upon creation.

"""
from dash import Dash, html
import dash_bootstrap_components as dbc

# application imports
from . import dropdown, bar_chart, side_bar

def error_404(dashboard: Dash) -> html.Div:
    """
    Returns 404 error
    """
    mydiv = html.Div(
        className = "p-3 bg-light rounded-3",
        children = [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P("The page was not recognised...")
            ]
    )
    return mydiv

def main_side_bar(dashboard: Dash) -> html.Div:
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
                children = [side_bar.render(dashboard, title='Test')]
            )
        ]
    )
    return mydiv

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

def simple_layout(dashboard: Dash) -> dbc.Container:
    """
    Simple layout for title and message
    """
    # define a simple layout with a dbc container
    mycont = dbc.Container(
        children = [
            html.Br(),
            html.H1(dashboard.title),
            html.Hr(),
            html.H3("Simple layout"),
            html.Br(),
            html.P("This is a simple layout for title and message")
        ]
    )
    return mycont