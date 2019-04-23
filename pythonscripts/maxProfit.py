# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 20:19:08 2019

@author: User1
"""

def searchInsert(self, nums: List[int], target: int) -> int:
    result = 0
    if target not in nums:
        while True:
            for num in nums:
                if num < target:
                    result += 1
                else:
                    return result
            retu
    else:
        result = nums.index(target)
    return result