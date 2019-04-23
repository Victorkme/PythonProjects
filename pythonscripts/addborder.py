# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 12:59:39 2019

@author: User1


def addBorder(picture):
    l=len(picture[0])+2
    return ["*"*l]+[x.center(l,"*") for x in picture]+["*"*l]

def addBorder(picture):

    r = ['*'*(len(picture[0])+2)]
    for i in picture:
        r.append('*' + i + '*')
    r.append(r[0])
    return r



"""
picture = ['abc','def']
def addBorder(picture):
    rows = len(picture) + 2
    columns = len(picture[0]) + 2
    picture.insert(0,"")
    picture.append("")
    for row in range(rows):
        if row == 0 or row == rows-1:
            for column in range(columns):
                picture[row] += '*'
        else:
            picture[row] = '*' + picture[row] + '*'
    return picture
print(addBorder(picture))

