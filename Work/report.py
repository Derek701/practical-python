# report.py
# 
# Exercise 2.7

import csv

def read_portfolio(filename):
    '''Opens a given portfolio file and reads it into a list of dictionaries'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = dict(name=row[0], shares=int(row[1]), price=float(row[2]))
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    '''Reads a set of prices into a dict where keys are stock names and values are stock prices'''
    price = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                price[row[0]] = float(row[1])
            except IndexError:
                print("Couldn't parse", row)
    return price

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
total_cost = 0.0
current_value = 0.0

for s in portfolio:
    total_cost += s['shares']*s['price']            # Total cost 44671.15
    current_value += s['shares']*prices[s['name']]  # Current value 28686.1

total_gain = current_value - total_cost             # Gain/loss -15985.05
