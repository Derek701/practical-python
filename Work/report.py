# report.py
# 
# Exercise 2.6

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
