# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:32:48 2019

@author: User1
"""

inputArray = ["abc","zzz","axx","abx","abc"]
result = []
def permutation(listArray):
    # If list is empty then there are no permutations
    if len(listArray) == 0:
        return []
    #if there is only one element in list then, only one permutation is possible
    if len(listArray) == 1:
        return [listArray]
    #Find the permutations for the list if there are more than 1 characters
    l = []
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(listArray)): 
        m = listArray[i] 
      # Extract lst[i] or m from the list.  remLst is 
      # remaining list 
        remLst = listArray[:i] + listArray[i+1:] 
       # Generating all permutations where m is first 
       # element 
        for p in permutation(remLst): 
            l.append([m] + p) 
    return l 
            
def stringsRearrangement(inputArray):
    word_length = len(inputArray[0])
    inputArray = permutation(inputArray)
    #print(inputArray)
    result = []
    tracker = 1
    for permute in range(len(inputArray)):
        result.append([])
        for index in range(1,len(inputArray[0])):
            flag = True
            tracker = 0
            for char in range(word_length):       
                if inputArray[permute][index][char] != inputArray[permute][index-1][char]:
                    tracker += 1
                    if tracker > 1:
                        flag = False
                        result[permute].append(flag)
                        break
            if tracker == 0:
                flag = False
                result[permute].append(flag)
            elif tracker == 1:
                flag == True
                result[permute].append(flag)
    for each in result:
        if all(each) == True:
            return True
    return False

#print(stringsRearrangement(inputArray,""))
print(stringsRearrangement(inputArray))