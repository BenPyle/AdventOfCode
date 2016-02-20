# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:55:54 2016

@author: Pyle
"""
import math
from operator import mul
from functools import reduce

THENUM=34000000
presents=1
ij=1
#Naive way
def sumDivisors(n):
    divisors=0
    it=1
    while it<=int(math.floor(math.sqrt(n))):
        x, r = divmod(n,it)
        #less than 50 houses for part 2
        if r==0 and x<=50:
            divisors+=it
        if r==0 and it*it!=n and it<50:
                divisors+=(n/it)
        it+=1
    presents=divisors*11
    return presents


while presents<THENUM:
    presents=sumDivisors(ij)
    if THENUM/presents>10:
        ij=ij*2
    ij+=1
print(ij-1)
 

#lets get number theoretical
#Fast Part 1
#def factorization(n):
#
#    p = 1
#    while p * p < n:
#        p += 1
#        k = 0
#        while n % p == 0:
#            k += 1
#            n //= p
#        if k:
#            yield p, k
#    if n != 1:
#        yield n, 1
#        
#def sum_of_divisors(n):
#    return reduce(mul, ((p**(k+1)-1) // (p-1) for p, k in factorization(n)), 1)
#    
#while presents<THENUM:
#    presents=10*sum_of_divisors(ij)   
#    ij+=1
#
#print(ij-1)