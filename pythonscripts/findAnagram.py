# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:49:19 2019

@author: User1
"""

s = 'abcughsoabc'
p = 'abc'

def findAnagram(s, p):
    start = 0
    end = len(p)
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    adict = {}
    adict2 = {}
    for char in alpha:
        adict[char] = adict.get(char,0)
        adict2[char] = adict.get(char,0)
    for letter in p:
        adict[letter] = adict.get(letter) + 1
    for index in range(len(p)):
        adict2[s[index]] = adict2.get(s[index]) + 1
    if adict2 == adict:
        result.append(0)
    while end < len(s):
        adict2[s[end]] = adict2.get(s[end]) + 1
        adict2[s[start]] -= 1
        if adict2 == adict:
            result.append(start+1)
        start += 1
        end += 1
    return result

print(findAnagram(s,p))