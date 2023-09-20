# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 20:06:38 2021

@author: Gianna
"""

def any_above(prices, threshold):
    """Tests to see if any prices are larger than the threshold"""
    
    for i in range(len(prices)):
        if prices[i] > threshold:
            return True
    
    return False