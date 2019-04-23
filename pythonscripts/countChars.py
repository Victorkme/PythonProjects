# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 21:37:48 2019

@author: User1
"""

#aaabbdcccccf` --> a3b2d1c5f1

inputString = 'aaabbdcccccf'
inputString2 = 'aaabbbaaabbbcccbbb'
inputString3 = 'jabviubagovuba'
inputString4 = 'ahkvkajhbva'

def countChars(inputString):
    inputString = list(inputString)
    result = [inputString.pop(),'1']
    for letter in reversed(inputString):
        if result[0] != letter:
            result.insert(0,letter)
            result.insert(1,'1')
        elif result[0] == letter:
            result[1] = str(int(result[1])+1)
    return "".join(result)

print(countChars(inputString))
print(countChars(inputString2))
print(countChars(inputString3))
print(countChars(inputString4))

''' Output 

a3b2d1c5f1
a3b3a3b3c3b3
j1a1b1v1i1u1b1a1g1o1v1u1b1a1
a1h1k1v1k1a1j1h1b1v1a1

'''