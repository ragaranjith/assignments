# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 11:48:14 2020

@author: ragar
"""
        
    
    
   # Write a program to check whether character is an alphabet or not using conditional operator.

#ASCIIvalues integer:[48,57], alphabet_lower[65,90], alphabet_upper[97,122]
i=input("enter a number(0 to 9) or an english aplhabet:")
v=ord(i)#finds out the ASCII value
if v in range(48,58):print("the value entered: %s"%i," is an integer")
elif v in range(65,91):print("the value entered: %s"%i," is an alphabet")
elif v in range(97,123):print("the value entered: %s"%i," is an alphabet")



#Python Program to check character is Alphabet or not

ch = input("Please Enter Your Own Character : ")

if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
    print("The Given Character ", ch, "is an Alphabet")
else:
    print("The Given Character ", ch, "is Not an Alphabet")