"""
file_loader.py

Jose Guzman
Created:  Tue Nov 22 19:41:01 CET 2022


User interfaces components (dcc) for loading data
"""
from datetime import date
from typing import List

from dash import Dash, html, dcc
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

from . import ids  # custom IDs

UPLOAD_STYLE = {
    "width": "300px",
    "height": "50px",
    "lineHeight": "50px",
    "borderWidth": "1px",
    "borderStyle": "dashed",
    "borderRadius": "5px",
    "textAlign": "center",
    "margin": "10px",
}

def controls(dashboard:Dash) -> html.Div:
    """
    Basic controls for file saving
    """
    controls = dbc.Card(
    [
        html.Div(
            [
                dbc.Label("Recording Date"),
                dcc.DatePickerSingle(
                    min_date_allowed = date(1995,8,1),
                    max_date_allowed = date.today(),
                    initial_visible_month = date.today(),
                    date = date.today()

                ),
            ]
        ),
        html.Div(
            [
                dbc.Label("Probe Type"),
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
    mysave = dbc.Card([
        dbc.CardHeader("Filename"),
        dbc.CardBody(
            dbc.Row(
                [
                    dbc.Col(
                        [
                        dbc.Input(id="cluster-count", type="text"),
                        ], width=9
                    ),
                    dbc.Col(
                        [
                        dbc.Button('Add', id='save-file')
                        ], width=3
                    )
                ]
            )
        )
    ])

    return html.Div(mysave)

def comments(dashboard:Dash) -> html.Div:
    accordion = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    html.P("Recording observations"),
                    dbc.Textarea("Click here"),
                ],
                title="Notes",
            ),
        ],
        )
    )
    return accordion

def upload_option(dashboard:Dash) -> html.Div:
    """
    Upload file option
    """

    bar = html.Div(
        [
            dbc.Label("Upload"),
            dcc.Upload(
                id = "upload-data",
                children = html.Div(
                    ['Drag and drop or ', html.A('Select a binary File')]
                ),
                style= UPLOAD_STYLE, multiple = False,
            ),
        ],
    )
    return bar 
