# pcost.py
# 
# Exercise 1.31

import os

def portfolio_cost(filename):
    f = open(filename, 'rt')
    headers = next(f)
    total_cost = 0
    for line in f:
        row = line.split(',')
        try:
            total_cost += int(row[1]) * float(row[2])
        except ValueError:
            print("Couldn't parse", row)
    f.close()
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost', cost)
