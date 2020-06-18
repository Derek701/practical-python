# report.py
# 
# Exercise 3.1

import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        select = ['name', 'shares', 'price']
        types = [str, int, float]
        indices = [ headers.index(colname) for colname in select ]
        portfolio = [ { colname: func(row[index]) for colname, func, index in zip(select, types, indices) } for row in rows ]
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices
    '''
    prices = {}
    with open(filename) as f:
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

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print(f'{"":->10s} {"":->10s} {"":->10s} {"":->10s}')
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {"$"+str(price):>10s} {change:>10.2f}')

print_report(make_report(read_portfolio('Data/portfolio.csv'), read_prices('Data/prices.csv')))
