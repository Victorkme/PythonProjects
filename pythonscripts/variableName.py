# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 13:56:35 2019

@author: User1
"""
name = "var_1__Int"

def variableName(name):
    numeric = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz_'
    num_dict = {}
    alpha_dict = {}
    for number in numeric:
        num_dict[number] = num_dict.get(number,number)
    for letter in alpha:
        alpha_dict[letter] = alpha_dict.get(letter,letter)
    print(alpha_dict)
    if name[0] in num_dict:
        return False
    for char in name.lower():
        if (char not in num_dict) and (char not in alpha_dict):
            return False
    return True

print(variableName(name))