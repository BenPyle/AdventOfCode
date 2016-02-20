# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:17:17 2016

@author: Pyle
"""
import itertools
import operator
import functools
###This is brute force slow
inputs = open('./d24_input.txt').read().splitlines()
presents=[]
for word in inputs:
    presents.append(int(word))
SUM_PRESENTS=sum(presents)/4
output=[]
minnum=10439961859*99999

for it in range(1,len(presents)):
    if output != []:
        break
    g1s=itertools.combinations(presents, it)
    for g1 in g1s:
        if sum(g1)==SUM_PRESENTS and functools.reduce(operator.mul, g1, 1)<minnum:
            smallerlist=set(presents)-set(g1)
            for ij in range(1,len(smallerlist)):
                g2s=itertools.combinations(smallerlist,ij)
                for g2 in g2s:
                    if sum(g2)==SUM_PRESENTS/3:
                        smallestlist=set(smallerlist)-set(g2)
                        for ik in range(1,len(smallestlist)):
                            g3s=itertools.combinations(smallerlist,ik)
                            for g3 in g3s:
                                if sum(g3)==SUM_PRESENTS:
                                    minnum=functools.reduce(operator.mul, g1, 1)
                                    output.append(minnum)
                                    break


print(min(output))


                            

