# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:34:01 2016

@author: Pyle
"""
#Part 1
import re
from random import shuffle
from datetime import datetime

inputs = open('./d19_input.txt').read().splitlines()
outputs=[]
matchWord=inputs[-1]
mydict=[]
for word in inputs[0:-2]:
    parsed=word.split(" ")
    out=[m.start() for m in re.finditer(parsed[0], matchWord)]
    for it in out:
        outputs.append(matchWord[:max(it,0)]+parsed[2]+matchWord[it+len(parsed[0]):])
print(len(set(outputs)))

for word in inputs[0:-2]:
    parsed=word.split(" ")
    mydict.append((parsed[0],parsed[2]))

target=matchWord
part2=0
minlength=999


#fairly dumb approach doesn't guarantee success, but it worked
while target!='e':
    tmp = target
    for a, b in mydict:
        if b not in target:
            continue
        target = target.replace(b, a, 1)
        part2 += 1
    if len(target)<minlength:
        minlength=len(target)
        print(len(target),str(datetime.now()))
    if tmp == target:
        target = matchWord
        part2 = 0
        shuffle(mydict)
        
print(part2)