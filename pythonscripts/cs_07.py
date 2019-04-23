# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 22:26:26 2019

@author: User1
"""
sequence = [1,2,1,2]
sequence1 = [1,2,5,3,5]
sequence2 = [10,1,2,3,4,5]
sequence3 = [1, 2, 3, 4, 5, 3, 5, 6]

def almostIncreasingSequence(sequence):
    count = 0
    for num in range(1,len(sequence)):
        if sequence[num] <= sequence[num-1]:
            count += 1
            if num == 1:
                sequence[num-1] = sequence[num]
            else:
                if sequence[num] <= sequence[num-2]:
                    sequence[num] = sequence[num-1]
        if count > 1:
            return False
    return True

print(almostIncreasingSequence(sequence))
