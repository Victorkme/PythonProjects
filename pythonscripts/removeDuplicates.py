# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 19:20:52 2019

@author: User1
"""
nums = [1,1,2]
index = [1,2]

def removeDuplicates(nums):
    result = 0
    index = []
    for num in nums:
        if num not in index:
            nums.insert(result,num)
            result += 1
            index.append(num)
    print(nums)
    return result

print(removeDuplicates(nums))