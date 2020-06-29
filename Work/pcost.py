#!/usr/bin/env python3
# pcost.py
# 
# Exercise 4.4

import report

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    portfolio = report.read_portfolio(filename)
    return sum( [s.shares * s.price for s in portfolio] )

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {argv[0]} portfolio_filename')
    print('Total cost', portfolio_cost(argv[1]))

if __name__ == "__main__":
    import sys
    main(sys.argv)
