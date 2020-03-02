# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:47:21 2020

@author: ragar
"""


#program to enter length in centimeter and convert to meter and kilometere
#length in cm
lcm=float(input("enter the length in cm:"))
#length in meter
lm=(lcm/100)
#length in kilometer
lkm=(lcm/100000)
print("length in meter=%2f" %lm)
print("length in kilometer=%2f" %lkm)