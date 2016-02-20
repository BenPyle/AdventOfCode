# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:21:55 2016

@author: Pyle
"""
import numpy as np
#100 x 100 grid
GRIDSIZE=100
inputs = open('./d18_input.txt').read()
inputs=inputs.replace('\n','')
lights= np.zeros(shape=(GRIDSIZE+2,GRIDSIZE+2),dtype=object)
lights[:][:]='.'
lights_new=np.copy(lights)
#padding inputs with .'s around the edges
for iy in range(0,GRIDSIZE):
    for ix in range(0,GRIDSIZE):
        lights[iy+1][ix+1]=inputs[iy*GRIDSIZE+ix]
        #day 2 corners are on
        if ix%(GRIDSIZE-1)==0 and iy%(GRIDSIZE-1)==0:
            lights[iy+1][ix+1]='#'

def checkNeighboors(y,x):
    ons=0
    for iy in range(-1,2):
        for ix in range(-1,2):
            if abs(ix)+abs(iy)!=0:
                if lights[y+iy][x+ix]=='#':
                    ons+=1
    if (lights[y][x]=='.' and ons==3) or (lights[y][x]=='#' and ons>1 and ons<4):
        return '#'        
    #day 2 corners are stuck on
    if x%(GRIDSIZE-1)==1 and y%(GRIDSIZE-1)==1:
        return '#'
    else:
        return '.'

def animate():
    on=0
    for iy in range(1,GRIDSIZE+1):
        for ix in range(1,GRIDSIZE+1):
            lights_new[iy][ix]=checkNeighboors(iy,ix)
            if lights_new[iy][ix]=='#':
                on+=1
    lights=np.copy(lights_new)
    return lights, on

   
for it in range(0,100):
    lights, ons=animate()
print(ons)
    
