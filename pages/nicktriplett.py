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
        html.H1('About Me - Nick Triplett',className='text-center text-dark mt-3 mb-2 fs-1'),
         html.Div(
            children=[
                '(618) 944-1952 | nicholas.triplett@siu.edu | ',
                html.A(
                    "linkedin.com/in/nicholas-triplett/",
                    href='https://www.linkedin.com/in/nicholas-triplett/',className='text-info fs-5'
                ),
        ],
        className='text-dark text-center fs-5 mt-2 mb-4'
        ),
        dbc.Row([
            dbc.Col(
                html.Img(
                    src=dash.get_asset_url('my-image.jpg'),
                    style={
                        'width':'250px',
                        'height':'375px',
                        'margin':'auto',
                        'vertical-align':'top',
                        'object-fit':'contain'}
                ),
                width={'size': 2},
                className='d-flex justify-content-center align-items-center'
            ),
            ],
            justify='center'
        ),
        html.P("Hey! My name is Nick Triplett, and I’m the creator of this dashboard! I’m 23 years old, I’m from Southern Illinois, and I’m a current graduate student striving to make a dream come true. Oh, and I’m a HUGE sports fan (no, really… I might be the biggest sports fan I know).",className='text-center text-dark mt-4 mb-2 fs-6'),
        html.P("Growing up, my sports background wasn’t generated through self-competition, but rather inherited through watching occasional events. From being introduced to NASCAR and St. Louis Cardinals at the age of five, to finding personal sports passions, the industry has always impacted my heart. I didn’t really know what I wanted to be when I was younger, but I knew that I wanted sports to play a large role in my life. Additionally, I noticed that there was one thing that always garnered my attention when finding associations towards my love of sports: the numbers and trends associated with them.",className='text-center text-dark mt-3 mb-2 fs-6'),
        html.P("This led me to pursue a career in analytics. Since then, I received a Bachelor’s degree in Business Analytics from Southern Illinois University – Carbondale (graduating with a 4.00 GPA), and I’ve started working towards an online Master’s degree in Business Analytics from there. During this time, I’ve learned how to clean and manipulate data, formulate code, perform statistical analysis, and apply these resources and information to businesses/teams and their various problems and questions. During this time, I’ve worked with tools, such as Microsoft Excel, Tableau, Python, SQL, and R (among others).",className='text-center text-dark mt-3 mb-2 fs-6'),
        html.P("In 2023, I received my first opportunity to work alongside a sports team by becoming a Data Analytics Intern for the Thrillville Thrillbillies, a summer wood-bat college baseball team located within the Prospect League. There, I assisted with the formulation of the organization’s analytics functions and experienced what work is necessary to ensure that everything runs smoothly for an organization in all aspects. I gained knowledge in working with baseball software, improved my analytical skills, and had significant involvement in operational and technical work. Over the two years that I was involved with the team, our organization won two divisional titles through the utilization of this website, advanced statistics, and other data that I created and accessed.",className='text-center text-dark mt-3 mb-4 fs-6'),
        dbc.Row([
            dbc.Col(
                html.Img(
                    src=dash.get_asset_url('thrillbillies-operation-image.jpg'),
                    style={
                        'width':'100%',
                        'vertical-align':'top',
                        'object-fit':'contain'}
                ),
                width={'size': 5}
            ),
            ],
            justify='center'
        ),
        html.P("In 2024, I was a Business Intelligence & Data Analytics Intern for the Pittsburgh Penguins. Using the skills and attributes that I developed through this website and my previous experiences, I was able to create impactful, long-lasting dashboards for the organization’s Business Operations divisions, won an intern project competition with a concept that was introduced to the team’s Research and Development department, and conducted various, data-related projects with many tools. My time with the Penguins is unforgettable, and I’m not only thankful for my time being with them, but also prepared for future opportunities because of the lessons learned and the additional knowledge gained from this time.",className='text-center text-dark mt-4 mb-2 fs-6'),
        html.P("All of this leads me to who and where I am today. As I continue working towards my degree and bettering my analytical knowledge and skills, I remain committed and motivated towards my dream. Ultimately, I desire to become a data/business analyst in the professional sports industry, where I can not only positively impact the organization that I work for, but also share my love of sports to others. I’m so thankful for God, as well as my family and friends, for establishing who I am today, and I’m excited to see what comes next.",className='text-center text-dark mt-3 mb-2 fs-6'),
        html.P("All of this leads me to who and where I am today. As I continue working towards my degree and bettering my analytical knowledge and skills, I remain committed and motivated towards my dream. Ultimately, I desire to become a data/business analyst in the professional sports industry, where I can not only positively impact the organization that I work for, but also share my love of sports to others. I’m so thankful for God, as well as my family and friends, for establishing who I am today, and I’m excited to see what comes next!",className='text-center text-dark mt-3 mb-2 fs-6'),
        html.P("Colossians 3:23-24",className='text-center text-dark mt-3 mb-3 fs-6'),
    ]
)
