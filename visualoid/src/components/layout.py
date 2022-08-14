"""
layout.py

Layouts for the visualoid dashboard

"""
from dash import Dash, html
from . import dropdown


def test_layout(dashboard: Dash) -> html.Div:
    """
    Basic layout to test that includes the title of the dashboard
    and a second html.Div element.
    """

    mydiv = html.Div(
        className = "app-div",
        children = [
            html.H1(dashboard.title),
            html.Hr(),
            html.Div(
                className = "dropbox-container", 
                children = [dropdown.render(dashboard, title='Test')]
            )
        ]
    )
    return mydiv

def basic(dashboard: Dash) -> html.Div:
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
