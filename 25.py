# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:41:45 2016

@author: l1bdp01
"""

FINALROW=2981
FINALCOL=3075
MODNUM=33554393
MULTNUM=252533
row=1
col=1
it=0

go=True 
while go: 
   it_col=0
   for it_row in range(row,0,-1):
        it_col+=1
        if it_row==FINALROW and it_col==FINALCOL:
            location=it
            go=False
            break
        it+=1
   row+=1

out=20151125
for ij in range(0,location):
    out=(out*MULTNUM)%MODNUM
print(out)

       