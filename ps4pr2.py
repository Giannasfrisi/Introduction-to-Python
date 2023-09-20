# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 22:55:36 2021

@author: Gianna
"""

#
# ps4pr2.py - Problem Set 4, Problem 2
#
# Using your conversion functions
#

from ps4pr1 import bin_to_dec
from ps4pr1 import dec_to_bin

# Problem 2 Section 1


def mul_bin(b1, b2):
    """Coverts to binary numbers to decimals,
    multiplies them and converts them
    back to binary"""
    n1 = bin_to_dec(b1)
    n2 = bin_to_dec(b2)

    product = n1 * n2
    b = dec_to_bin(product)
    return b


# Problem 2 Section 2
def largest_bin(binvals):
    """Takes a list of strings and returns
    the largest binary number"""

    length_words = [[len(x), x] for x in binvals] 
    max_pair = max(length_words)
    return max_pair[1]


    
