# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:04:02 2019

@author: User1
"""

yourLeft = 10
yourRight = 15
friendsLeft = 10
friendsRight = 15

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return (max(yourLeft,yourRight) == max(friendsLeft,friendsRight) and min(yourLeft,yourRight) == min(friendsLeft,friendsRight))

print(areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight))