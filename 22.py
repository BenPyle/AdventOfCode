# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 20:34:13 2016

@author: Pyle
"""
import random

boss_hp=55
boss_atk=8
turnnum=0
totalcost=0
#pois,shield,rechars
effects = [0, 0, 0]
costs=[]

spells=['mm','drain','poison','shield','recharge']
        
class aboss():
    def __init__(self,health,atk):
        self.hp=health
        self.atk=atk

    
class aplayer():
    def __init__(self):
            self.hp=50
            self.mana=500
            self.armor=0
            
def checkspell(spell):
    spellOK=2
    mana_check=player.mana
    if effects[2]>0:
        mana_check=player.mana+101
    if mana_check<53:
        return 0
    if spell=='drain':
        if mana_check<73:
            spellOK=1
    if spell=='poison':
        if mana_check<173 or effects[0]>1:
            spellOK=1
    if spell=='shield':
        if mana_check<113 or effects[1]>1:
            spellOK=1
    if spell=='recharge':
         if mana_check<229 or effects[2]>1:
            spellOK=1
    return spellOK

def turn(turn,spell):
    cost=0
    if effects[0]>0:
        effects[0]-=1
        boss.hp-=3
    if effects[1]>0:
        effects[1]-=1
        player.armor=7
    if effects[1]==0:
        player.armor=0
    if effects[2]>0:
        effects[2]-=1
        player.mana+=101
    if turn%2==0:
        if spell=='mm':
            cost=53
            boss.hp-=4
        if spell=='drain':
            cost=73
            boss.hp-=2
            player.hp+=2
        if spell=='poison':
            cost=173
            effects[0]=6
        if spell=='shield':
            cost=113
            effects[1]=6
        if spell=='recharge':
            cost=229
            effects[2]=5
    player.mana-=cost
    if turn%2==1:
        player.hp-=max(boss.atk-player.armor,1)
    #print(player.hp)
    return cost
        
#monte carlo it
for it in range(0,100):
    totalcost=0
    boss=aboss(boss_hp,boss_atk)
    player=aplayer()
    while boss.hp>0 and player.hp>0:
        if turnnum%2==0:
            if checkspell('mm')==0:
                break
            checked_spell=1
            while checked_spell==1:
                select_spell=random.choice(spells)
                checked_spell=checkspell(select_spell)
            totalcost+=turn(turnnum,select_spell)
            turnnum+=1
        if turnnum%2==1:
            turn(turnnum,'no')
            turnnum+=1
        if boss.hp<=0:
            costs.append(totalcost)
        
print(min(costs))


# turn player cast spell, and effect it
# then boss attack player and effect

        