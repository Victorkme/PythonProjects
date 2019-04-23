# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:39:03 2019

@author: User1
"""
nums = [1,0,1]
def singleNumber(nums):
    for num in nums:
        if nums.count(num) == 1:
            return num
    return False
print(singleNumber(nums))