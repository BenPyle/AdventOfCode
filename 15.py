# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 17:24:26 2016

@author: l1bdp01
"""
import re
import numpy as np

inputs = open('./d15_input.txt').read().splitlines()
ints= np.zeros([4,5])
it=0
yummy=0
for word in inputs:
    ints[it,:]=np.array([int(s) for s in re.findall("[-+]?\d+[\.]?\d*", word)])
    it+=1
def f(a,b,c,d): 
    out=int(np.prod((a*ints[0,0:-1]+b*ints[1,0:-1]+c*ints[2,0:-1]+d*ints[3,0:-1]).clip(0)))
    cals=int(a*ints[0,-1]+b*ints[1,-1]+c*ints[2,-1]+d*ints[3,-1]) 
    
    return out, cals

for a in range(0,100):
    for b in range(0,100-a):
        for c in range(0,100-a-b):
            d = 100 - a - b - c;
            yums, cals = f(a,b,c,d)
            #comment out second conditional for part 1
            if yums>yummy and cals==500:
                yummy=yums
print(yummy)

