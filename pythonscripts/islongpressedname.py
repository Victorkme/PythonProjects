# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 16:17:15 2019

@author: User1
"""
name = 'leelee'
typed = 'lleeeleeleeleee'

def isLongPressedName(name, typed):
    index_i = 0
    index_j = 0
    while index_j < len(typed) and index_i < len(name):
        if typed[index_j] == name[index_i]:
            index_i += 1
            index_j += 1
        elif index_j > 0 and typed[index_j] == name[index_i]:
            index_j += 1
        else:
            index_j += 1
    return index_i == len(name)

print(isLongPressedName(name,typed))