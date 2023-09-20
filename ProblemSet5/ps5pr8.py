# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:33:03 2021

@author: Gianna
"""

#
# ps5pr8.py - Problem Set 5, Problem 8
#
# Processing sequences with loops
#

#Problem 8 Section 1 
def num_multiples(m, values):
    """Takes a positive integer and returns 
    the amount of integers that are 
    multiples of value m"""
    count = 0
    i = 0
    for i in range(len(values)):
        if values[i] % m == 0:
            count += 1
            
    return count

#Problem 8 Section 2
def add_stars(s):
    """Takes a string s and returns the 
    string adding a asterisk between each 
    character"""
    result = ''
    for i in range(len(s)):
        result = result + s[i] + '*'
          
    return result[:-1]
    

#Problem 8 Section 3 
def compare(s1, s2):
    """Takes two strings and returns 
    the number of differences in the 
    two strings"""

    result = 0
    len_shorter = min(len(s1), len(s2))
    len_longer = max(len(s1), len(s2))

    for i in range(len_shorter):
        if s1[i] != s2[i]:
            result+=1
    
    if len(s1) != len(s2):
        result += len_longer - len_shorter
        
    return result  
   
#Problem 8 Section 4 
def begins_with(prefix, wordlist):
    """Takes a string and returns the 
    words in a list that start with 
    the prefix"""
   
    result = [] 
    for i in range(len(wordlist)):
        length = len(prefix)
        test_word = wordlist[i]
        if prefix == test_word[:length]:
            result = result + [test_word]
        
    return result
      
            
    
    
    
    
    
    
    
    
    
    
    
    
    