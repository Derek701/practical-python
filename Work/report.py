#!/usr/bin/env python3
# report.py
# 
# Exercise 4.8

from fileparse import parse_csv
from stock import Stock
import tableformat

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of Stock instances with
    name, shares, and price.
    '''
    with open(filename) as lines:
        portdicts = parse_csv(lines, select=['name','shares','price'], types=[str,int,float])
        portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
        return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices
    '''
    with open(filename) as lines:
        return dict(parse_csv(lines, types=[str, float], has_headers=False))

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    report = []
    for s in portfolio:
        holding = (s.name, s.shares, prices[s.name], prices[s.name]-s.price)
        report.append(holding)
    return report

def print_report(reportdata, formatter):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfoliofile, pricefile, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(argv):
    if len(argv) < 3:
        raise SystemExit(f'Usage: {argv[0]} portfoliofile pricefile [format]')
    elif len(argv) == 3:
        portfolio_report(argv[1], argv[2], 'txt')
    else:
        portfolio_report(argv[1], argv[2], argv[3])

if __name__ == "__main__":
    import sys
    main(sys.argv)
