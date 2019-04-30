# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 22:53:05 2019

@author: User1
"""

def allLongestStrings(inputArray):
    maxLen = 0
    result = []
    for word in inputArray:
        maxLen = max(maxLen, len(word))
    for word in inputArray:
        if len(word) == maxLen:
            result.append(word)
    return result
