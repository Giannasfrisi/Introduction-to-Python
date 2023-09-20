# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 17:33:38 2021

@author: Gianna
"""

# 
# ps2pr3.py - Problem Set 2, Problem 3
#
# practice writing non-recursive functions
#

#Problem 3 Section 1

def longer(s1, s2):
    """Takes inputs two string values s1 and s2, and 
    returns the string with the longer length"""
    
    lengths1 = 0
    lengths2 = 0
    
    def len(s1):
        return lengths1
    
    def len(s2):
        return lengths2
    
    if lengths1 > lengths2:
        return s1 
    elif lengths1 < lengths2:
        return s2
    elif lengths1 == lengths2:
        return s1
        
#Problem 3 Section 2

def swap_halves(s):
    """Takes a string input s and returns 
    a string whose first half is s's second half 
    and whose second half is s's first half"""
    
    x = len(s)//2
    
    if x % 2 == 0: 
        return s[x:]+ s[:x]
    else: 
        return s[x:] + s[:x]
    
#Problem 3 Section 3

def repeat_one(values, index, num_times):
    """Takes as inputs a list values, an integer index 
    and a positive integer num_times, and returns a new list 
    which the element has been repeated num_times times"""
    
    return values[:index] + [values[index]] *  (num_times - 1) + values[index:]

    
    
    
    