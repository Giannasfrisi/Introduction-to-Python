# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:33:02 2021

@author: Gianna
"""

# 
# ps6pr3.py - Problem Set 6, Problem 3
#
# Functions that use loops
#

#Problem 3 Section 1
def BUtify(s):
    """Takes a string and returns a 
    new string which all Bs and Us are 
    uppercase"""
    
    new = ''
    for i in range(len(s)): 
        if s[i] == 'b':
            new = new + 'B'
        elif s[i] == 'u':
            new = new + 'U'
        else:
            new = new + s[i]
    return new
        
        
#Problem 3 Section 2
def diff(vals1, vals2):
    """Takes a list of non-negative numbers 
    and returns the abolsute value of the 
    difference"""
    
    len_shorter = min(len(vals1), len(vals2))
    len_longer = max(len(vals1), len(vals2))
    final = []
    
    for i in range(len_shorter): 
        difference = vals1[i] - vals2[i]
        if difference < 0:
            difference = difference  *-1
            final = final + [difference]
        else:
            final = final + [difference]

    if len(vals1) != len(vals2):
        if len(vals1) > len(vals2):
            final = final + vals1[len(vals2):]
        else: 
            final = final + vals2[len(vals1):]

    return final

#Problem 3 Section 3
def index(elem, seq):
    """Returns the index of the first 
    occurance of the elem in the sequence"""
    
    for i in range(len(seq)):
        if seq[i] == elem:
            return i
    
    return -1 
        

#Problem 3 Section 4
def square_evens(vals):
    """Takes a list of integers and 
    modfies the internals of the list 
    so that evens are replaced with 
    their squares, odds are unchanged"""
    
    final = []
    for i in range(len(vals)):
        if vals[i] % 2 == 0:
            vals[i] = vals[i]**2
        
            
    





