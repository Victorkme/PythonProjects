# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 11:44:29 2019

@author: User1
"""
address = 'mevictor123@gmail.com'

def findEmailDomain(address):
    address = address[::-1]
    index = address.index('@')
    result = address[:index]
    return result[::-1]

print(findEmailDomain(address))