# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:38:25 2019

@author: User1
"""

inputString = 'racecar'

def checkPalindrome(inputString):
    start = 0
    end = -1
    for i in inputString:
        if inputString[start] == inputString[end]:
            print(inputString[start] + ' = ' + inputString[end])
            start += 1
            end -= 1
        else:
            return False
    return True

print(checkPalindrome(inputString))