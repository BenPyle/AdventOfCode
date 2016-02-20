# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:54:42 2016

@author: l1bdp01
"""
import itertools

def travelLength(directions):
    distance = 0
    for cur, dest in zip(directions[0:-1], directions[1:]):
        distance+=int(direction_dictionary[cur+dest])
    return distance
    

inputs = open('./d9_input.txt').read().splitlines()
locations= []
direction_dictionary={} 
for ins in inputs:
    direction_dictionary[ins.split(" ")[0]+ins.split(" ")[2]]=ins.split(" ")[4]
    direction_dictionary[ins.split(" ")[2]+ins.split(" ")[0]]=ins.split(" ")[4]  
    locations.append(ins.split(" ")[0])
    locations.append(ins.split(" ")[2])

unique_locations=set(locations)

perms = itertools.permutations(unique_locations,len(unique_locations))
distances=[]
paths=[]
for perm in perms:
    paths.append(perm)
    distances.append(travelLength(perm))


print(max(distances)) #change to min for part 1

    