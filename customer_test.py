from dataclasses import dataclass
import json, re, csv
from datetime import datetime as dt
from collections import namedtuple, Counter, defaultdict
from typing import List, Dict

'''
    Objects:
    Transaction, Merchant

    Variables:

    merchants : Dictionary, key = merchantId, val = Merchant object
    tags: all possible tags
    data_with_geo: all transactions with geo info
    spending: all transactions without income
    spending_transactions: array of Transaction objects created from spending
    tag_merchant_sorted: Dict, key = tag, val = (merchant, amount), sorted by amount in descending order

'''

TRANS = './data/rich_girl.json'
reg = re.compile('\d{4}-\d{2}-\d{2}')
Transaction = namedtuple('Transaction', ['tags', 'lon', 'lat',
                                         'storeName',
                                         'storeID',
                                         'amount',
                                         'date',  # a datetime object, allow easy access of month, day
                                         ])


@dataclass
class Merchant:
    tags: List[str]
    lon: float = 0
    lat: float = 0
    name: str = ''
    store_id: str = ''
    amount: float = 0
    frequency: int = 0

    def incFreq(self):
        self.frequency += 1
    
    def incAmount(self, amount:float):
        self.amount += amount


# infomation for plots
info = {'categoryTags': [],
        'locationLongitude': [],
        'locationLatitude': [],
        'merchantName': [],
        'merchantId': [],
        'currencyAmount': [],
        'originationDateTime': [],
        }

data_with_geo, tags = {}, set()
# information for each transaction as a Transaction object
spending_transactions = []


# clean date format
def createDate(input: str):
    reg = re.compile('\d{4}-\d{2}-\d{2}')
    m = reg.match(input).group(0)
    return dt.strptime(m, '%Y-%m-%d')

for data in data_with_geo:
    transacs.append(
        Transaction(*[createDate(data[k]) if k == 'originationDateTime' else data[k] for k in info.keys()])
    )

# Write all data to files
def createDataFiles() -> None:
    def write_to_file(data: dict, filename: str) -> None:
        with open(f'./data/{filename}.json', 'w') as f:
            json.dump(data, f)
    filenames = ['data_for_plots', 'brand_frequency',
                 'location_frequency', 'spending', 'tags']
    all_data = [info, freq_brand, freq_location, spending, list(tags)]

    for f, d in zip(filenames, all_data):
        write_to_file(d, f)


with open(TRANS) as f:
    result = json.load(f)['result']


# Filter out transactions without geo info
data_with_geo = list(filter(lambda data: 'locationLongitude' in data, result))
# Filter out income but keep transcs without geo info for pie chart
spending = list(
    filter(lambda data: data['currencyAmount'] >= 0 and 'Income' not in data['categoryTags'] and 'Transfer' not in data['categoryTags'],
           result))

for k in info.keys():
    info[k] = [data[k] for data in data_with_geo]

# DateTime is not needed for the map
merchant_info : Dict[str, List] = {k: info[k] for k in info.keys() if k != 'originationDateTime'}

merchants:Dict[str, Merchant] = {}

for m in data_with_geo:
    mID:str = m['merchantId']
    # If the object is already created, update the value
    if mID in merchants:
        merchants[mID].incAmount(m['currencyAmount'])
        merchants[mID].incFreq()
    else: 
        temp = [ m[k] for k in merchant_info.keys() ]
        merchants[m['merchantId']] = Merchant(*temp) 

# transactions without incomes
spending_transactions = []
for data in spending:
    spending_transactions.append(
        Transaction(*[createDate(data[k]) if k ==
                        'originationDateTime' else data.get(k, None) for k in info.keys()])
    )

tags.update(*[t.tags for t in spending_transactions])


fieldnames = ['date', 'amount', 'tag']

def writeCSV():
    with open('test.csv', 'w') as csv_file:

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for t in spending_transactions: 
            writer.writerow({'date': t.date.strftime('%m-%d'),
                        'amount': t.amount, 'tag': t.tags[0]})


merchant_name_amount = defaultdict(lambda:0)
tag_merchant_name = {tag:set() for tag in tags}
tag_merchant_sorted = {tag:[] for tag in tags}

for transac in spending_transactions:
    merchant_name_amount[transac.storeName] += transac.amount
    tag_merchant_name[transac.tags[0]].add(transac.storeName)


name_amount = merchant_name_amount.items()


for tag, ms in tag_merchant_name.items():
    for m in ms:
        tag_merchant_sorted[tag].append((m, merchant_name_amount[m]))

for k,v in tag_merchant_sorted.items():
    tag_merchant_sorted[k] = sorted(v, key=lambda x: x[1], reverse=True)
