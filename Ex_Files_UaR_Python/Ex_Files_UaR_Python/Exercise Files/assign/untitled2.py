# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:49:17 2018

@author: Rohan
"""
import csv

def shape(filename):
    op = open(filename)
    rd = csv.reader(op)
    print(rd)
    
def sq():
    num = [0,1,2,3,4]
    even_sq = [x ** 2 for x in num if x % 2 == 0]
    print(even_sq)
    
