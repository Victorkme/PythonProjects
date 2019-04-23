# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 13:02:18 2019

@author: User1
"""
inputString = 'foo(bar)baz'  # = foorabbaz
inputString = "foo(bar)baz(blim)"

def reverseInParentheses(inputString):
    def reverse_slicing(s):
        s = s[::-1]
        return s
    end = inputString.find(')')
    start = inputString.rfind('(',0,end)
    while end != -1:
        inputString = inputString[:start] + reverse_slicing(inputString[start+1:end]) + inputString[end+1:]
        end = inputString.find(')')
        start = inputString.rfind('(',0,end)
    return(inputString)
    
print(reverseInParentheses(inputString))