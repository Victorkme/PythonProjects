# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:58:08 2019

@author: User1
"""
s = 'cbaebabacd'
p = 'abc'

def findAnagrams(s, p):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    start = 0
    index = len(p)
    result = []
    adict = {}
    for letter in alpha:
        adict[letter] = 0
    for letter in p:
        if not adict[letter]:
            adict[letter] = 0
        adict[letter] += 1
    def checkAnagram(adict,s_slice):
        result = 0
        adict2 = adict.copy()
        for letter in s_slice:
            adict2[letter] -= 1
        for letter in p:
            result = result + abs(adict2[letter])
        if result == 0:
            return True
    while index <= len(s):
        s_slice = s[start:index]
        if checkAnagram(adict,s_slice):
            result.append(start)
        start += 1
        index += 1
    return result

print(findAnagrams(s,p))