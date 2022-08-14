"""
Visualoid Dash app

Author: Jose Guzman
Created: Sun Aug 14 00:28:22 EDT 2022

Visit https://github.com/okomarov/dash_on_flask for details

This dashboard runs under flask
"""
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

#app = Dash(__name__)

# fake a datafram
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})


def create_visualoid_app(flask_app):
    '''
    creates dash application inside the flask application and 
    renders it in /visualoid
    '''
    # dash application
    dash_app = Dash(server = flask_app, name = 'visualoid', url_base_pathname = '/visualoid/')

    # dash layout
    myfig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
    dash_app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

        html.Div(children='''
            Dash: A web application framework for your data.
        '''),

        dcc.Graph(id='example-graph',figure = myfig)
        ])

    return dash_app 


if __name__ == '__main__':
    app.run_server(debug=True)
