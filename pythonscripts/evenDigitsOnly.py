# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 13:42:28 2019

@author: User1
"""
n = 22466
def evenDigitsOnly(n):
    for letter in str(n):
        if int(letter) % 2 != 0:
            return False
    return True
print(evenDigitsOnly(n))