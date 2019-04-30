# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:18:19 2019

@author: User1
"""

inputArray = [1,2,3,4,5,6,7,8,9,10]

def extractEachKth(inputArray, k):
    values = int(len(inputArray)/k)
    while values > 0:
        inputArray.pop(values*k-1)
        values -= 1
    return inputArray

print(extractEachKth(inputArray,3))