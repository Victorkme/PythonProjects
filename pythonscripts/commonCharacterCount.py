# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:00:16 2019

@author: User1
"""

s1 = "aabcc"
s2 = "adcaa"

def commonCharacterCount(s1, s2):
    mydict = {}
    final = 0
    for letter in s1:
        mydict[letter] = mydict.get(letter,0) + 1
    for letter in s2:
        if letter in mydict:
            mydict[letter] = max(mydict[letter]-1,0)
    for letter in mydict:
        final += mydict[letter]
    return (len(s1)-final)

print(commonCharacterCount(s1,s2))
