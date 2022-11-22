"""
table.py
"""

from dash import Dash, dash_table
from dash import html, dcc

import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)[["country", "pop", "continent", "lifeExp"]]

app = Dash(__name__)

def create_table() -> html.Div:

    mytable = html.Div(
        [ 
            html.Hr(),
            html.H6('Recording Library'),
            html.Br(),
            dash_table.DataTable(
            df.to_dict("records"),
            [{"name": i, "id": i} for i in df.columns],
            filter_action="native",
            filter_options={"placeholder_text": "Filter column..."},
            page_size=10,
            )
        ]
    )
    return mytable
