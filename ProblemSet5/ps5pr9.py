# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 23:43:47 2021

@author: Gianna
"""

#
# ps5pr9.py - Problem Set 5, Problem 9
#
# Choosing the correct type of loop
#

#Problem 9 Section 1 
def log(b, n):
    """Uses a loop to compute and 
    return the logarithm to the base 
    of b of a number n"""
    
    result = 0
    while n > 1:
        result += 1
        p = b
        n = n//b
        print('dividing', p*n, 'by', b, 'gives', n)
        
    return result

#Problem 9 Section 2
def add_powers(m, n):
    """Takes two integers and adds 
    together the first m powers of n 
    and returns the sum"""
    
    result = 0
    for p in range(m):
         a = n**p
         result = result + a
         print(n, '**', p, '=', a)
             
    return result 