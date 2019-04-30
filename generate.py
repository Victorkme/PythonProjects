# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 12:29:26 2019

@author: User1
"""

numRows = 5


def generate(numRows):
    if numRows == 0:
        return [[]]
    elif numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1],[1,1]]
    else:
        result = [[1],[1,1]]
        for row in range(2,numRows):
            result.append([1])
            for index in range(1,row):
                result[row].append(result[row-1][index-1]+result[row-1][index])
            result[row].append(1)
        return result
        
print(generate(numRows))