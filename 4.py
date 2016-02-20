# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import hashlib

hashedSolved = False
it = 1


while (hashedSolved == False):
    test = "ckczppom"+str(it)
    hashed= hashlib.md5(test.encode('UTF-8')).hexdigest() 
    if hashed[0:6]=="000000":
        hashedSolved=True
        print(it)
    it+=1
