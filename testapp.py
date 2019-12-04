import json


import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from piechart import labels, values
from customer_test import tag_merchant_sorted

external_stylesheets = [dbc.themes.FLATLY]
colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

labels = labels
values = values

# title = dict(text='Spending per category',
#              position="top center", font=dict(size=25))

fig = go.Pie(labels=labels,
             values=values,
             textinfo='label',
             textfont_size=15,
             hoverinfo='value+percent',
             marker=dict(colors=colors))


data = [
    dict(
        labels=labels,
        values=values,
        hole=0.3,
        textinfo='label',
        textfont_size=20,
        hoverinfo='value+percent',
        marker=dict(colors=colors),
        type='pie',
    ),
]

piechart = dcc.Graph(
    id='piechart',
    figure={
        'data': [fig],
        'layout': {
            'margin': {
                'l': 20,
                'r': 20,
                'b': 10,
                't': 10
            },
        }
    },
)


piegraph = dbc.Card(
    dbc.CardBody([
        html.H4('Spending per category'),
        piechart
    ]),
    color="success",
    outline=True
    # className="pretty_container seven columns",
)

click_data = dbc.Card(
    dbc.CardBody(html.Pre(id='click-data', style=styles['pre'])),
    className="mb-3",
    color="success",
    outline=True
)
# click_data = html.Div(
#     [
#         html.Pre(id='click-data', style=styles['pre']),
#     ],
#     )

app.layout=html.Div(
    [html.Div([html.H1("Where Did My Money Go")],
             style={"textAlign": "center"}),

    dbc.Row([
        dbc.Col(piegraph,  width={"size": 7, "offset": 0}),
        dbc.Col(click_data,  width={"size": 3, "order": "last"})
    ], justify='center')]
)

@app.callback(
    Output('click-data', 'children'),
    [Input('piechart', 'clickData')])
def display_click_data(clickData):
    return json.dumps(clickData, indent = 2)


if __name__ == '__main__':
    app.run_server(debug = True)
