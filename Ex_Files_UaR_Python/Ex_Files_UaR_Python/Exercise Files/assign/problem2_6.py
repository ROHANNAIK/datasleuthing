# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 17:43:39 2017

@author: Rohan
"""

#%%
import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(431)  # don't remove when you submit for grading
    ct = 0
    for ct in range (0,100):
        print(random.randint(1,6)+random.randint(1,6))

   
#%%