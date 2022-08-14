"""
layout.py

Layouts for the visualoid dashboard

"""
from dash import Dash, html


def basic(dashboard: Dash) -> html.Div :
    """
    Basic layout to test
    """

    return html.Div(
        className = "app-div",
        children = [
                html.H1(dashboard.title),
                html.Hr()
                ] 
    )
