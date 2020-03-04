# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 11:45:50 2020

@author: ragar
"""

#Write a program to swap two numbers using bitwise operator.


a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print("entered numbers are:",list((a,b)))
def XOR_swap(x,y):
    x=x^y
    y=x^y
    x=x^y
    return(x,y)
l=list(XOR_swap(a,b))
print("swapped numbers are:",l)