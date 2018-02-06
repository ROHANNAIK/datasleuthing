# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 17:35:45 2017

@author: Rohan
"""
#%%
import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    ct = 0
    #for ct in range(0,10):
        #print(random.sample(range(30,35), 10))
    print([i+30 for i in [random.uniform(0,5) for ii in range (10)]])
#%%
