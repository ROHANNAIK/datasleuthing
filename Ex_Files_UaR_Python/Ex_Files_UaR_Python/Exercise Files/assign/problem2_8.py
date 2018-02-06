# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 20:26:02 2017

@author: Rohan
"""

#%%
hourly_temp = [40.0, 39.0, 37.0, 34.0, 33.0, 34.0, 36.0, 37.0, 38.0, 39.0, \
               40.0, 41.0, 44.0, 45.0, 47.0, 48.0, 45.0, 42.0, 39.0, 37.0, \
               36.0, 35.0, 33.0, 32.0]
#%%
def problem2_8(temp_list):
    sum_of_temp = 0
    for i in range(len(temp_list)):
        sum_of_temp = sum_of_temp + temp_list[i]
    avg_of_temp = sum_of_temp/(len(temp_list))
    print("Average:",avg_of_temp)
    high = max(temp_list)
    print("High:",high)
    low = min(temp_list)
    print("Low:",low)
    
    

        
    
#%%