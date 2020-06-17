# report.py
# 
# Exercise 2.5

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
