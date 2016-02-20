# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 11:40:29 2016

@author: Pyle
"""
import re


class Sue:
    def __init__(self, dictionary):
        
        for k, v in masterSueDict.items():
            setattr(self, k, None)
        for k, v in dictionary.items(): 
            setattr(self, k, v)

        theSue=True
        for k, v in masterSueDict.items():
            if getattr(self, k)!=None:
                if k=='cats' or k=='trees':
                    if getattr(self, k)<=v:
                        theSue=False
                elif k=='pomeranians' or k=='goldfish':
                    if getattr(self, k)>=v:
                       theSue=False
                elif getattr(self, k)!=v:
                        theSue=False
        self.isTheSue=theSue 
            
masterSueDict={'children':3,'cats': 7, 'samoyeds': 2, 'pomeranians' : 3, 'akitas': 0, 'vizslas':0,  'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes':1}



masterSue=Sue(masterSueDict)
ij=1
        
inputs = open('./d16_input.txt').read().splitlines()
for words in inputs:
    words=words.replace(',','')
    parsed=words.split(" ")
    temp_dictionary={}
    for it in range(2,8,2):
        temp_dictionary[parsed[it][0:-1]]=int(re.search(r'\d+', parsed[it+1]).group())
    newSue=Sue(temp_dictionary)
    if newSue.isTheSue==True:
        print(temp_dictionary)
        theSue=ij
    ij+=1
print(theSue)



    