# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:27:07 2019

@author: User1
"""

def allLongestStrings(inputArray):
    string_list = [inputArray[0]]
    if len(inputArray) < 2:
       return string_list
    for i in range(1, len(inputArray)):
        if len(inputArray[i]) > len(string_list[0]):
            string_list.clear()
            string_list.append(inputArray[i])
        elif len(inputArray[i]) == len(string_list[0]):
            string_list.append(inputArray[i])
    return string_list