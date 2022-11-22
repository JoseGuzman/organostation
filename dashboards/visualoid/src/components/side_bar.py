"""
This app creates a simple sidebar layout using inline style 
arguments and the dbc.Nav component.

dcc.Location is used to track the current location, and a 
callback uses the current location to render the appropriate 
page content. The active prop of each NavLink is set automatically 
according to the current pathname. 
"""

from dash import Dash, html, dcc
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc # for themes

from . import layout

# the style arguments for the sidebar. 
# We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position 
# it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
def render(dashboard: Dash, title: str) -> html.Div:
    """
    The main application side menubar
    """
    sidebar = html.Div([
        html.H2(title, className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", 
            className="lead"
        ),
        dbc.Nav([
            dbc.NavLink('File Manager', href="/file_manager", active="exact"),
            dbc.NavLink('Visualize', href="/visualize", active="exact"),
            dbc.NavLink('Analysis', href="/analysis", active="exact"),
            ],
            fill=True, pills=True, justified=True
            ),
        ],
        #style=SIDEBAR_STYLE,
    )
    @dashboard.callback(
        Output("page-content", "children"),
        [Input("url", "pathname")]
    )
    def render_page_content(pathname:str):
        """
        reads pathname and loads the corresponding layout
        """
        if pathname == "/file_manager":
            return html.P("This is the content of the home page!")
        elif pathname == "/visualize":
            return html.P("This is the content of page 1. Yay!")
        elif pathname == "/analysis":
            return layout.error_404(dashboard)
        # return a 404 message
        return html.P('Home page')

    content = html.Div(id="page-content", style=CONTENT_STYLE)
    mylayout = html.Div([dcc.Location(id="url"), sidebar, content])

    return mylayout
