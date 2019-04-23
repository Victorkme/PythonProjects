# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 21:44:19 2019

@author: User1
"""

statues = [6,2,3,8]

def makeArrayConsecutive2(statues):
    if len(statues) <= 1:
        return 0
    count = 0
    for index in range(min(statues)+1,max(statues)):
        print(index)
        if index not in statues:
            count += 1
    return count

print(makeArrayConsecutive2(statues))
