"""
file_loader.py

Jose Guzman
Created:  Tue Nov 22 19:41:01 CET 2022


User interfaces components (dcc) for loading data
"""
from typing import List

from dash import Dash, html, dcc
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

from . import ids  # custom IDs

UPLOAD_STYLE = {
    "width": "300px",
    "height": "60px",
    "lineHeight": "60px",
    "borderWidth": "1px",
    "borderStyle": "dashed",
    "borderRadius": "5px",
    "textAlign": "center",
    "margin": "10px",
}

def controls(dashboard:Dash) -> html.Div:
    controls = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("Recording Date"),
                dcc.Dropdown(
                    id="x-variable",
                    options=[
                        {"label": col, "value": col} for col in ['a', 'b', 'c']
                    ],
                    value="sepal length (cm)",
                ),
            ]
        ),
        html.Div(
            [
                dbc.Label("Y variable"),
                dcc.Dropdown(
                    id="y-variable",
                    options=[
                        {"label": col, "value": col} for col in range(4)
                    ],
                    value="sepal width (cm)",
                ),
            ]
        ),
        html.Div(
            dbc.Row(
                [
                    dbc.Col(
                        [
                        dbc.Label("Channel number"),
                        dbc.Input(id="cluster-count", type="number", value=3),
                        ]
                    ),
                    dbc.Col(
                        [
                        dbc.Label("Sampling (kHz)"),
                        dbc.Input(id="cluster-count", type="number", value=30),
                        ] 
                    )
                ]
            )
        ),
    ],
    body=True,
    )
    return html.Div(controls)

def save(dashboard:Dash) -> html.Div:
    """
    Save options
    """
    mysave = dbc.Card(
        [
        html.Div(
            dbc.Row(
                [
                    dbc.Col(
                        [
                        dbc.Input(id="cluster-count", type="number", value=3),
                        ], width=9
                    ),
                    dbc.Col(
                        [
                        dbc.Button('Save', id='save-file')
                        ], width=3
                    )
                ]
            )
        )
        ], body=True,
    )

    return html.Div(mysave)

def upload_option(dashboard:Dash) -> html.Div:
    """
    Upload file option
    """

    bar = html.Div(
        [
            html.H6("Upload"),
            dcc.Upload(
                id = "upload-data",
                children = html.Div(
                    ['Drag and drop or ', html.A('Select a binary File')]
                ),
                style= UPLOAD_STYLE, multiple = False,
            ),
            html.H6("Recording Library"),
            html.Hr(),
            html.Ul(id="file-list")
        ],
    )
    return bar 
