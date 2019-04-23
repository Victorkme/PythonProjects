# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:51:51 2019

@author: User1
"""

a = [1, 2, 5, 8, 10, 22]


def absoluteValuesSumMinimization(a):
    result_array = []
    if len(a) <= 2:
        return a[0]
    for index, num in enumerate(a):
        result_array.append(0)
        for jndex in range(len(a)):
            result_array[index] += abs(a[jndex]-num)
    return (a[result_array.index(min(result_array))])

print(absoluteValuesSumMinimization(a))