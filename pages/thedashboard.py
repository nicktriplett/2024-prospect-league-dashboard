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
        html.H1('About This Project - The Prospect League Dashboard',className='text-center text-dark mt-4 mb-4 fs-1'),
        dbc.Row([
            dbc.Col(
                children=[
                     html.P("In 2023 and 2024, I was a Data Analytics Intern for the Thrillville Thrillbillies. There, my mission was to provide Thrillbillies coaches, media, and fans with the data, insights, and analysis necessary to better understand the team I was associated with, as well as the rest of the league that the Thrillbillies compete in: the Prospect League. For people away from the team and its activities, my goal was to share more about this team within the community that regained professional baseball. For people tied to the team, my goal was simple: help the team win. This dashboard serves as an example of me trying to do just that.",className='text-left text-dark mt-0 mb-2 fs-6'),
                ],
                width=10,
                className='mt-4 offset-md-1 mb-4'
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.Img(
                    src=dash.get_asset_url('pl-data.png'),
                    style={
                        'width':'100%',
                        'vertical-align':'top',
                        'object-fit':'contain',
                        'height':'450px'}
                ),
                width={'size': 10},
                className='mt-4 mb-3'
            ),
            ],
            justify='center'
        ),
        html.Div(
        children=[
            'Data Source: ',
            html.A(
                'Prospect League',
                href='https://prospectleague.com/landing/index',className='text-info fs-6'
            ),
        ],
        className='text-dark text-center fs-6 mt-2 mb-4'
    ),
        dbc.Row([
            dbc.Col(
                children=[
                     html.P("At the start of the 2023 season, I began reviewing statistics from the Prospect League website with the intention of finding unique ways to work with the public data. What I quickly realized was that a greater opportunity made itself known: our team needed more information to fully analyze players and teams in the Prospect League. Nearly 25 hitting statistics and 15 pitching statistics were easily available to my team and me, yet I knew we could learn more about our team and its performance if we had more information. From there, I started creating a foundation for a new method of reviewing Prospect League data.",className='text-left text-dark mt-0 mb-2 fs-6'),
                ],
                width=10,
                className='mt-4 offset-md-1 mb-5'
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.Img(
                    src=dash.get_asset_url('excel-file.png'),
                    style={
                        'width':'100%',
                        'vertical-align':'top',
                        'object-fit':'contain',
                        'height':'400px'}
                ),
                width={'size': 10},
                className='mt-4 mb-3'
            ),
            ],
            justify='center'
        ),
        dbc.Row([
            dbc.Col(
                children=[
                     html.P("NOTE: This data set is available and can be accessed by request.",className='text-center text-dark mt-0 mb-2 fs-6'),
                ],
                width=10,
                className='mt-2 offset-md-1 mb-4'
            )
        ]),
        dbc.Row([
            dbc.Col(
                children=[
                     html.P("Though I had created new data sets, I wanted to find uses for it within the Thrillbillies organization. One of the most notable way this data was utilized was in creating game day guides through Tableau for our team’s coaches. The combination of existing basic and advanced statistics, along with additional calculations added in the Excel data sets, resulted in the team having information set up in the style of a table normally found on Baseball Reference. Our opponent’s and own player and team statistics were provided before each game, with the purpose of assisting in-game strategy and decision making.",className='text-left text-dark mt-0 mb-2 fs-6'),
                ],
                width=10,
                className='mt-2 offset-md-1 mb-3'
            )
        ]),
        dbc.Row([
            dbc.Col(
                children=[
                     html.P("Another way this data was useful was in publishing statistics on Tableau Public. As the season progressed, uploading these statistics allowed fans and promoters of the Prospect League to grab a full understanding of what exactly was happening within the league. Rather than relying on simple statistics, people were able to know just how much each player and team was producing towards varying levels of success over the course of the summer.",className='text-left text-dark mt-0 mb-2 fs-6'),
                ],
                width=10,
                className='mt-2 offset-md-1 mb-4'
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.Img(
                    src=dash.get_asset_url('tableau.png'),
                    style={
                        'width':'100%',
                        'vertical-align':'top',
                        'object-fit':'contain',
                        'height':'500px'}
                ),
                width={'size': 10},
                className='mt-4 mb-3'
            ),
            ],
            justify='center'
        ),
        html.Div(
            children=[
                'NOTE: This website is live and can be accessed ',
                html.A(
                    'here.',
                    href='https://public.tableau.com/app/profile/nicholas.triplett/viz/2024ProspectLeagueStatistics/IllinoisValley?publish=yes',className='text-info fs-6'
                ),
        ],
        className='text-center text-dark mt-2 mb-4 fs-6'
        ),
        dbc.Row([
            dbc.Col(
                children=[
                     html.P("In this website’s case, visualizing Prospect League data serves a few purposes. First and foremost, visualizing Prospect League data helped the Thrillbillies recognize where they thrived and struggled, in comparison to opponents. This information could be relayed to coaches and staff members, where team adjustments could be made. Ultimately, this led the Thrillbillies to win two straight South Division titles and nearly 70 wins during the first two years of existence.",className='text-left text-dark mt-0 mb-2 fs-6'),
                ],
                width=10,
                className='mt-2 offset-md-1 mb-3'
            )
        ]),
        dbc.Row([
            dbc.Col(
                children=[
                     html.P("Secondly, this project became an opportunity for me to showcase my knowledge of coding and prove my capabilities for the baseball industry. Learning Python has been and continues to be a passion of mine, and my goal is that this dashboard not only replicates some of my abilities that I can provide to a professional sports organization, but also shows my desire to learn more about coding and being associated with the industry. My time with the Thrillville Thrillbillies assisted in the creation of this dashboard, among many other projects. Now, I turn towards future opportunities, where I look forward to bringing these skills, alongside many others, to benefit other organizations and, overall, the sports industry.",className='text-left text-dark mt-0 mb-2 fs-6'),
                ],
                width=10,
                className='mt-2 offset-md-1 mb-4'
            )
        ]),
        dbc.Row([
            dbc.Col(
                children=[
                     html.P("Please feel free to reach out to me at nicholas.triplett@siu.edu or visit my LinkedIn profile if you have any questions for me. Explore the dashboard here yourself and see how this website has generated data-driven opportunities for the Thrillbillies.",className='text-center text-dark mt-0 mb-2 fs-6'),
                ],
                width=10,
                className='mt-2 offset-md-1 mb-5'
            )
        ]),
    ]
)
