# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:27:10 2018

@author: sonerk
"""



import numpy as np


def diagonal_Diff(Arr):
    
    right_Sum = 0
    
    left_Sum = 0
    
    left_Iter = 0
    for i in range(len(Arr)):
        
        
        right_Sum += Arr[i][i]
        
    for i in range(len(Arr)-1,-1,-1):
        
        left_Sum += Arr[left_Iter][i]
        
        left_Iter += 1
    
    result = abs(right_Sum - left_Sum)
    
    return result

a = np.random.randint(0,5, size = [3,3])
b = diagonal_Diff(a)


