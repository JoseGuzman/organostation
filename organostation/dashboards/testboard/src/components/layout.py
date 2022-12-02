"""
layout.py

Author: Jose Guzman
Created: Mon Aug 15 21:38:23 EDT 2022

Dash layouts based on this video:
https://www.youtube.com/watch?v=7m0Bq1EGPPg

A dashboard layout contains the dash application,
the components with the callbacks, and a container
with a list of html components.

"""
from flask import Flask

from dash import Dash, html 
from dash import Output, Input

# interactive higher-level components generated with 
# JavaScript, HTML, and CSS through the React.js library 
from dash import dcc 
import dash_bootstrap_components as dbc # install dash-bootstrap-components

import plotly.express as px

import pandas as pd


def simple_callback(flask_app:Flask) -> Dash:
    """
    Layout to test Dash with a simple callback
    """
    # main Dash application
    mydashboard = Dash(server = flask_app,
        name = 'TestBoard',
        url_base_pathname = '/testboard/',
        external_stylesheets=[dbc.themes.SOLAR]
    )

    # define components  
    myhead = dcc.Markdown(children='# Simple Callback ')
    myinput = dbc.Input(value='Insert your message here')
    mytext = dcc.Markdown(children=' ')

    # callback decorator and callback function
    @mydashboard.callback(
        Output(mytext, component_property='children'),
        Input(myinput, component_property='value')
    )

    def update_title(mytext):
        """
        Function argument comes from component_property of input
        """
        # returns componenent_property of the output
        return mytext

    # dash layout
    mydashboard.title = "testboard"
    mydashboard.layout = dbc.Container(
        children=[
            html.Br(),
            myhead, 
            html.Hr(), 
            myinput, 
            html.Hr(), 
            mytext
        ]
    )

    return mydashboard

def simple_graph(flask_app:Flask) -> Dash:
    """
    Creates a simple graph in a Flask application
    """

    # dash applicaton
    mydash = Dash( server = flask_app, 
        name = 'Simple Graph', 
        url_base_pathname = '/testboard/',
        external_stylesheets=[dbc.themes.LUX]
        )

    df = px.data.medals_long()

    # 1. components
    mytitle = dcc.Markdown(children='# App to see medals')
    mygraph = dcc.Graph( figure={}, id='graph', config= {'displaylogo': False})
    mydropdown = dcc.Dropdown(
        options = ['Bar Plot', 'Scatter Plot'],
        value = 'Bar Plot',
        clearable = False
    )

    # 2. callback decorator and function
    @mydash.callback(
        Output(component_id = 'graph', component_property = 'figure'),
        Input(mydropdown, component_property = 'value')
    )

    def update_graph(myselection):
        """
        It populates the figure
        """
        if myselection == 'Bar Plot':
            fig = px.bar(
                data_frame=df, x = 'nation', y = 'count',
                color='medal'
            )
        elif myselection == 'Scatter Plot':
            fig = px.scatter(
                data_frame = df, 
                x = 'nation', 
                y = 'count',
                color = 'medal'
            )
        # returned objects go to OutPut components_property 
        return fig
    # dash layout
    mydash.title = 'Graph'
    mydash.layout = dbc.Container(
        children = [
            html.Br(),
            mytitle,
            mygraph,
            mydropdown
        ]
    )
    return mydash 