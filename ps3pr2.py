# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:31:39 2021

@author: Gianna
"""

# 
# ps3pr2.py - Problem Set 3, Problem 2
#
# Algorithm design
#

#Problem 2 Section 1

def abs_list_lc(values):
    """Uses list comprehension to return 
    the absolute values of a list"""
    lc = [abs(x) for x in values] 
    return lc 
    

#Problem 2 Section 2

def  abs_list_rec(values):
    """Uses recusion to return the 
    absolute value of a given list"""

    if values == []:
        return []
    else:
        rest_values = abs_list_rec(values[1:])
        if values [0] > 0:
            return [values[0]] + rest_values
        else:
            return [values[0]*-1] + rest_values


#Problem 2 Section 3
   
def num_vowels(words):
    """ returns the number of vowels in the string word
        input: word is a string of 0 or more lowercase letters
    """
    if words == '':
        return 0
    else:
        num_in_rest = num_vowels(words[1:])
        if words[0] in 'aeiou':
            return 1 + num_in_rest
        else:
            return 0 + num_in_rest
   
def most_vowels(words):
   """ Takes a list of strings and 
   returns the one with the most vowels"""
   
   vowels = [[num_vowels(s), s] for s in words]
   correct = max(vowels)
   return correct[1]
   

#Problem 2 Section 4

def num_multiples(m, values):
    """ Takes an interger and a value 
    and returns te values that are 
    multiples of the integer"""
    
    if values == []:
        return 0
    else:
        rest_values = num_multiples(m, values[1:])
        if values[0] % m == 0:
            return 1 + rest_values
        else:
            return rest_values
    

def mylen(s):
    """ returns the length of a list"""
    
    if s == '' or s == []:
        return 0
    else:
        len_rest = mylen(s[1:])
        return 1 + len_rest
    

#Problem 2 Section 5

def  begins_with(prefix, wordlist):
    """Returns a list of strings that 
    contain the prefix using list 
    comprehension"""
    
    lc = [x for x in wordlist if x[:len(prefix)] == prefix] 
    return lc 
    names = ['Alex', 'Adlai', 'Alison', 'Amalia', 'Anbita']
    
   
    
    
    
    
    
    
    