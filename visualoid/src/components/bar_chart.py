"""
bar_plot.py

Jose Guzman
Created: Sun Aug 14 21:29:31 EDT 2022
"""
from typing import List

from dash import Dash, html, dcc
from dash.dependencies import Input, Output

import plotly.express as px

from . import ids

data = px.data.medals_long()


def render(dashboard: Dash) -> html.Div:
    @dashboard.callback(
        Output(ids.BAR_CHART, "children"),
        [
            Input(ids.NATION_DROPDOWN, "value"),
        ]
    )
    def update_bar_chart(nations: list[str]) -> html.Div:
        selected_data = data.query('nation in @nations')
        if selected_data.shape[0] == 0:
            myDiv = html.Div("No data selected", id=ids.BAR_CHART)

        else:
            fig = px.bar(selected_data, 
                x='medal', y= 'count', color='nation', text='nation')
            myDiv = html.Div(dcc.Graph(figure=fig), id = ids.BAR_CHART )
        
        return myDiv

    return html.Div(id = ids.BAR_CHART)
    


