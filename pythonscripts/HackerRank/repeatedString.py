# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 22:44:49 2019

@author: User1
"""

s = 'bbbbba'
n = 1

def repeatedString(s, n):
    counter = 0
    remaining = 0
    for letter in s:
        if letter == 'a':
            counter += 1
    if counter == 0:
        return 0
    repeats = int(n/len(s))
    if n < len(s):
        remainder = n
    else:
        remainder = n % len(s)
    for char in s[:remainder]:
        if char == 'a':
            remaining += 1
    return counter*repeats+remaining

print(repeatedString(s,n))