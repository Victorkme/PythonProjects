# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:16:16 2019

@author: User1
"""

inputString = "10.254.255.0"

def isIPv4Address(inputString):
    splitString = inputString.split('.')
    if len(splitString) != 4:
        return False
    for string in splitString:
        if string.isnumeric():
            if int(string) not in range(256):
                return False
        else:
            return False
    return True

print(isIPv4Address(inputString))