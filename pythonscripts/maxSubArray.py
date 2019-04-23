# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 18:51:20 2019

@author: User1
"""
nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
    for i in range(1,len(nums)):
        nums[i] = max(nums[i-1]+nums[i],nums[i])
        print(nums)
    return max(nums)

print(maxSubArray(nums))