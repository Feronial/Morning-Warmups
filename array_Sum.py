# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 10:29:01 2018

@author: sonerk
"""

def ArraySum(ar):
    
    sum = 0
    
    for i in ar:
        
        sum += i
    
    return sum

print(ArraySum([1,2,3,4,5]))