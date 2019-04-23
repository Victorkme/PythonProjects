# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 11:22:12 2019

@author: User1
"""

matrix = [[True,False,False],[False,True,False],[False,False,False]]

def minesweeper(matrix):
    if not matrix:
        return [[0]]
    rows = len(matrix)
    columns = len(matrix[0])
    result = [[0 for col in range(columns)] for mrow in range(rows)]
    for row in range(rows):
        for column in reversed(range(columns)):       
            value = matrix[row][column]
            #print(result)
            #print("column: " + str(column) + " value: " + str(value))
            if row == 0:
                if column == len(matrix[row])-1:
                    if value:
                        result[row][column-1] += 1
                        result[row+1][column-1] += 1
                        result[row+1][column] += 1
                elif column == 0:
                    if value:
                        result[row][column+1] += 1
                        #print(result)
                        result[row+1][column+1] += 1
                        #print(result)
                        result[row+1][column] += 1
                        #print(result)
                else:
                    if value:
                        result[row][column-1] += 1
                        result[row][column+1] += 1
                        result[row+1][column-1] += 1
                        result[row+1][column+1] += 1
                        result[row+1][column] += 1
            elif row == rows-1:
                if column == len(matrix[row])-1:
                    if value:
                        result[row][column-1] += 1
                        result[row-1][column-1] += 1
                        result[row-1][column] += 1
                elif column == 0:
                    if value:
                        result[row][column+1] += 1
                        result[row-1][column+1] += 1
                        result[row-1][column] += 1
                else:
                    if value:
                        result[row][column-1] += 1
                        result[row][column+1] += 1
                        result[row-1][column-1] += 1
                        result[row-1][column+1] += 1
                        result[row-1][column] += 1
            else:
                if column == len(matrix[row])-1:
                    if value:
                        result[row][column-1] += 1
                        result[row-1][column-1] += 1
                        result[row-1][column] += 1
                        result[row+1][column-1] += 1
                        result[row+1][column] += 1
                elif column == 0:
                    if value:
                        result[row][column+1] += 1
                        result[row-1][column+1] += 1
                        result[row-1][column] += 1
                        result[row+1][column+1] += 1
                        result[row+1][column] += 1
                else:
                    if value:
                        result[row][column-1] += 1
                        result[row][column+1] += 1
                        result[row-1][column-1] += 1
                        result[row-1][column+1] += 1
                        result[row-1][column] += 1
                        result[row+1][column-1] += 1
                        result[row+1][column+1] += 1
                        result[row+1][column] += 1
    return result

print(minesweeper(matrix))