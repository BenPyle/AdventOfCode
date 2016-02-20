# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 15:22:45 2016

@author: Pyle
"""

import numpy as np
import re


lightArray= np.zeros((1000, 1000))

inputs = open('./d6_input','r').read().splitlines()

#inputs = ["turn on 0,0 through 9,9"]

#part 1
#for word in inputs:
#    numsOnly=[int(s) for s in re.findall(r'\d+', word)]
#    if word[0:7]=="turn on":
#        lightArray[numsOnly[0]:numsOnly[2]+1,numsOnly[1]:numsOnly[3]+1]+=1
#    elif word[0:8]=="turn off":
#        lightArray[numsOnly[0]:numsOnly[2]+1,numsOnly[1]:numsOnly[3]+1]=0
#    else: 
#        lightArray[numsOnly[0]:numsOnly[2]+1,numsOnly[1]:numsOnly[3]+1]+=1
#        lightArray[numsOnly[0]:numsOnly[2]+1,numsOnly[1]:numsOnly[3]+1]=np.remainder(lightArray[numsOnly[0]:numsOnly[2]+1,numsOnly[1]:numsOnly[3]+1],2)
#
#print(np.sum(lightArray))

#part 2
for word in inputs:
    numsOnly=[int(s) for s in re.findall(r'\d+', word)]
    if word[0:7]=="turn on":
        lightArray[numsOnly[0]:numsOnly[2]+1,numsOnly[1]:numsOnly[3]+1]+=1
    elif word[0:8]=="turn off":
        lightArray[numsOnly[0]:numsOnly[2]+1,numsOnly[1]:numsOnly[3]+1]-=1
        lightArray = lightArray.clip(min=0)
    else: 
        lightArray[numsOnly[0]:numsOnly[2]+1,numsOnly[1]:numsOnly[3]+1]+=2
print(np.sum(lightArray))