# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 17:18:17 2018

@author: Rohan
"""

import sys

infilename = sys.argv[1]
outfilename = sys.argv[2]

infile = open(infilename)
outfile = open(outfilename, 'w')

for line in infile:
    outfile.write(line)
    
infile.close()
outfile.close()