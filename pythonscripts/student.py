# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 12:06:48 2018

@author: User1
"""

class Student:
    
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
    