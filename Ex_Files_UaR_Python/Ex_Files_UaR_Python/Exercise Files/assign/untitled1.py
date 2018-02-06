# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:28:53 2018

@author: Rohan
"""
#import sys

#filename = sys.argv[1]
#file2= sys.argv[1]
def problem3_6(filename, file2):
    text_file = open(filename)
    file2 = open(file2,'w',newline='')
   
    for line in text_file:
        for word in line.lower().split():
            word = word.strip("\n")
            count = 0
            count = count + 1
        file2.write(str(count))
    file2.close()
    text_file.close()

    
