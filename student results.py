# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:31:30 2020

@author: ragar
"""

x=int(input("enter the marks of the student:"))
if x>70:
    print("distinction")
elif 70>x>60:
    print("first class")
elif 60>x>50:
    print("second class")
elif 50>x>40:
    print("third class")
elif x<40:
        print("fail")
    
# for 70 60 50 40 marks there wont be any thing printed for the above program

    
x=int(input("enter the marks of the student:"))
if x>=70:
    print("distinction")
elif 70>x>=60:
    print("first class")
elif 60>x>=50:
    print("second class")
elif 50>x>=40:
    print("third class")
elif x<40:
        print("fail")