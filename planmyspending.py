#Bootstrap Component for "plan my spending"

planMySpending = html.Div(
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
            ],className="mb-3",
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
    ]
)