# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 13:09:26 2019

@author: User1
"""

T = [73,74,75,71,68,72,76,73]

def dailyTemperatures(T):
    futureTemp = []
    result = []
    for temp in reversed(T):
        if not futureTemp:
            futureTemp.append(temp)
            result.insert(0,0)
        else:
            futureTemp.insert(0,temp)
            if temp < max(futureTemp):
                for ftemp in futureTemp:
                    if ftemp > temp:
                        result.insert(0,futureTemp.index(ftemp))
                        break
            else:
                result.insert(0,0)
    print(futureTemp)
    return result

print(dailyTemperatures(T))