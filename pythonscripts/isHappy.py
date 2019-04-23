# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:14:39 2019

@author: User1
"""

n = 19

def isHappy(n):
    mydict = {}
    num = n
    while num != 1:
        print(num)
        nums = str(num)
        print(nums)
        num = 0
        if nums not in mydict:
            mydict[nums] = mydict.get(nums,0)
        elif nums in mydict:
            return False
        for digit in nums:
            num += int(digit)**2
    return True

print(isHappy(19))