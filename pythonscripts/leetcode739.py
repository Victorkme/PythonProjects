# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 09:48:34 2019

@author: User1
"""
T = [73,74,75,71,69,72,76,73]

def dailyTemperatures(T):
    nxt = [float('inf')] * 102 #create a range of infinity values to represent index of the temperature value seen
    ans = [0] * len(T) #create answer array
    for i in range(len(T) - 1, -1, -1):
        #Use 102 so min(nxt[t]) has a default value
        warmer_index = min(nxt[t] for t in range(T[i]+1, 102)) #find the lowest temperature from current temperature to 102
        if warmer_index < float('inf'): #if warmer_index is less than infinity the answer will be the stored index - the current index
            ans[i] = warmer_index - i
        nxt[T[i]] = i #store the index of the temperature in the nxt array
    return ans

print(dailyTemperatures(T))