# stock.py
# 
# Exercise 4.1

class Stock:
    '''
    An instance of a stock holding consisting of name, shares, and price.
    '''
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
