# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 11:14:58 2016

@author: l1bdp01
"""
import re
#pwd = 'vzbxkghb' #round 1
pwd = 'vzbxxyzz' #round 2


#122 is z, 97 is a 
ASCII_CONSTANT=96
NUM_LETTERS=27

def convertToNum(pwd):
    output=[]
    for char in pwd:
        number = ord(char)-ASCII_CONSTANT
        output.append(number)
    return output

def checkRules(pwd):
    pwd_num=convertToNum(pwd)
    rulesPassed=True
    firstRun=True
    while(rulesPassed==True & firstRun==True):
        firstCondition=0
        for first, second, third in zip(pwd_num[0:-2], pwd_num[1:-1], pwd_num[2:]):
            #rules n, n+1, n+2 must exist
            if first+2==second+1==third:
                firstCondition+=1
        if firstCondition==0:
            rulesPassed=False
        #two non overlapping aa, bb
        thirdCondition=[m.group() for m in re.finditer(r'((\w)\2)+', pwd)]
        if len(thirdCondition)<2:
            rulesPassed=False
        firstRun=False
        
    return rulesPassed
    
def nextPwd(pwd):
    pwd_num=convertToNum(pwd)
    carry=0
    new_pwd=[]
    pwd_num[-1]+=1
    for digit in pwd_num[::-1]:
        carry, new_num = divmod(digit+carry,NUM_LETTERS)
        if new_num ==0:
            new_num=1
        new_pwd= [chr(new_num+ASCII_CONSTANT)]+new_pwd
    out_pwd=''.join(new_pwd)
    return out_pwd
    
    
    
pwd = nextPwd(pwd) #round 2

while checkRules(pwd) == False:
    #Lazy and Hacky, come back and fix. 
    pwd = pwd.replace('i','j')
    pwd = pwd.replace('o','p')
    pwd = pwd.replace('l','m')
    pwd=nextPwd(pwd)

print(pwd)
    
    
        
    

