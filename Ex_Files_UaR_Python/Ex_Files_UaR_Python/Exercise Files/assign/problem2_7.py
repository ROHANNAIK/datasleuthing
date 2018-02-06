# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 17:51:18 2017

@author: Rohan
"""

#%%

def problem2_7():
    
    """ computes area of triangle using Heron's formula. """
    a = input("Enter length of side one: ")
    a = float(int(a))
    b = input("Enter length of side two: ")
    b = float(int(b))
    c = input("Enter length of side three: ")
    c = float(int(c))
    s = (1/2)*(a+b+c)x
    #print(s)
    #s = float(int(s))
    area = (s*(s-a)*(s-b)*(s-c))**(1/2)
    #print(area)
    print("Area of a triangle with sides",a,b,c,"is",area)
    
#%%