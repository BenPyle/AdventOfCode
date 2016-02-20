# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:48:19 2016

@author: Pyle
"""
import itertools
boss_hp=109
boss_def=2
boss_atk=8

hero_hp=100

#cost damage armor
weaps=[(8,4,0),(10,5,0),(25,6,0),(40,7,0),(74,8,0)]
armors=[(13,0,1),(31,0,2),(53,0,3),(75,0,4),(102,0,5)]
rings=[(25,1,0),(50,2,0),(100,3,0),(20,0,1),(40,0,2),(80,0,3)]
costs=[]
lose_costs=[]

def fight(hero_atk,hero_def):
    player_wins=True
    hero_hp_local=hero_hp
    boss_hp_local=boss_hp
    while boss_hp_local>0 and hero_hp_local>0:
        boss_hp_local=boss_hp_local-max(hero_atk-boss_def,1)
        hero_hp_local=hero_hp_local-max(boss_atk-hero_def,1)
    if boss_hp_local>0:
        player_wins=False
    return player_wins



for ix in weaps:
    for iy in range(0,len(armors)+1):
        for iz in range(0,len(rings)+1):
            #INIT            
            cost=0
            hero_atk=0
            hero_def=0
            ###
            
            #weapons info
            hero_atk+=ix[1]
            cost+=ix[0]
            
            #iy loop        
            if iy<len(armors):
                hero_def+=armors[iy][2]
                cost+=armors[iy][0]
            #iz loops
            if iz<len(rings):
                hero_atk+=rings[iz][1]
                hero_def+=rings[iz][2]
                cost+=rings[iz][0]
            if iz==len(rings):
                cost+=0
            if fight(hero_atk,hero_def)==True:
                costs.append(cost)
            if fight(hero_atk,hero_def)==False:
                lose_costs.append(cost)
    

#sloppy way of dealing with the possibility of two rings    
for ix in weaps:
    for iy in range(0,len(armors)+1):
        for iza, izb in itertools.combinations(rings, 2):
            #INIT            
            cost=0
            hero_atk=0
            hero_def=0
            ###
            
            #weapons info
            hero_atk+=ix[1]
            cost+=ix[0]
            
            #iy loop        
            if iy<len(armors):
                hero_def+=armors[iy][2]
                cost+=armors[iy][0]
            #iz loops
            hero_atk+=iza[1]+izb[1]
            hero_def+=iza[2]+izb[2]
            cost+=iza[0]+izb[0]
            if fight(hero_atk,hero_def)==True:
                costs.append(cost)
            if fight(hero_atk,hero_def)==False:
                lose_costs.append(cost)
        

print(min(costs))
print(max(lose_costs))
    