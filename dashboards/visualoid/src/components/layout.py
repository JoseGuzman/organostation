"""
layout.py

Layouts for dash app return html.Div objects objects
to be appended to a dash application upon creation.
Ideally, the functions here should only get dash components
as argument, but they sometimes load the dashboard.

"""
from dash import Dash, html
import dash_bootstrap_components as dbc

# application imports
from . import dropdown, bar_chart, side_bar, files

def start_page(dashboard:Dash) -> html.Div:
    """
    Returns start page
    """
    mydiv = html.Div(
        className = "p-3 bg-light rounded-3",
        children = [
            html.H1("App start", className="center text-secondary"),
            html.Hr(),
            html.P("This is the main page ...")
            ]
    )
    return mydiv

def file_manager(dashboard:Dash) -> html.Div:
    """
    returns the file manager page
    """
    return html.Div(
        #className = "p-3 bg-light rounded-3",
        children =
            [
            dbc.Row(
                [
                    dbc.Col(files.controls(dashboard), md=3, className="bg-light"),
                    dbc.Col(files.upload_option(dashboard), className='bg-light')
                ],
                align="top"
            )
            ]
    )

def error_404(dashboard:Dash) -> html.Div:
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

def main_side_bar(dashboard:Dash) -> html.Div:
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

def simple_callback(dashboard:Dash) -> html.Div:
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


def simple_layout(dashboard: Dash) -> html.Div:
    """
    Simple layout for title and message for
    Bootstrap styling
    """
    # define a simple layout with a dbc container

    nav = dbc.Nav(
        [
            dbc.NavItem(dbc.NavLink('File Manager', active='exact', href="/file_manager")),
            dbc.NavItem(dbc.NavLink('Visualize', href="#")),
            dbc.NavItem(dbc.NavLink("Analysis", disabled=True, href="#")),
        ],
        fill=True, pills=True
    )

    mycont = html.Div(
        children = [
            html.Br(),
            html.H2(dashboard.title),
            html.Hr(),
            nav,
            html.Hr(),
            html.P("This is a simple layout for title and message")
        ]
    )
    return mycont