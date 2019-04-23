# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 19:50:55 2019

@author: User1
"""

inputArray = [-53, -56, -24, -23,-21,3]

def adjacentElementsProduct(inputArray):
    for i in range(1,len(inputArray)):
        inputArray[i-1] = inputArray[i-1]*inputArray[i]
    inputArray[-1] = inputArray[-2]
    return(max(inputArray))

print(adjacentElementsProduct(inputArray))