# -*- coding: utf-8 -*-
"""
Created on Mon May 18 22:56:39 2020

@author: Mukund Rastogi
"""

def isArmstrong(n):
    temp=n
    s=0
    while(temp):
        rem=temp%10
        s=s+rem**3
        temp=temp//10
    if n==s:
        return True
    else:
        return False
x=int(input("Enter number"))
if(isArmstrong(x)):
    print(x,"is Armstrong number")
else:
    print("It is not Armstrong no.")
    