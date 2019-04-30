# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:42:46 2019

@author: User1
"""

# Create function that checks if two strings differ by one character
# Function inputs: 2 equal length strings
# Function outputs: Boolean (True if differ by one character, False otherwise)

inputArray1 = ['abb','abc','abb']
inputArray2 = ["abc","abx","axx","abx","abc"]
inputArray3 = ['q','q']
inputArray4 = ['abb','abc','abb','def','hik']
inputArray5 = ["abc","abx","axx","abx","abc"]
inputArray6 = ['abb','abb','abb','aba','aba','aba']

def charChecker(string1, string2):
    tracker = 0 # used to check the number of characters that differ
    for index, char in enumerate(list(string1)):
        if string2[index] != char:
            tracker += 1
            if tracker > 1: #used to end for loop early
                return False
    if tracker == 1: # these two strings differ by 1 character
        return True
    else: # last case is if the two strings are the same, which will mean it is false
        return False

# Create a function that takes an list of strings and picks through recursion
# Permutations that must differ by one character using the charChecker function
# If at the end of recursion, inputArray is empty check if length of chosen is equal
# to length of original input array. if it is return true, else return false
#
# Function Inputs: 1. List of Strings, 2.Chosen, 3. Original Length of list
# Function Outputs: Boolean (True if arrangement is found, false otherwise)

def permuteHelper(inputArray, chosen, length):
    if not inputArray and len(chosen) == length: # Returns true if InputArray is empty
        return True
    elif not inputArray and len(chosen) != length: # Don't think this does anything but dont want to break my code
        return False
    else:
        for index in range(len(inputArray)):
            if not chosen: #choose first element
                nextElem = inputArray[index]
            elif charChecker(chosen[len(chosen)-1],inputArray[index]): #use charChecker to choose next element that is 1 character different
                nextElem = inputArray[index]
            elif not charChecker(chosen[len(chosen)-1],inputArray[index]) and index == len(inputArray)-1: #if no words have 1 char difference return false
                return False
            else:
                continue
            #print(index)
            #print(nextElem)
            #print(chosen)
            #print(inputArray)
            inputArray.pop(index) # remove element from inputArray to pass through recursion
            chosen.append(nextElem)
            if permuteHelper(inputArray,chosen,length) == False: #if recursive function returns false, put back element and try next element
                inputArray.insert(0,nextElem)
                chosen.pop()
            elif permuteHelper(inputArray,chosen,length) == True: #if recursive function returns true, we are done and continue to return true through all called recursions
                return True
        return False # this means it checked all combinations and will return false

# Main function using helper functions to answer Code Signal #33

def stringsRearrangement(inputArray):
    length = len(inputArray)                   
    return permuteHelper(inputArray,[],length) # pass empty list as first choice

print(stringsRearrangement(inputArray1))
print(stringsRearrangement(inputArray2))
print(stringsRearrangement(inputArray3))
print(stringsRearrangement(inputArray4))
print(stringsRearrangement(inputArray5))
print(stringsRearrangement(inputArray6))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    