# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 20:23:52 2021

@author: Gianna
"""

# 
# ps2pr5.py - Problem Set 2, Problem 5
#
#  Fun with recursion, part 2
#

#Problem 5 Section 1
def dot(vals1, vals2):
    """Takes two input values 
    and returns the dot product"""
    
    if len(vals1) != len(vals2) or vals1 == [] or vals2 == []:
        return 0.0

    
    else:
        dot_rest = dot(vals1[1:], vals2[1:])
        return (vals1[0]*vals2[0]) + dot_rest
        
    
#Problem 5 Section 2
def any_odd(vals):
    """Takes values and uses recursion 
    to determind if the values are odd"""
  
    if vals == []:
        return False
    else:
        odd_rest = any_odd(vals[1:])
        if vals[0] % 2 == 0:
            return odd_rest
        else:
            return True
    
  
#Probelem 5 Section 3
def process(vals):
    """Takes a list of values and 
    uses recursion to return each 
    odd number with its square"""
    
    if vals == []:
        return []
    else:
        process_rest = process(vals[1:])
        if vals[0] % 2 == 0:
            return [vals[0]] + process_rest
        elif vals[0] % 2 != 0:
            return [(vals[0]**2)] + process_rest
        
    
    
    
    
    
    
    
    
    
    
    
    
    
