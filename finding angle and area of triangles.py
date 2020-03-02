# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:43:51 2020

@author: ragar
"""


#program to find the third angle of a triangle when other 2 angles are known
a=int(input("enter the first angle of a triangle:"))
b=int(input("enter the second angle of a triangle:"))
#sum of three angles in a triangle =180
c=(180-a-b)
print("the third angle of triangle=%i" %c)


#program to find the area of the triangle when base and height are given
b=int(input("enter the base of the triangle:"))
h=int(input("enter the height of the triangle:"))
area=((1/2)*b*h)
print("area of the triangle for given base and height=%i" %area)


#program to calculate area of an equilateral triangle
#length of one side of triangle
a=int(input("length of one side of equilateraltriangle:"))
area=((3/4)**(1/2)*(a**2))
print("area of equilateral triangle for a given side=%F" %area)