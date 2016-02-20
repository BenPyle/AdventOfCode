# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 13:59:34 2016

@author: l1bdp01
"""

#Part1
import re
import json
ledger = open('./d12_input.txt').read()
string_numbers = re.findall("[-+]?\d+[\.]?\d*",ledger)
numbers=map(int,string_numbers)
print(sum(numbers))


### Part 2 Got help on this from reddit   
### Learn a bit more about how json works 
def n(j):
    if type(j) == int:
        return j
    if type(j) == list:
        return sum([n(j) for j in j])
    if type(j) != dict:
        return 0
    if 'red' in j.values():
        return 0
    return n(list(j.values()))

with open('./d12_input.txt') as data_file:
    data=json.load(data_file)
print(n(data))