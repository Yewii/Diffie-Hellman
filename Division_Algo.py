# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 09:36:57 2017

@author: adamwarner
"""
import numpy as np 

def division_algo(n,d):
    store = []   
    while n  >=  1: 
        store.append(str(n % d))
        n = int(n/d)
    return ''.join(store)


def gcd(a,b):
    mod = a % b
    while a % b >= 1: 
        
        n = b * int(a/b) + a % b 
        a = b 
        b = mod
    return mod 
    
    
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
        

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m