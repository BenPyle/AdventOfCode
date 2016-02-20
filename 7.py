# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:33:58 2016

@author: Pyle
"""
import re
lc = re.compile('[a-z]+')
inputs = open('./d7_input','r').read().splitlines()

#Part 1

my_dictionary={}
for word in inputs:
    leftwords = word.split(" -> ")
    outs=leftwords[1]
    ins=lc.findall(leftwords[0])
    ints= [int(s) for s in word.split() if s.isdigit()]
    if not ins:
        my_dictionary[outs]=ints[0]
    elif set(ins).issubset(my_dictionary.keys()): 
        if len(ins)==1:        
            ints=[my_dictionary[ins[0]]] + ints
        if len(ins)==2:
            ints=[my_dictionary[ins[0]]]+[my_dictionary[ins[1]]]+ints
        if leftwords[0].find('AND')>0:
            my_dictionary[outs]=(ints[0]&ints[1])
        elif leftwords[0].find('OR')>0:
             my_dictionary[outs]=(ints[0]|ints[1]) 
        elif leftwords[0].find('OT')>0:
            #Not is protected... dumb
             my_dictionary[outs]=(~ints[0])
        elif leftwords[0].find('LSHIFT')>0:
             my_dictionary[outs]=(ints[0]<<ints[1])
        elif leftwords[0].find('RSHIFT')>0:
             my_dictionary[outs]=(ints[0]>>ints[1])
        else:
            my_dictionary[outs]=ints[0]
    else:
        inputs.append(word)


        
aOut=my_dictionary['a']

#Part 2
inputs = open('./d7_input','r').read().splitlines()

my_dictionary={}
my_dictionary['b']=aOut
for word in inputs:
    leftwords = word.split(" -> ")
    outs=leftwords[1]
    if outs != 'b':
        ins=lc.findall(leftwords[0])
        ints= [int(s) for s in word.split() if s.isdigit()]
        if not ins:
            my_dictionary[outs]=ints[0]
        elif set(ins).issubset(my_dictionary.keys()): 
            if len(ins)==1:        
                ints=[my_dictionary[ins[0]]] + ints
            if len(ins)==2:
                ints=[my_dictionary[ins[0]]]+[my_dictionary[ins[1]]]+ints
            if leftwords[0].find('AND')>0:
                my_dictionary[outs]=(ints[0]&ints[1])
            elif leftwords[0].find('OR')>0:
                 my_dictionary[outs]=(ints[0]|ints[1]) 
            elif leftwords[0].find('OT')>0:
                #Not is protected... dumb
                 my_dictionary[outs]=(~ints[0])
            elif leftwords[0].find('LSHIFT')>0:
                 my_dictionary[outs]=(ints[0]<<ints[1])
            elif leftwords[0].find('RSHIFT')>0:
                 my_dictionary[outs]=(ints[0]>>ints[1])
            else:
                my_dictionary[outs]=ints[0]
        else:
            inputs.append(word)

print(my_dictionary['a'])

