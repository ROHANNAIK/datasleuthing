# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 20:11:43 2018

@author: Rohan
"""
#%%
def problem3_3(month, day, year):
    """ Takes date of form mm/dd/yyyy and writes it in form June 17, 2016 
        Example3_3: problem3_3(6, 17, 2016) gives June 17, 2016 """
    month_tuple = ("January", "February", "March", "April", "May", "June", "July","August","September","October","November","December")

    #month_name = month_tuple(month)
    #output = str(month_tuple[month-1] +str(day),year
    outputstr = month_tuple[month-1] +" "+str(day)+", "+str(year)
    print(outputstr.format(month_tuple[month-1],day,year))
    #print(output)
#%%
