import json
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output
import piechart, barchart, maptest
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


pieFig = go.Pie(labels=piechart.labels,
             values=piechart.values,
             textinfo='label',
             textfont_size=15,
             hoverinfo='value+percent',
             marker=dict(colors=colors))


piechart = dcc.Graph(
    id='piechart',
    figure={
        'data': [pieFig],
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

barchart = dcc.Graph(
    id='barchart',
    figure=barchart.fig
)

spending_map = dcc.Graph(
    id='spending-map',
    figure={
        'data':[maptest.mapFig],
        'layout':maptest.mapLayout
    }
)

mapbox = dbc.Card(
    dbc.CardBody([
        html.H4('My spending footprint'),
        spending_map
    ]),
    color="success",
    # outline=True
    # className="pretty_container seven columns",
)


pieCard = dbc.Card(
    dbc.CardBody([
        html.H4('Spending Per Category'),
        piechart
    ]),
    color="success",
    outline=True
    # className="pretty_container seven columns",
)

barCard = dbc.Card(
    dbc.CardBody([
        html.H4('Plan for Next Month'),
        barchart
    ]),
    color="success",
    outline=True
)

plan_spending = dbc.Card(
    [
        dbc.InputGroup(
            [
                dbc.InputGroupAddon("Spending for", addon_type="append"),
                dbc.Select(
                    options=[
                        {"label": "First Quarter", "value": 1},
                        {"label": "Second Quarter", "value": 2},
                        {"label": "Third Quarter", "value": 3},
                        {"label": "Fourth Quarter", "value": 4},
                    ]
                )
            ], className="mb-3",
        ),

        dbc.InputGroup(
            [
                dbc.InputGroupAddon("Total: $", addon_type="prepend"),
                dbc.Input(placeholder="Amount", type="number"),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupAddon("Food", addon_type="prepend"),
                dbc.Input(placeholder="Amount", type="number"),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupAddon("Entertainment", addon_type="prepend"),
                dbc.Input(placeholder="Amount", type="number"),
            ],
            className="mb-3",
        ),
        dbc.InputGroup(
            [
                dbc.InputGroupAddon("Shopping", addon_type="prepend"),
                dbc.Input(placeholder="Amount", type="number"),
            ],
            className="mb-3",
        ),
    ],
    color="success",
    outline=True
)


ranking = dbc.Card(
    [
        dbc.CardHeader('Your favorite stores'),
        dbc.ListGroup([
                         
                     ],
                     id='rankingGroup'
                     )],
    color="success",
    outline=True

)

imageCard = dbc.Card(
    dbc.CardImg(src="assets/Capture.PNG"),
    color="success",
    outline=True
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Back To Online Banking", href="#"))],
        brand="Where My Money Went",
        brand_href="#",
        color="primary",
        dark=True,
)

app.layout = html.Div(
    # Title
    [   navbar,
        html.Br(),
        html.Div([html.H1("Where My Money Went")],
              style={"textAlign": "center"}),

    # Pie chart and ranking
     dbc.Row([
         dbc.Col(pieCard,  width={"size": 7, "offset": 0}),
         dbc.Col(ranking,  width={"size": 3, "order": "last"})
     ], justify='center'),

     html.Br(),

     # Mapbox
     dbc.Row(dbc.Col(
         mapbox, width={"size": 10}),
         justify='center'),

     html.Br(),

     dbc.Row(dbc.Col(
         imageCard, width={"size": 10}),
         justify='center'),

     html.Br(),

    # Bar chart and plan input group
     dbc.Row([
         dbc.Col(barCard, width={"size": 7, "offset": 0}),
         dbc.Col(plan_spending,
                 width={"size": 3, "order": "last"})
         ],
         justify='center'
     ),

     ],
    style={'backgroundColor': 'rgb(250,250,250)'}
)


@app.callback(
    Output('rankingGroup', 'children'),
    [Input('piechart', 'clickData')]
)
def ranking_by_tag(clickData):
    ranking = []
    if clickData:
        ranking = []
        result = tag_merchant_sorted[clickData['points'][0]['label']]
        if result != None:
            for (merchant, amount) in result:
                ranking.append(dbc.ListGroupItem(f'{merchant}      ${amount:.2f}'))
    return ranking


if __name__ == '__main__':
    app.run_server(debug=True)
