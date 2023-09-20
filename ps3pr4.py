# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 00:30:57 2021

@author: Gianna
"""

# 
# ps3pr4.py - Problem Set 3, Problem 4
#
# More algorithm design!
#

#Problem 4 Section 1

def index(elem, seq):
    """Takes an element and a sequence and 
    returns the first occurance of the element 
    in the sequence"""
    
    if seq == []:
        return -1
    elif seq == '':
        return -1
    else:
        index_rest = index(elem, seq[1:])
        if seq[0] == elem:
            occurance = 0
            return occurance  
        else:
            occurance = 1 + index_rest
            return occurance
       
        # if len(seq) == occurance - 1:
        #     return -1 
   
#Problem 4 Section 2

def index_last(elem, seq):
    """Takes an element and a sequence and 
    returns the last occurance of the element 
    in the sequence"""
  
    if seq == []:
        return -1
    elif seq == '':
        return -1
    else:
        index_rest = index(elem, seq[1:])
        if seq[-1] == elem:
            return len(seq) - index_rest
        else: 
            return index_rest 
    
#Problem 4 Section 3

def jscore(s1, s2):
    """Takes two strings and returns 
    the jotto score"""
    
    score = 0
    if s1 == '':
        return 0
    elif s2 == '':
        return 0
    else:        
        if s1[0] in s2:
            return (score + 1), rem_first
        else:
            return rem_first(s1, s2[1:])
        
        return score
        
def rem_first(elem, values):
    """removes the first occruance 
    of elem from values"""
    
    if values == '':
        return ''
    elif values[0] == elem:
        return values[1:], (score + 1)
    else:
        rem_rest = rem_first(elem, values[1:])
        return values[0] + rem_rest
        

    
    
    
    
    
    