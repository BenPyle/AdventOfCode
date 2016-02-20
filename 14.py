# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:24:46 2016

@author: l1bdp01
"""
import numpy as np
inputs = open('./d14_input.txt').read().splitlines()

reindeer=[]
TIME=2503

for ins in inputs:
    #Tuple is name, speeds, travel_times, rest_times
    reindeer.append((ins.split(" ")[0],float(ins.split(" ")[3]),float(ins.split(" ")[6]),float(ins.split(" ")[13])))
    
print(reindeer)
def traveling(reindeer, TIME):
    total_cycles, left_over= divmod(TIME,reindeer[2]+reindeer[3])
    if left_over>reindeer[2]:
        travel_cycles=total_cycles+1
    else:
        travel_cycles=total_cycles+left_over/reindeer[2]
    distance=int(travel_cycles*reindeer[1]*reindeer[2])
    return distance

traveled=[]
for i in range(0,len(reindeer)):
    traveled.append(traveling(reindeer[i],TIME))
    
print(int(max(traveled)))


#Part2
points=[0] * len(reindeer)
for j in range(1,TIME):
    traveled2=[]
    for i in range(0,len(reindeer)):
        traveled2.append(traveling(reindeer[i],j))
    winners = np.argwhere(traveled2 == np.amax(traveled2)).flatten().tolist()
    for win in winners:
        points[win]+=1   


print(max(points))