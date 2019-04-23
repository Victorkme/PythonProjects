# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 08:24:27 2019

@author: User1
"""
matrix = [[]]

def matrixElementsSum(matrix):
    result = 0
    for row in range(len(matrix)):
        if result == 0:
            result = sum(matrix[row])
        else:
            for column in range(len(matrix[row])):
                if matrix[row-1][column] == 0:
                    matrix[row][column] = 0
                else:
                    result = result + matrix[row][column]
    return result

print(matrixElementsSum(matrix))