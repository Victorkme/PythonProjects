# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 11:50:24 2019

@author: User1
"""
#st = 'abcdc' 
#st = 'race'
#st = 'abbbbaaaabbbb'

def buildPalindrome(st):
    index = 0
    check = st[index:]
    left = check[:round(len(check)/2+0.2)]
    right = check[int(len(check)/2):]
    while left != right[::-1]:
        check = st[index:]
        left = check[:round(len(check)/2+0.2)]
        print(left)
        right = check[int(len(check)/2):]
        print(right)
        index += 1
    result = st[:index-1]
    return (st+result[::-1])

print(buildPalindrome(st))