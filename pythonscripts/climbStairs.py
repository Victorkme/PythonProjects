# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:43:07 2019

@author: User1
"""

n = 4
def climbStairs(n):
    nums = []
    index = 1
    while index <= n:
        nums.append(1)
        index += 1
    if n < 4:
        return n
    index = 3
    while index <= n:
        nums[-2] = 2
        print(nums)
        nums[-index] = nums[-index+1] + nums[-index+2]
        print(nums)
        index += 1
    return nums[0]
print(climbStairs(n))