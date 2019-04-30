# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 14:43:39 2019

@author: User1
"""

T = [73,74,75,71,68,72,76,73]

for index, temp in enumerate(reversed(T)):
    print(index)
    print(temp)
    
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()
for y in sorted(car.values()):
    print(y)
