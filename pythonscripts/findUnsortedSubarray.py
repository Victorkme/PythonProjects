# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 21:51:20 2019

@author: User1
"""
#nums = [1,3,2,2,2,4,4,5]
#nums = [2,6,4,8,10,9,15]
#nums = [1,2]
#nums = [2,1]
#nums = [4,3,2,1]
#nums = [1,2,3,3]
#nums = [2,3,3,2,4]

def findUnsortedSubarray(nums):
    start = -1
    check = 0
    result = 0
    for index in range(1,len(nums)):
        if start < 0 and nums[index-1] > nums[index]:
            start = index-1
            result = 2
            check = nums[index]
        elif start > -1 and check >= nums[index]:
            result = index - start + 1
        elif start > -1 and nums[index-1] > nums[index]:
            result = index - start + 1
    return max(start,result)

print(findUnsortedSubarray(nums))