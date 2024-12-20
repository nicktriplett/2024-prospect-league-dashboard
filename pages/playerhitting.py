# Player Hitting Page

import os
import pathlib
from pathlib import Path
import pandas as pd
import plotly.express as px
import dash
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_table import DataTable

# Loading Data for Visualizations
main_file_path = pathlib.Path(__file__)
parent_folder = main_file_path.parent

data_file1 = parent_folder / 'pl_player_hitting_stats.csv'
data_file1.is_file()
player_hitting_stats = pd.read_csv(data_file1)
player_hitting_stats

last_row_index1 = len(player_hitting_stats) - 1
player_hitting_stats.drop(last_row_index1, inplace=True)

# Convert columns to float/numeric
player_hitting_stats['K%'] = player_hitting_stats['K%'].str.rstrip('%').astype(float)
player_hitting_stats['BB%'] = player_hitting_stats['BB%'].str.rstrip('%').astype(float)
# player_hitting_stats['SB%'] = player_hitting_stats['SB%'].str.rstrip('%').astype(float)
player_hitting_stats['TTO%'] = player_hitting_stats['TTO%'].str.rstrip('%').astype(float)
playerhitting_columns_to_convert = ['G','PA','PA/G','BB%','K%','BABIP', 'RC', 'wOBA','wRAA','wRAA/PA','wRC']
# include sb%  and wRC+ here
for column in playerhitting_columns_to_convert:
    player_hitting_stats[column] = pd.to_numeric(player_hitting_stats[column], errors='coerce')

# Creating Dataframe for Visualization
player_hitting_stats = player_hitting_stats.drop(columns=['#','Year','Position', 'Name (Original)', 'Team G Played', 'PA/TG','Abbreviation', 'Games Played %','PF'])
player_hitting_stats1 = player_hitting_stats.drop(columns=['Name'])
player_hitting_stats1.loc[:,('Name (Team)')]
player_hitting_stats1.set_index('Name (Team)',inplace=True)
player_hitting_stats2=player_hitting_stats1.drop(columns=['Team'])

player_hitting_stats3 = player_hitting_stats[player_hitting_stats['Qualified'] == "Yes"]
player_hitting_stats3.set_index('Name (Team)',inplace=True)

# Sorting Lists for Dashboard Components
batting_stat_list=[x for x in player_hitting_stats2.columns if x not in ['Conference', 'Division']]
batting_player_list = [x for x in player_hitting_stats2.index]
unique_teams = player_hitting_stats1['Team'].unique()


# Registring the Page
dash.register_page(__name__)

# The Pitching Chart Page
layout=dbc.Container(
    children=[
    # Title and Dashboard Explanation
    html.H1('2024 Prospect League Player Hitting Overview',className='text-center text-dark mt-3 mb-2 fs-1'),
    html.H3('Scatter Plot', className='text-info text-center fs-2 mt-3 mb-0'),
    # The Graph
    dbc.Row([
        dbc.Col(
            children=[
                dcc.Graph(
                    id='scatter_plot',
                    className='mx-4 my-3',
                    config=dict(displayModeBar=False),
                    style={
                        'height':'425px'
                    }
                ),
            ],
            width=10,
            className='offset-md-1'
        )
    ]),
    dbc.Row([
        dbc.Col(
            children=[
                dcc.RadioItems(
                    id='filter-radio',
                    options=[
                        {'label':'All Prospect League Hitters','value':'all'},
                        {'label':'Qualified Prospect League Hitters','value':'greater_than_2.7'}
                    ],
                    value='all',
                    labelStyle={'display': 'inline-block','margin-right': '10px'},
                    inputStyle={'margin-right': '10px'}
                )
            ],
            className='offset-md-4'
        )
    ]),
    dbc.Row([
        dbc.Col(
            children=[
                html.P('Team(s) Selector',className='text-dark, text-center mb-2 fs-5'),
                dcc.Dropdown(
                    id='team-dropdown25',
                    options=[{'label': team, 'value': team} for team in unique_teams],
                    multi=True,
                    value=unique_teams
                ),
            ],
            width=10,
            className='mt-4 offset-md-1 mb-3'
        )
    ]),

    dbc.Row([
        dbc.Col(
            children=[
                html.P('Please select a statistical measure for the X-axis to compare players with.',className='text-center text-dark fs-5 mt-1')
            ],
            width=6
        ),
        dbc.Col(
            children=[
                html.P("Please select a statistical measure for the Y-axis to compare players with.",className='text-center text-dark fs-5 mt-1')
            ],
            width=6
        )
    ]),
    # Dropdown Boxes
    dbc.Row([
        dbc.Col(
            children=[
                dcc.Dropdown(
                    id='stat_dropdown1',
                    options=[
                        dict(label=x,value=x) for x in batting_stat_list
                    ],
                    optionHeight=25,
                    className='mt-0 mb-3',
                    value='OPS',
                    clearable=False
                )
            ],
            width=4,
            className='offset-md-1'
        ),
        dbc.Col(
            children=[
                dcc.Dropdown(
                    id='stat_dropdown2',
                    options=[
                        dict(label=x,value=x) for x in batting_stat_list
                    ],
                    optionHeight=25,
                    className='mt-0 mb-3',
                    value='wRC',
                    clearable=False
                )
            ],
            width=4,
            className='offset-md-2'
        )
    ]),


    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    # Title and Dashboard Explanation
    html.H3('Bar Chart', className='text-info text-center fs-2 mt-3 mb-0'),
    # The Graph
    dbc.Row([
        dbc.Col(
            children=[
                dcc.Graph(
                    id='bar_chart1',
                    className='m-4',
                    config=dict(displayModeBar=False),
                ),
            ],
            width=10,
            className='offset-md-1'
        )
    ]),
    # User Commands
    dbc.Row([
        dbc.Col(
            children=[
                html.P('Please select a statistical measure to compare players with.',className='text-center text-dark fs-5 mt-3')
            ],
            width=6
        ),
        dbc.Col(
            children=[
                html.P("Please select a player(s) you'd like to review above.",className='text-center text-dark fs-5 mt-3')
            ]
        )
    ]),
    # Dropdown Boxes
    dbc.Row([
        dbc.Col(
            children=[
                dcc.Dropdown(
                    id='stat_choice1',
                    options=[
                        dict(label=x,value=x) for x in batting_stat_list
                    ],
                    className='mt-1 mb-3',
                    value='wRC',
                    multi=False,
                    optionHeight=25,
                    clearable=False
                )
            ],
            width=4,
            className='offset-md-1'
        ),
        dbc.Col(
            children=[
                dcc.Dropdown(
                    id='player_dropdown1',
                    options=[
                        dict(label=x,value=x) for x in batting_player_list
                    ],
                    multi=True,
                    placeholder='Please select a team to review.',
                    optionHeight=25,
                    className='mt-1 mb-3',
                    value=['Eric Colaco (CHI)'],
                    clearable=False
                )
            ],
            width=4,
            className='offset-md-2'
        )
    ]),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    html.H3('Interactive Table (Qualified Hitters)', className='text-info text-center fs-2 mt-3 mb-4'),

    dbc.Row([
        dbc.Col(
            children=[
                DataTable(
                    id='datatable-interactivity1',
                    columns=[{"name": i, "id": i,"deletable": False} for i in player_hitting_stats3.columns], 
                    data=player_hitting_stats3.to_dict('records'),
                    sort_action="native",
                    sort_mode="multi",
                    page_action="native",
                    page_current=0,
                    page_size=10,
                    style_table={'overflowX': 'auto'},
                    style_cell={'textAlign': 'center','backgroundColor': 'white','color': '#000','padding': '10px','border': '1px solid black',},
                    style_header={'backgroundColor': 'black','fontWeight': 'bold','color': 'white','textAlign': 'center'},
                    style_data_conditional=[{'if': {'row_index': 'odd'},'backgroundColor': 'lightgrey',},{'if': {'row_index': 'even'},'backgroundColor': 'white'}],
                        
                ),
            ],
            width=10,
            className='offset-md-1'
        )
    ]),
    
    dbc.Row([
        dbc.Col(
            children=[
                html.P("Please select what statistics or measures you'd like to be included in this table.",className='text-center text-dark fs-5 mt-3')
            ],
        )
    ]),

    # Dropdown Box for Column Selection
    dbc.Row([
        dbc.Col(
            children=[
                dcc.Dropdown(
                    id='column_dropdown1',
                    options=[
                        {'label': col, 'value': col} for col in player_hitting_stats3.columns
                    ],
                    multi=True,
                    placeholder='Please select a statistic(s) to review.',
                    className='mt-1 mb-3',
                ),
            ],
            width=4,
            className='offset-md-4'
        ),
    ]),

    # Data Sources and Information
    html.Div(
        children=[
            'Data Source: ',
            html.A(
                'Prospect League',
                href='https://prospectleague.com/landing/index',className='text-info fs-5'
            ),
        ],
        className='text-dark text-center fs-5 mt-5'
    ),
    html.Div(
        children=[
            'Baseball Data Abbreviations and Definitions: ',
            html.A(
                'MLB Glossary',
                href='https://www.mlb.com/glossary',className='text-info fs-5'
            )
        ],
        className='text-dark text-center fs-5 mb-2'
    )
    ],
    fluid=True
)


# Section for the Callback
@callback(
    Output('datatable-interactivity1', 'columns'),
    Output('datatable-interactivity1', 'data'),
    Output('scatter_plot','figure'),
    Output('bar_chart1','figure'),
    Input('filter-radio','value'),
    Input('team-dropdown25','value'),
    Input('stat_dropdown1','value'),
    Input('stat_dropdown2','value'),
    Input('stat_choice1','value'),
    Input('player_dropdown1','value'),
    Input('datatable-interactivity1', 'selected_columns'),
    Input('column_dropdown1', 'value'),
    Input('datatable-interactivity1', "derived_virtual_data"),
    Input('datatable-interactivity1', "derived_virtual_selected_rows"),
)

def charts(filter_value,selected_teams,stat_selection1,stat_selection2,stat_selection3,player_selection,selected_columns1, column_selection1, rows1, derived_virtual_selected_rows1):    
    if filter_value == 'all':
        filtered_data = player_hitting_stats1
    else:
        filtered_data = player_hitting_stats1[player_hitting_stats1['Qualified'] == "Yes"]

    filtered_data = filtered_data[filtered_data['Team'].isin(selected_teams)]

    if len(filtered_data) == 0 and filter_value == 'greater_than_2.7':
        filtered_data = player_hitting_stats1[player_hitting_stats1['Qualified'] == "Yes"]
    elif len(filtered_data) == 0:
        filtered_data = player_hitting_stats1
    
    if len(filtered_data) == 0:
        filtered_data = player_hitting_stats1

    if len(stat_selection3)==0:
        stat_selection3 = ['wRC']

    if len(player_selection)==0:
        player_selection = ['Eric Colaco (CHI)']

    if derived_virtual_selected_rows1 is None:
        derived_virtual_selected_rows1 = []

    if column_selection1 is None:
        column_selection1 = player_hitting_stats3.columns

    if 'Name (Team)' not in column_selection1:
        column_selection1.insert(0, 'Name (Team)')

    # Update the DataTable based on selected columns
    columns1 = [{"name": i, "id": i, "deletable": True, "selectable": True} for i in column_selection1]
    data1 = player_hitting_stats3.reset_index()[column_selection1].to_dict('records')

    # Making Batting Data Subset
    player_data_subset=player_hitting_stats1.loc[player_selection,stat_selection3].copy().reset_index()

    # Create a new DataFrame with 'Team' as a regular column
    team_column = player_hitting_stats1.loc[player_selection, 'Team'].reset_index()['Team']

    # Add the 'Team' column to the player_data_subset DataFrame
    player_data_subset['Team'] = team_column

        # Pitching Chart
    hitting_scatter_plot=px.scatter(
        filtered_data,
        x=stat_selection1,
        y=stat_selection2,
        title=' ',
        hover_name=filtered_data.index,
        color='Team',
        color_discrete_map={
            "Champion City Kings":'#044283',
            "Chillicothe Paints":'#BA0C2F',
            "Johnstown Mill Rats":'#3E342F',
            "Lafayette Aviators":'#FFC82F',
            "Danville Dans":'#D22730',
            "Dubois County Bombers":'#0C2340',
            "Full Count Rhythm":'#8BB8E8',
            "Normal CornBelters":'#2C5234',
            "REX Baseball":'#0057B7',
            "Burlington Bees":'#FFB81C',
            "Clinton LumberKings":'#00843D',
            "Illinois Valley Pistol Shrimp":'#FF8200',
            "Quincy Gems":'white',
            "Springfield Lucky Horseshoes":'#072B31',
            "Alton River Dragons":'#279989',
            "Cape Catfish":'#78BE21',
            "Jackson Rockabillys":'#84329B',
            "O'Fallon Hoots":'#010101',
            "Thrillville Thrillbillies":'#FF8F1C',
        }
    )

    hitting_scatter_plot.update_xaxes(
        title_font={
        'size': 18,
        'color': 'black'
        },
        tickfont=dict(
            size=14,
            color='black'
        ),
        showgrid=True,
        gridwidth=0.5,
        gridcolor='black',
        showline=True,
        linewidth=1,
        linecolor='black'
    )

    hitting_scatter_plot.update_yaxes(
        title_font={
        'size': 18,
        'color': 'black'
        },
        tickfont=dict(
            size=14,
            color='black'
        ),
        showline=True,
        linewidth=1,
        linecolor='black',
        showgrid=True,
        gridwidth=1,
        gridcolor='black',
    )

    hitting_scatter_plot.update_layout(
        title_font={
        'size': 24,
        'color': 'black'
        },
        title_x=0.5,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0,r=0,t=0,b=0),
        showlegend=False,
    )

    hitting_scatter_plot.update_traces(
        marker_size=11,
        marker_line_color='black',
        marker_line_width=1,
        textfont_size=14
)
    
    # Batting Chart
    batting_figure1=px.bar(
        player_data_subset,
        x=stat_selection3,
        y='Name (Team)',
        orientation='h',
        text_auto=True,
        title=' ',
        color='Team',
        color_discrete_map={
            "Champion City Kings":'#044283',
            "Chillicothe Paints":'#BA0C2F',
            "Johnstown Mill Rats":'#3E342F',
            "Lafayette Aviators":'#FFC82F',
            "Danville Dans":'#D22730',
            "Dubois County Bombers":'#0C2340',
            "Full Count Rhythm":'#8BB8E8',
            "Normal CornBelters":'#2C5234',
            "REX Baseball":'#0057B7',
            "Burlington Bees":'#FFB81C',
            "Clinton LumberKings":'#00843D',
            "Illinois Valley Pistol Shrimp":'#FF8200',
            "Quincy Gems":'white',
            "Springfield Lucky Horseshoes":'#072B31',
            "Alton River Dragons":'#279989',
            "Cape Catfish":'#78BE21',
            "Jackson Rockabillys":'#84329B',
            "O'Fallon Hoots":'#010101',
            "Thrillville Thrillbillies":'#FF8F1C',
        }
    )

    batting_figure1.update_xaxes(
        title_font={
        'size': 18,
        'color': 'black'
        },
        tickfont=dict(
            size=14,
            color='black'
        ),
        showgrid=True,
        gridwidth=1,
        gridcolor='black',
        showline=True,
        linewidth=1,
        linecolor='black'
    )

    batting_figure1.update_yaxes(
        title_text='Player(s)',
        title_font={
        'size': 18,
        'color': 'black'
        },
        tickfont=dict(
            size=14,
            color='black'
        ),
        showline=True,
        linewidth=1,
        linecolor='black',
        categoryorder='total ascending'
    )

    batting_figure1.update_layout(
        title_font={
        'size': 24,
        'color': 'black'
        },
        title_x=0.5,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0,r=0,t=0,b=0),
        showlegend=False,
    )

    batting_figure1.update_traces(
        marker_line_color='black',
        marker_line_width=1,
        textfont_size=14
)

    return columns1, data1, hitting_scatter_plot, batting_figure1
