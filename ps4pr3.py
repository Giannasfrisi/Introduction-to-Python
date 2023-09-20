# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 12:50:28 2021

@author: Gianna
"""

#
# ps4pr3.py - Problem Set 4, Problem 3
#
# Functions that process binary numbers
#


#Problem 3 Section 1
def count_evens_rec(binvals):
    """Takes a string and returns the amount 
    of even numbers using recursion"""
    
    if binvals == []:
        return 0
    else:
        rest = count_evens_rec(binvals[1:])
        first_string = binvals[0]
        if first_string[-1] == '0':
            return 1 + rest
        else:
            return rest
    
    
#Problem 3 Section 2
def count_evens_lc(binvals):
    """Takes a string and returns the amount 
    of even numbers using LC"""
    
    lc = [1 for x in binvals if x[-1] == '0']
    return sum(lc)
    
    
#Problem 3 Section 3
def  add_bitwise(b1, b2):
    """Performs addition of B1 and B2"""
    
    if b1 == b2 == '':
        return ''
    elif b1 == '':
        return b2
    elif b2 == '':
        return b1
    else:
        rest = add_bitwise(b1[:-1], b2[:-1])
        if b1[-1] == '0':
                return rest + b2[-1]
        elif b2[-1] == '0':
                return rest + '1'
        else:
            # when b1[-1] == '1'
            if b2[-1] == '0':
                return rest + b1[-1]
            else:
                return add_bitwise(rest, '1') + '0'
    
    