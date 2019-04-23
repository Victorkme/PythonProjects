# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 20:40:19 2019

@author: User1
"""
prices = [7,6,5,4,3,5]

def maxProfit(prices):
    buy = prices[0]
    sell = 0
    if not prices:
        return 0
    for num in prices:
        if num < buy:
            buy,sell = num,num
        elif num > sell:
            sell = num
    return (sell-buy)

print(maxProfit(prices))
