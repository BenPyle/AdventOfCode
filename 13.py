# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:52:28 2016

@author: l1bdp01
"""

#Using a simlar approach to traveling salesman

import itertools

def travelLength(directions):
    happys = 0
    for first, second in zip(directions[0:-1], directions[1:]):
        happys+=(direction_dictionary[first+second])
        happys+=(direction_dictionary[second+first])
    happys+=(direction_dictionary[directions[0]+directions[-1]])
    happys+=(direction_dictionary[directions[-1]+directions[0]])
    return happys
    

inputs = open('./d13_input.txt').read().splitlines()
people= []
direction_dictionary={} 

for ins in inputs:
    ins=ins.replace('.','')
    if ins.split(" ")[2]=="gain":
        happy_units=int(ins.split(" ")[3])
    else:
        happy_units=-1*int(ins.split(" ")[3])
    direction_dictionary[ins.split(" ")[0]+ins.split(" ")[10]]=happy_units
    people.append(ins.split(" ")[0])

unique_people=set(people)


##part 2 of question
for ppl in unique_people:
    direction_dictionary["me"+ppl]=0
    direction_dictionary[ppl+"me"]=0

unique_people=unique_people|{"me"}
##Part 2 end

perms = itertools.permutations(unique_people,len(unique_people))
happiness=[]
arrangements=[]
for perm in perms:
    arrangements.append(perm)
    happiness.append(travelLength(perm))


print(max(happiness)) #change to min for part 1