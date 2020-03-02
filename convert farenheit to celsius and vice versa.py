# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:46:35 2020

@author: ragar
"""


#program to enter celcius and convert to farenheit temperature
#temp in celcius
tc=float(input("enter the celsius temperature:"))
#temp in farenheit
tf=(tc*(9/5)+32)
print("temperature in farenheit is=%2f" %tf)


#program to enter farenheit to celsius temperature
#temp in farenheit
tf=float(input("enter the farenheit temperature:"))
#temp in celcius
tc=((tf-32)*(5/9))
print("temperature in celsius=%2f" %tc)