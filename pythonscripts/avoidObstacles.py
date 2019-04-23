# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:44:55 2019

@author: User1
"""
inputArray = [5,3,6,7,9]

def avoidObstacles(inputArray):
    start = 0
    increment = 1
    while start <= max(inputArray):
        if start not in inputArray:
            start += increment
        else:
            increment += 1
            start = 0
    return increment

print(avoidObstacles(inputArray))