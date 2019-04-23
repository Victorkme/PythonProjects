# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 17:43:56 2019

@author: User1
"""
s = 'A man, a plan, a canal: Panama'
s = 'race a car'
s = 'abcdefg gg gfedcba'

def isPalindrome(s):
    if not s or s == 1:
        return True
    alpha = 'abcdefghijklmnopqrstuvwxyz1234567890'
    s = s.lower()
    i = 0
    j = len(s)-1
    while i <= j:
        while s[i] not in alpha:
#            print(s[i])
            i += 1
        while s[j] not in alpha:
            j -= 1
        if s[i] != s[j]:
#            print(s[i] + ' ' + s[j])
            return False
        if i == j:
            return True
        i += 1
        j -= 1
    return True

print(isPalindrome(s))