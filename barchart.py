import plotly.graph_objects as go
from customer_test import info
from plotly.offline import plot


def extract(info, category, keyword):
    updated_info = {'categoryTags': [],
                    'locationLongitude': [],
                    'locationLatitude': [],
                    'merchantName': [],
                    'merchantId': [],
                    'currencyAmount': [],
                    'originationDateTime': [],
                    }
    for i in range(len(info['categoryTags'])):
        if keyword in info[category][i]:
            for k in updated_info.keys():
                updated_info[k].append(info[k][i])
    return updated_info


def sum_currency(info):
    amount = 0
    for i in range(len(info['categoryTags'])):
        amount += info['currencyAmount'][i]
    return amount


entertainment_info = extract(info, 'categoryTags', 'Entertainment')
food_info = extract(info, 'categoryTags', 'Food and Dining')
home_info = extract(info, 'categoryTags', 'Home')
shopping_info = extract(info, 'categoryTags', 'Shopping')
shopping_amount = home_amount = food_amount = entertainment_amount = Tim_amount = Walmart_amount = 0
Tim_info = extract(info, 'merchantName', 'Tim Hortons')
Walmart_info = extract(info, 'merchantName', 'Wal')

entertainment_amount = sum_currency(entertainment_info)
home_amount = sum_currency(home_info)
food_amount = sum_currency(food_info)
Tim_amount = sum_currency(Tim_info)
Walmart_amount = sum_currency(Walmart_info)
shopping_amount = sum_currency(shopping_info)

amounts1 = []
amounts2 = []

enter = extract(info, 'categoryTags', 'Entertainment')
food = extract(info, 'categoryTags', 'Food and Dining')
shop = extract(info, 'categoryTags', 'Shopping')
ae = sum_currency(enter)
af = sum_currency(food)
ash = sum_currency(shop)  # shopping amount
ep = ae / (ae + af + ash)
fp = af / (ae + af + ash)
sp = ash / (ae + af + ash)  # shopping percent
budget = 3000
eb = budget * ep
fb = budget * fp
sb = budget * sp  # shopping budget


julyinfo = extract(info, 'originationDateTime', '2019-07')

info7e = extract(julyinfo, 'categoryTags', 'Entertainment')
info7d = extract(julyinfo, 'categoryTags', 'Food and Dining')
info7s = extract(julyinfo, 'categoryTags', 'Shopping')

amounts7 = []
amounts7.append(sum_currency(info7d))
amounts7.append(sum_currency(info7e))
amounts7.append(sum_currency(info7s))

fig = {
    'data': [go.Bar(name='Last month', x=['Food and Dining', 'Entertainment', 'Shopping'], y=[fb, eb, sb], marker_color='gold'),
             go.Bar(name='Your plan', x=['Food and Dining', 'Entertainment', 'Shopping'], y=amounts7,
                    width=[0.6, 0.6, 0.6], marker_color='darkorange')],
    'layout': go.Layout(barmode='overlay')
}
