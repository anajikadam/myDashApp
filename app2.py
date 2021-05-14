import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


# app = dash.Dash(__name__, suppress_callback_exceptions=True)
from server import app, server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='main-page-content')
])


index_page = html.Div([
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
])
from app1 import layout1
page_1_layout = html.Div([
    html.H1('Page 1'),
    dcc.Link(html.I(className="fa fa-home fa-2x"), href='/'),
    html.Hr(),
    layout1,
    ])

from layout_1 import appMain_layout
page_2_layout = html.Div([
    html.H1('Page 2'),
    dcc.Link(html.I(className="fa fa-home fa-2x"), href='/'),
    html.Hr(),
    appMain_layout,
    html.Br(),
])

# Update the index
@app.callback(dash.dependencies.Output('main-page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return index_page


if __name__ == '__main__':
    app.run_server(debug=True)
