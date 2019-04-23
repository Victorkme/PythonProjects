# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:19:59 2019

@author: User1
"""
cell1 = 'A1'
cell2 = 'B3'

def chessBoardCellColor(cell1, cell2):
    my_dict = { 'a':1,
                'b':2,
                'c':3,
                'd':4,
                'e':5,
                'f':6,
                'g':7,
                'h':8   }
    if ((my_dict[cell1[0].lower()]+int(cell1[1]))%2) == ((my_dict[cell2[0].lower()]+int(cell2[1]))%2):
        return True
    else:
        return False

print(chessBoardCellColor(cell1,cell2))