"""
User interfaces components (dcc)
for layouts and menus


"""
from typing import List, Tuple
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

from . import ids

def render(dashboard: Dash, title:str) -> html.Div:
    """
    A header string with a Dropdown component.
    """
    all_nations = ['South Korea', 'China', 'Canada']
    myoptions = [{"label":i, "value":i} for i in all_nations]

    @dashboard.callback(
        Output(ids.NATION_DROPDOWN, 'value'),
        Input(ids.NATION_BUTTON, 'n_clicks'),
    )
    def select_all_nations(_:int) -> List[str]:
        """ collects inputs (number of clicks) 
        and sets the value of dropbox to all nations"""
        return all_nations

    mydiv = html.Div(
        children = [
            html.H6(title),
            dcc.Dropdown(id = ids.NATION_DROPDOWN,
                    options = myoptions,
                    value = all_nations,
                    multi=True
            ),
            html.Button(id = ids.NATION_BUTTON,
                className="dropdown-button",
                children = ["Select All"]

            )
            ]
        )
    return mydiv
