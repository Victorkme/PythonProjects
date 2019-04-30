# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 23:08:28 2019

@author: User1
"""

def jumpingOnClouds(c):
    if len(c) == 2:
        return 1
    counter = 0
    index = len(c) - 1
    while index > 1:
        if c[index] == 0:
            index -= 2
            counter += 1
        else:
            index += 1
    if index == 1:
        counter += 1
    return counter
