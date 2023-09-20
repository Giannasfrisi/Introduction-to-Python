# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:32:09 2021

@author: Gianna
"""

def avg_price(prices):
    final = 0
    for i in range(len(prices)):
        final = final + prices[i]
    
    average = final/len(prices)
