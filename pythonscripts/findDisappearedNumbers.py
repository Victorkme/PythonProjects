# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:13:03 2019

@author: User1
"""
nums = [1,1]
def findDisappearedNumbers(nums):
    b = set(range(1,len(nums)+1))
    nums = set(nums)
    result = []
    for num in (b-nums):
        result.append(num)
    return(result)

print(findDisappearedNumbers(nums))