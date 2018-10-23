# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 08:59:01 2018

@author: sonerk
"""

def buble_Sort(arr):
        
    i = 0
    count = 0
    action = 0
    
    while True:
        
        if i != len(arr) - 1:
        
            if arr[i] > arr[i+1]:
            
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i + 1] = temp
                i += 1
                count = 0
                action += 1
                
            else:
                
                i += 1
                count +=1 
        
        elif count >= len(arr) - 1:
            
            break
        
        
        
        else:
            
            i = 0
            
    return action,arr



print(swapper(a))
        
    