# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 17:47:44 2016

@author: l1bdp01
"""

start = '3113322113 '

def looksay(inStr):
    outStr=""
    counter = 1
    test = inStr[0]
    for i in range(0,len(inStr)-1):
        if (test==inStr[i+1]):
            counter+=1
        else:
            # using += is waaaay faster than declaring anew string
            outStr+=str(counter)+inStr[i]
            counter=1
            test=inStr[i+1]
            
    return outStr
            
        

for i in range(0,50):
    start=looksay(start)+" "
    print(i)

print(len(start)-1)