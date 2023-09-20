# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 18:05:45 2021

@author: Gianna
"""

def min_day(prices):
    """compares a list of prices and returns
    the day of the smallest price"""
    
    output = []
    day = 0
    final = 0
    for i in range(len(prices)):
        if prices[0] > prices[i]:
            day = i
            final = prices[i]
            output = [day, final]
    
    return output


        
    