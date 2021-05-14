import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
# from dash.dependencies import Input, Output, State
# from dash import no_update
# from flask import session, copy_current_request_context
import plotly.graph_objs as go

from server import app, server
from Covid_data import fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9

appMain_layout = html.Div([

       html.Div([
        dbc.Container([
            html.Div([
                html.Img(src=app.get_relative_path('/assets/Img/Image.jpg'), style={'width':'100%'})
            ],id = "#"
            ),

            html.Div([
            dbc.Col(html.H3("Covid overall Cases and Latest increament Cases in Country"),
                            width={'size': 12, 'offset': 0}, ),
            dbc.Row(
                dbc.Col([
                    dbc.Col(
                        dcc.Graph(id='fig1', figure=fig1),
                        width={'size':10},style={'display':'inline-block'},
                    ),
                ],width={'size': 12, 'offset': 0},style={'background-color': 'aliceblue'},
                ),
            ), 
            dbc.Row(dbc.Col(html.Hr(), width = True )),
            ], id = "page_1",
            ), 

            html.Div([
            dbc.Col(html.H3("Covid overall Cases and Latest increament Cases in State"),
                            width={'size': 12, 'offset': 0}, ),
            dbc.Row(
                dbc.Col([
                    dbc.Col(
                        dcc.Graph(id='fig2', figure=fig2),
                        width={'size':10},style={'display':'inline-block'},
                    ),
                ],width={'size': 12, 'offset': 0},style={'background-color': 'aliceblue'},
                ),
            ), 
            dbc.Row(dbc.Col(html.Hr(), width = True )),
            ], id = "page_2",
            ),

            html.Div([
            dbc.Col(html.H3("Covid Cases | Top 10 States based on Latest Increament Active cases"),
                            width={'size': 12, 'offset': 0}, ),
            dbc.Row(
                dbc.Col([
                    dbc.Col(
                        dcc.Graph(id='fig3', figure=fig3),
                        width={'size':10},style={'display':'inline-block'},
                    ),
                ],width={'size': 12, 'offset': 0},style={'background-color': 'aliceblue'},
                ),
            ), 
            dbc.Row(dbc.Col(html.Hr(), width = True )),
            ], id = "page_3",
            ),

            html.Div([
            dbc.Col(html.H3("Covid Cases | Top 10 States based on Latest Positive cases"),
                            width={'size': 12, 'offset': 0}, ),
            dbc.Row(
                dbc.Col([
                    dbc.Col(
                        dcc.Graph(id='fig4', figure=fig4),
                        width={'size':10},style={'display':'inline-block'},
                    ),
                ],width={'size': 12, 'offset': 0},style={'background-color': 'aliceblue'},
                ),
            ), 
            dbc.Row(dbc.Col(html.Hr(), width = True )),
            ], id = "page_4",
            ),

            html.Div([
            dbc.Col(html.H3("Covid Cases | Top 10 States based on Active cases"),
                            width={'size': 12, 'offset': 0}, ),
            dbc.Row(
                dbc.Col([
                    dbc.Col(
                        dcc.Graph(id='fig5', figure=fig5),
                        width={'size':10},style={'display':'inline-block'},
                    ),
                ],width={'size': 12, 'offset': 0},style={'background-color': 'aliceblue'},
                ),
            ), 
            dbc.Row(dbc.Col(html.Hr(), width = True )),
            ], id = "page_5",
            ),

            html.Div([
            dbc.Col(html.H3("Covid Cases | Top 10 States based on Positive cases"),
                            width={'size': 12, 'offset': 0}, ),
            dbc.Row(
                dbc.Col([
                    dbc.Col(
                        dcc.Graph(id='fig6', figure=fig6),
                        width={'size':10},style={'display':'inline-block'},
                    ),
                ],width={'size': 12, 'offset': 0},style={'background-color': 'aliceblue'},
                ),
            ), 
            dbc.Row(dbc.Col(html.Hr(), width = True )),
            ], id = "page_6",
            ),

            html.Div([
            dbc.Col(html.H3("Covid Cases | Top 10 States with new increament in Active cases"),
                            width={'size': 12, 'offset': 0}, ),
            dbc.Row(
                dbc.Col([
                    dbc.Col(
                        dcc.Graph(id='fig7', figure=fig7),
                        width={'size':10},style={'display':'inline-block'},
                    ),
                ],width={'size': 12, 'offset': 0},style={'background-color': 'aliceblue'},
                ),
            ), 
            dbc.Row(dbc.Col(html.Hr(), width = True )),
            ], id = "page_7",
            ),

            html.Div([
            dbc.Col(html.H3("Covid Cases | Top 10 States with new increament in Cured cases"),
                            width={'size': 12, 'offset': 0}, ),
            dbc.Row(
                dbc.Col([
                    dbc.Col(
                        dcc.Graph(id='fig8', figure=fig8),
                        width={'size':10},style={'display':'inline-block'},
                    ),
                ],width={'size': 12, 'offset': 0},style={'background-color': 'aliceblue'},
                ),
            ), 
            dbc.Row(dbc.Col(html.Hr(), width = True )),
            ], id = "page_8",
            ),

            html.Div([
            dbc.Col(html.H3("Covid Cases | Top 10 States with new increament in Death cases"),
                            width={'size': 12, 'offset': 0}, ),
            dbc.Row(
                dbc.Col([
                    dbc.Col(
                        dcc.Graph(id='fig9', figure=fig9),
                        width={'size':10},style={'display':'inline-block'},
                    ),
                ],width={'size': 12, 'offset': 0},style={'background-color': 'aliceblue'},
                ),
            ), 
            dbc.Row(dbc.Col(html.Hr(), width = True )),
            ], id = "page_9",
            ),

])
])
])

