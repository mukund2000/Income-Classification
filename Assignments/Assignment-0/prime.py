# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:53:19 2020

@author: Mukund Rastogi
"""

def isPrime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return True
    else:
        return False

m=int(input("Enter the starting of number"))
p=int(input("Enter the ending of number"))
for i in range(m,p+1):
    if(isPrime(i)):
        print(i,"is prime")
