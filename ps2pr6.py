# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 14:49:10 2021

@author: Gianna
"""

# 
# ps2pr6.py - Problem Set 2, Problem 6
#
#  Fun with recursion, part 3
#

#Problem 6 Section 1

def letter_score(letter):
    """Takes a lower case letter and 
    returns the value of the letter in scrabble"""

    assert(len(letter) == 1)
    
    if letter in ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']:
        return 1
    if letter in ['d', 'g']:
        return 2
    if letter in ['b', 'c', 'm', 'p']:
        return 3
    if letter in ['f', 'h', 'v', 'w', 'y']:
        return 4
    if letter in ['k']:
        return 5
    if letter in ['j', 'x']:
        return 8
    if letter in ['q', 'z']:
        return 10
    else:
        return 0
    

#Problem 6 Section 2

def scrabble_score(word):
    """Takes a series of lowercase 
    letters and returns the scrabble 
    score of the word"""
    if word == '':
        return 0
    else:
        score = letter_score(word[0])
        scrabble = scrabble_score(word[1:])
        return score + scrabble


#Problem 6 Section 3

def compare(s1, s2):
    """Compares the two strings and return the number of characters they have different"""
    if s1 == s2:
        return 0
    else:
        compare_rest = compare(s1[1:], s2[1:])
        if s1[0] == s2[0]:
            return compare_rest
        else:
            return 1 + compare_rest


#Problem 6 Section 4

def weave(vals1, vals2):
    """ Use recurison to weave 
    the values of vals1 and vals2 
    alternating with each other"""
    

    if vals1 == vals2 == []:
        return []
    if vals1 == []:
        return vals2
    if vals2 == []:
        return vals1
    
    else:
        weave_rest = weave(vals1[1:], vals2[1:])
        return [vals1[0], vals2[0]] + weave_rest






