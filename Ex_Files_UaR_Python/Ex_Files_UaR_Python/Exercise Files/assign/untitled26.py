# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 17:56:47 2018

@author: Rohan
"""

import sys

filename = sys.argv[1]

text_file = open(filename)

word_dic = {}

for line in text_file:
    for word in line.lower().split():
        word = word.strip("',;.!?")
        if word not in word_dic:
            word_dic[word] = 0
        word_dic[word] = word_dic[word] + 1

text_file.close()

print("List of words on the file with numbers of appearances:")
word_list  = sorted(word_dic)
for word in word_list:
    print(word_dic[word], word)
    

for item in word_dic.items():
    print(item)