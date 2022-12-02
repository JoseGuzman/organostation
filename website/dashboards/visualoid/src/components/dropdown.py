"""
dropdown.py

Jose Guzman
Created: Sun Aug 14 21:29:31 EDT 2022

User interfaces components (dcc) for layouts and menus 
that are using dropout components
"""
from typing import List

from dash import Dash, html, dcc
from dash.dependencies import Input, Output

from . import ids  # custom IDs


def render(dashboard: Dash, title: str) -> html.Div:
    """
    A header string with a Dropdown component.
    """
    all_nations = ['South Korea', 'China', 'Canada']
    myoptions = [{"label": i, "value": i} for i in all_nations]
    # we need a reference to our dashboard to create callbacks

    @dashboard.callback(
        Output(ids.NATION_DROPDOWN, 'value'),
        Input(ids.NATION_BUTTON, 'n_clicks'),
    )
    def select_all_nations(_: int) -> List[str]:
        """ collects inputs (number of clicks) 
        and sets the value of dropbox to all nations"""
        return all_nations

    mydiv = html.Div(
        children=[
            html.H6(title),
            dcc.Dropdown(id=ids.NATION_DROPDOWN,
                    options=myoptions,
                    value=all_nations,
                    multi=True
                    ),
            html.Button(id=ids.NATION_BUTTON,
                    className="dropdown-button",
                    children=["Select All"]
                    )
        ]
    )
    return mydiv
