# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 20:46:29 2021

@author: Gianna
"""

def find_tts(prices):
    """Finds the best day to buy and sell stocks 
    resulting in the largest profit"""
    
    difference = 0
    profit = 0
    output = []
    day_one = 0
    day_two = 0
    for i in range(len(prices)):
        for j in range(len(prices)):
            if prices[j] > prices[i]:
                if j > i:
                    difference = prices[j] - prices[i]
                    if difference > profit:
                        profit = difference
                        day_one = i
                        day_two = j
            
    output = [day_one, day_two, profit]
    return output