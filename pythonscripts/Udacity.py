# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 22:19:51 2018

@author: User1
"""


udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(uni_list):
    enroll = 1
    fees = 2
    tot_enrol = 1
    tot_fees = 1
    result = []
    for university in uni_list:
        tot_enrol = tot_enrol + university[1]
        tot_fees = university[2]
    avg_fees = tot_fees/len(uni_list)
    result_fees = avg_fees*tot_enrol
    result =[tot_enrol,result_fees]
    return result

print total_enrollment(udacious_univs)
#>>> (90000,0)

# The L is automatically added by Python to indicate a long
# number. If you are trying the question in an outside 
# interpreter you might not see it.

#print total_enrollment(usa_univs)
#>>> (77285,3058581079)




print measure_udacity(['Dave','Sebastian','Katy'])