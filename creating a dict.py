# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 14:16:58 2020

@author: ragar
"""
 # the below program is done using def and also normally using dict function  

def convert(tup,dictonary):
    dictonary = dict(tup)
    return dictonary
tup=((1,2),(2,3),(3,4))
dictonary={}
print(convert(tup,dictonary))



tup=((2,3),(3,4),(5,6))
dictonary=dict(tup)
print(dictonary)