# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 21:14:59 2019

@author: User1
"""
inputString = 'racecar'

def checkPalindrome(inputString):
    length = len(inputString)/2
    j = 1
    for i in range(int(len(inputString)/2)):
        if inputString[i] != inputString[-j]:
            return False
        j += 1
    return True

print(checkPalindrome(inputString))