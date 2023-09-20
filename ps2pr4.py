# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 16:56:00 2021

@author: Gianna
"""

# 
# ps2pr4.py - Problem Set 2, Problem 4
#
# Fun with recursion, part 1
#

#Problem 4 Section 1

def mult(vals):
    """Takes a list of numbers and uses recursion 
   to return the values multiplied together"""
    if len(vals) == 1:
        return vals[0]
    else:
        mult_rest = mult(vals[1:]) * vals[0]
        return mult_rest
    
#Problem 4 Section 2

def add_stars(s):
    """Takes a string and uses recursion to return 
    a string formed by adding a star"""
    if len(s) < 2:
        return s
    else: 
        stars_rest = add_stars(s[1:]) 
        return s[0] + '*' + stars_rest
        
    
        