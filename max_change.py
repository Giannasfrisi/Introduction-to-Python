# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 18:34:11 2021

@author: Gianna
"""

def max_change_day(prices):
    """returns the largest change in price 
    over a single day"""
    
    difference = 0
    for i in range(len(prices)):
        x = i+1
        if x < len(prices):
            if prices[x] - prices[i] > difference:
                difference = prices[x] - prices[i]
            
    return difference