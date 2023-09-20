# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 17:19:44 2021

@author: Gianna
"""

#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# Markov text generation    
#



def create_dictionary(filename):
    """Takes a string representing the name of a text 
    file and returns a dictionary of key-value pairs"""
    
    file = open(filename, 'r')
    text = file.read()
    file. close()
    
    words = text.split()
    d = {}
    current_word = '$'
    
    for next_word in words:
        if ('.' in next_word) or ('!' in next_word) or ('?' in next_word):
            if current_word not in d:
                d[current_word] = [next_word]
                current_word = '$'
            else:
               d[current_word] += [next_word]
               current_word = '$'
                
        else:
            if current_word not in d:
                d[current_word] = [next_word]
                current_word = next_word
            else:
               d[current_word] += [next_word]
               current_word = next_word
           
    return d

def generate_text(word_dict, num_words):
    """Takes the dictionary and generates a new word text"""
    import random
    start = '$'
    output = ''
    for x in range(num_words):
        wordlist = word_dict[start]
        next_word = random.choice(wordlist)
        if '!' in next_word or '.' in next_word or '?' in next_word:
            output += next_word 
            start = '$'
        else:
            output += next_word + ''
            start = next_word
        
        print(output)
    
    
            