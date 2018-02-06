# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 18:22:04 2018

@author: Rohan
"""

# -problem3_6.py *- coding: utf-8 -*-

import sys

# add your code here

#%%
def problem3_1(txtfilename):
    
    filename = open(txtfilename)
    
    #word_dic = {}
    ct = 0
    
    for line in filename:
        print(line,end="")
        for word in line:
            ct = ct + 1
            
    print("\n")
    print("There are",ct,"letters in the file.")
    
    filename.close()

#%%