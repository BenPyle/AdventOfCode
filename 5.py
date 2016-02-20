# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 14:12:17 2016

@author: Pyle
"""
import re
inputs = open('./d5_input','r').read().splitlines()

#inputs = ["xayyxa" "ttt"]
nice_words = 0
#vowels = "aeiouAEIOU"
#bad_combos= ["ab", "cd", "pq", "xy"]
#
#
#for word in inputs:
#    vowel_count = 0
#    double_letter = 0
#    bad_count = 0
#    
#    if re.findall(r'([a-z])\1', word.lower()):
#        double_letter= 1
#    for v in vowels:
#         vowel_count+=word.lower().count(v)
#    for b in bad_combos:
#        bad_count+=word.lower().count(b)
#    
#    if(double_letter == 1 and vowel_count>2 and bad_count == 0):
#        nice_words+=1
#        
#        
#print(nice_words)


#part two
for word in inputs:
    double_letter=0
    repeat_letter=0
#\b is a word boundry \w*? some number of letters (lazily) (w{2}) exactly two letters, match and capture
#\w*? same as above \1 the content of our two letter capture group \w*? same as above \b another word boundry
    if re.findall(r'\b\w*?(\w{2})\w*?\1\w*\b', word.lower()):
        double_letter= 1
    if re.findall(r'\b\w*?(\w{1})\w{1}\1\w*\b', word.lower()):
        repeat_letter= 1
    if(double_letter == 1 and repeat_letter ==1):
        nice_words+=1
print(nice_words)