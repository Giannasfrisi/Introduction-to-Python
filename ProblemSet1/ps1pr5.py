# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 16:59:16 2021

@author: Gianna
"""

# 
# ps1pr5.py - Problem Set 1, Problem 5
#

def last_first(values):
    """ Took a series of values, and returns the last 
    value and the first value """
    last = values[-1]
    first = values[0]
    return [last, first]

    
def every_other(values):
    """ Slices a list of values, returns every other """
    newvalues = values[0::2]
    return newvalues

def begins_with(word, prefix):
    """ Tests if a word starts with a given prefix"""
    length = len(prefix)
    phrase = word[:length]
    if phrase == prefix:
        return True
    else:
        return False
    

    