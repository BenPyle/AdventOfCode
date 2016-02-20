# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 08:35:44 2016

@author: Pyle
"""
#import numpy as np
import itertools
inputs = open('./d17_input.txt').read().splitlines()
sizes=[]
for words in inputs:
    sizes.append(int(words))

possibleCombos=0
possibleShortCombos=0
shortest=99
#part 1
for it in range(1,len(sizes)):
        for combo in itertools.combinations(sizes, it):
            if sum(combo)==150:
                shortest=min(len(sizes),it,shortest)
                possibleCombos+=1
print(possibleCombos)

#part two
for combo in itertools.combinations(sizes, shortest):
    if sum(combo)==150:
        possibleShortCombos+=1
print(possibleShortCombos)