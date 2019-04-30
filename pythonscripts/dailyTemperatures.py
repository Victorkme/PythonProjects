# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 13:09:26 2019

@author: User1
"""

T = [73,74,75,71,69,72,76,73]


def dailyTemperatures(T):
    futureTemp = []
    order = []
    result = []
    maxTemp = 0
    for temp in reversed(T):
        maxTemp = max(maxTemp,temp)
        if not futureTemp:
            order.append(temp)
            futureTemp.append(temp)
            result.append(0)
        else:
            #print(temp)
            futureTemp.insert(0,temp)
            if temp == order[len(result)-1]:
                if result[len(result)-1] == 0:
                    result.append(0)
                    continue
                result.append(result[len(result)-1]+1)
                continue
            if temp in order:
                print(order)
                order.remove(temp)
                order.append(temp)
                print(order)
            else:
                order.append(temp)
            if temp < maxTemp:
                for ftemp in order[::-1]:
                    #print(order)
                    #print(futureTemp)
                    #print(str(temp) + "   temp")
                    #print(str(ftemp) + '   ftemp')
                    if ftemp > temp:
                        result.append(futureTemp.index(ftemp))
                        break
            else:
                result.append(0)
    return result[::-1]

print(dailyTemperatures(T))