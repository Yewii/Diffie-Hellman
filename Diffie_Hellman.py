# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 15:34:06 2017

@author: adamwarner
"""

## This program will be used to demonstrate basic Diffie-Hellman Key Exchange 

import numpy as np 
import pandas as pd 
import random 
from fractions import gcd
import math 

def soe(n):
    store = []
    prime = []
    z = n
    r = range(z+1)[2:len(range(z+1))]
    r = r[1::2]
    for i in range(len(r)):
        for j in range(len(r)):
             prime.append(r[i] % r[j])
    chunks = [prime[x:x+len(r)] for x in xrange(0, len(prime), len(r))]
    for i in range(len(chunks)):
       if chunks[i].count(0) == 1:
           store.append(r[i])
    store.insert(0,2)
    return store
        

#primes = soe(20000)

def first_primitive_root(p):
    primes = soe(int(round(math.sqrt(p))))
    tot = p-1
    divisor = []
    more = []
    for i in primes: 
        if tot % i == 0: 
            divisor.append(i)
    for i in divisor: 
        more.append(tot/i)
    prim_check = []
    for i in range(2,p):        
        prim_check = []
        for j in more:
            prim_check.append((i**j % p))
        if any(z == 1 for z in prim_check):
            continue
        else: 
            break
        
    return i
    
def all_roots(p):
    while True:
        try: 
            roots = [first_primitive_root(p)]
            a = first_primitive_root(p)
            for i in range(2,p):
                if gcd(i,p-1) == 1: 
                    roots.append(a ** i % p)
            return roots
        except ValueError: 
            return "Use a prime please" 


def invmodp(a, p):
    for d in xrange(1, p):
        r = (d * a) % p
        if r == 1:
            break
    else:
        raise ValueError('%d has no inverse mod %d' % (a, p))
    return d

any_in = lambda a, b: any(i in b for i in a)



def baby_step_giant_step(h,g,p):
    
    m = int(math.ceil(math.sqrt(p)))
    group = []
    for i in range(m+1):
        group.append(pow(g,i) % p)
    
    z = pow(invmodp(g,p),m) % p
    store = []
    more = 0
    k = 0
    q = m
    for i in range(0,q):
        if any_in(group,store) == True:        
            more += i-1
            break
        else:
            store.append(h*pow(z,i) % p)
            
    
    for j in range(len(group)):
        if group[j]== store[more]:
            k = k+j
            
    final_number = more*m+k
    return final_number
#    
#    return more,group,store,k,final_number,z
#    return m
##    return final_number #z,store,more,jj,final_number 
#    return more
#    
    
    
def DH(p,g,a,b):
#    p = 761 
#    g = 6

## Alice ## 
#    a = 12
    p = p
    A = pow(g,a) % p
## Bob ## 
#    b = 15 
    B = pow(g,b) % p 

## Alice 
    s_a = pow(B,a) % p 
## Bob 
    s_b = pow(A,b) % p 
    return {'secret':"The common secret is " + str(s_a), 'A':A,'p':p,'g':g}
#    print s_a 
#    print s_b
D_H = DH(761,6,7,15)
#print "Eve has got your secret " + str(baby_step_giant_step(A,g,p))