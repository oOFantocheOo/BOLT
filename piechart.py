import plotly.graph_objects as go
import json
from customer_test import info, tags, spending_transactions

colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']

# total_amount = sum([ t.date.month for t in spending_transactions])
tag_amount = { t:0 for t in tags }

for tran in spending_transactions:
    for tag in tran.tags:
        tag_amount[tag] += tran.amount

labels = list(tag_amount.keys())
values = list(tag_amount.values())



# def get_percentage(amt:float) -> float:
    


fig = go.Figure(data=[go.Pie(labels=labels, 
                            values=values,
                            textinfo='label',
                            textfont_size=20,
                            hoverinfo='value+percent',
                            marker=dict(colors=colors))],
                )

# Extract ranking for each category


