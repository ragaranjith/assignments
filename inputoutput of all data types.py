# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:11:28 2020

@author: ragar
"""

#string- text type data type
s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

#integer - number type data type
x=5
print(x)
 #float
x=5.5
print(x)
 #complex
x=1+2j
print(x)
 
 #list sequence type data types
a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

 #tuple
t = (5,'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])


 #range
x = range(6)
print(x)
print(x[3])
y =range(3,20,2)
print(y)
print(y[1])


#mapping type-dictonary
d = {1:'value','key':2}
print(type(d))

print("d[1] = ", d[1]);

print("d['key'] = ", d['key']);


 #set type
x={"red","green","white"}
print(x)
print(type(x))

 #frozen set
x=frozenset({"red","green","white"})
print(x)
print(type(x))

  #boolean
x = True
print(x)
