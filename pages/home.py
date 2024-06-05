# Dashboard Home Page

import os
import pathlib
from pathlib import Path
import pandas as pd
import plotly.express as px
import dash
from dash import Dash, html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

layout = html.Div(
    children=[
        html.H1('2024 Prospect League Dashboard',className='text-center text-dark mt-3 mb-2 fs-1'),
        html.H1('DATA LAST UPDATED: 6/4/2024',className='text-center text-dark mt-3 mb-2 fs-1'),
        html.P("Testing...",className='text-center text-dark mb-4 mt-4 fs-6'),
        dbc.Row([
            dbc.Col(
                html.Img(
                    src=dash.get_asset_url('prospect-league-logo-image.png'),
                    style={
                        'width':'100%',
                        'vertical-align':'top',
                        'object-fit':'contain'}
                ),
                width={'size': 5},
            ),
            ],
            justify='center'
        ),
        html.Div(
            children=[
                'Image and Favicon Source: ',
                html.A(
                    'Prospect League',
                    href='https://d2o2figo6ddd0g.cloudfront.net/h/p/iwgjhe5gqqzrfm/primary-logo-newimage.png',className='text-info fs-4'
                ),
        ],
        className='text-dark text-center fs-4 mt-3'
        ),
    ]
)