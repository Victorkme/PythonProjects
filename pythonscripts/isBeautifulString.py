# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 09:10:47 2019

@author: User1
"""
inputString = 'bbbcc'

def isBeautifulString(inputString):
    my_dict = {}
    current,previous = -1,-1
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for letter in inputString:
        my_dict[letter] = my_dict.get(letter,0) + 1
    for char in alpha:
        if current < 0:
            current = my_dict.get(char,0)
        else:
            previous = current
            current = my_dict.get(char,0)
            if current > previous:
                return False
    return True

print(isBeautifulString(inputString))