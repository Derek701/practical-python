# report.py
# 
# Exercise 2.23

import csv

def read_portfolio(filename):
    '''Opens a given portfolio file and reads it into a list of dictionaries'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        select = ['name', 'shares', 'price']
        indices = [ headers.index(colname) for colname in select ]
        portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
    for s in portfolio:
        s['shares'] = int(s['shares'])
        s['price'] = float(s['price'])
    return portfolio

def read_prices(filename):
    '''Reads a set of prices into a dict where keys are stock names and values are stock prices'''
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                continue # Skip empty line without printing error message
    return prices

def make_report(stocks, prices):
    ''' Takes a list of stocks and dict of prices and returns a list of tuples with report data'''
    report = []

    for s in stocks:
        holding = (s['name'], s['shares'], prices[s['name']], prices[s['name']]-s['price'])
        report.append(holding)
    return report

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)
headers = ('Name', 'Shares', 'Price', 'Change')

cost = sum([ s['shares'] * s['price'] for s in portfolio ])         # Total cost 44671.15
value = sum([ s['shares'] * prices[s['name']] for s in portfolio ]) # Current value 28686.1
gain = value - cost                                                 # Gain/loss -15985.05

header = f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}'
separator = f'{"":->10s} {"":->10s} {"":->10s} {"":->10s}'

print(header)
print(separator)
for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {"$"+str(price):>10s} {change:>10.2f}')
