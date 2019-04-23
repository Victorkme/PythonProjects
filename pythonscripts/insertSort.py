# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 14:48:19 2019

@author: User1
"""

numArray = [99,2,10,15,22,25,4,3,3,7,8,2,5,12,21,9,3,1]

def insertSort(arraya):
    array = arraya
    length = len(array)
    index = 1 #start with index 1
    while index < length:
        check = index - 1
        change = -1
        while check >= 0:
            if array[index] < array[check]:
                change = check
                check -= 1
            else:
                check -= 1
        if change != -1:
            array.insert(change,array[index])
            del array[index+1]
        index += 1
    return array

print(insertSort(numArray))