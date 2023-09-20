# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 18:08:32 2021

@author: Gianna
"""
# 
# ps1pr6.py - Problem Set 1, Problem 6
#

def reverse(s):
    """ Takes a given string, returns it in reverse"""
    string = s[::-1]
    return string

# Problem 6 Section 2

def ends_match(s):
    """Tests if the first letter of a string matches the last letter """
    if s[0] == s[-1]:
        return True
    else:
        return False
    
# Problem 6 Section 3

def replace_start(values, new_start_vals):
    """Returns a new list combining a list of new elements
    and ending with the original values"""
    length = len(new_start_vals)
    phrase = values[length:]
    newvalues = new_start_vals + phrase 
    return newvalues

# Problem 6 Section 4

def adjust(s, length):
    """Test the length of a string, slices it and returns. 
    If the length is longer then the string, 
    repeats the last value to make up the length"""
    new = s[:length]
    stringlength = len(s)
    if length > stringlength:
        difference = length - stringlength
       # print(difference)
        new = new + (s[-1] * difference)
        return new
    else:
        return new
    
    
    
    
    
    
    
    
    