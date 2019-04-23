# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 12:36:34 2019

@author: User1
"""
a = [4,2,9,11,2,16]
def sortByHeight(a):
    b = sorted(a, reverse = True)
    print(b)
    j = 0
    for index in range(1,len(a)+1):
        if a[-index] != -1:
            a[-index] = b[j]
            j += 1
    return a

print(sortByHeight(a))
