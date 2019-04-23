# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 22:54:52 2019

@author: User1
"""

a = [1, 2, 3]
b = [1, 3, 2]


def areSimilar(A, B):
    print(sum(a!=b for a,b in zip(A,B)))
    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2
    
print(areSimilar(a,b))