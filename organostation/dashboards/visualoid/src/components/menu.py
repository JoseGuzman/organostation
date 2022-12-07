"""
Menu components 

"""

from dash import Dash, html, dcc
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc # for themes

from . import layout

def main_menu(dashboard:Dash) -> html.Div:
    """
    Basic three option menu to select pages
    """
    menubar = html.Div(
        [
            html.H1('App'),
            dbc.Nav(
                [
                    dbc.NavLink('File Manager', href='/manager', active='exact'),
                    dbc.NavLink('Visualize', href='/visualize', active='exact'),
                    dbc.NavLink('Analysis', href='/analysis', active='exact')
                ],
                fill = True, # fill horizontal space
                justified = True, # all items equal size
                pills = True #
            ),
            html.Br()
        ]
        #style = MENUBAR_STYLE
    )
    @dashboard.callback(
        Output("page-content", 'children'),
        [Input('url', 'pathname')]
    )
    def update_page(pathname:str) -> html.Div:
        """
        Update page content
        """
        if pathname =='/manager':
            return layout.file_manager(dashboard)
        else:
            return layout.start_page(dashboard)

    content = html.Div(id='page-content', children=[])
    # dcc.Location is a hidden component that tracks the url
    # the callback uses the current location to render the appropriate
    # page content. The active prop of each NavLink is set automatically
    # according to the current pathname.
    return html.Div(
        [
            dcc.Location(id='url'),
            menubar,
            content
        ]
    )