# About Page

import os
import pathlib
from pathlib import Path
import pandas as pd
import plotly.express as px
import dash
from dash import Dash, html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc

dash.register_page(__name__)

layout = html.Div(
    style={'max-width': '1475px', 'margin': 'auto'},
    children=[
        html.H1('About Us',className='text-center text-dark mt-3 mb-2 fs-1'),
        html.P("COMING SOON!",className='text-center text-dark mt-3 mb-2 fs-6'),
    ]
)