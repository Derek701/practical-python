# pcost.py
# 
# Exercise 1.32

import csv

def portfolio_cost(filename):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    total_cost = 0
    for row in rows:
        try:
            total_cost += int(row[1]) * float(row[2])
        except ValueError:
            print("Couldn't parse", row)
    f.close()
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost', cost)
