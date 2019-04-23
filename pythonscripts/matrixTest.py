# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:01:39 2019

@author: User1
"""

image = [[1,1,1,1],[1,7,8,1],[1,1,1,1]]

def boxBlur(image):
    srow = 1
    scol = 1
    blur = 0
    result = []
    while srow < len(image)-1:
        result.append([])
        while scol < len(image[0])-1:
            blur = int(sum(image[srow-1][scol-1:scol+2] + image[srow][scol-1:scol+2]
                      +image[srow+1][scol-1:scol+2])/9)
            result[srow-1].append(blur)
            scol+=1
        srow+=1
    return result

print(boxBlur(image))