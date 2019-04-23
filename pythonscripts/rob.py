# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:39:14 2019

@author: User1
"""
nums = [1]
nums1 = [1,2,1,2]
nums2 = [2,1,1,2,5]
nums3 = [2,1,2,1,2]
nums = [2,1,1,2,2]
nums4 = [1,2,2,1,1]

def rob(nums):
    if len(nums) < 4:
        try:
            return max(nums[0]+nums[2],nums[1])
        except:
            return max(nums)
    index = 3
    nums[-index] = nums[-index]+nums[-1]
    while index < len(nums):
        index += 1
        nums[-index] = max((nums[-index]+nums[-index+2]),nums[-index]+nums[-index+3])
    return max(nums)

print(rob(nums))