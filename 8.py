# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 08:42:53 2016

@author: l1bdp01
"""

#import sys

words = open('./d8_input.txt').read().splitlines()
total=0
new_total=0
for w in words:
    total+= len(w)-len(eval(w))
    new_total+=(2+w.count('\\')+w.count('"'))
print(total)
print(new_total)