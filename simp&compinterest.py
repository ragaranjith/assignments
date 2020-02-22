# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 14:06:50 2020

@author: ragar
"""


#program to enter P,T,R and calculate simple intrest
P=float(input("enter the principle amount:"))
T=float(input("enter the number of years:"))
R=float(input("enter the rate of interest:"))
SI=(P*T*R/100)
print("simple interest=%2f" %SI)


#program to enter P,T,R and calculate compound intrest
P=float(input("enter the principle amount:"))
T=float(input("enter the number of years:"))
R=float(input("enter the rate of interest:"))
CI = P * (pow((1 + R / 100), T)) 
print("compound interest=%2f" %CI)