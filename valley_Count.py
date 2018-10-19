# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 14:26:33 2018

@author: sonerk
"""

def countingValleys(n, s):
    
    flag = 0
    is_Valley = 0
    valley_Count = 0
    
    for i in s:
        
        if i == 'U':
        
            is_Valley += 1 
            
            if is_Valley == 0:
            
                valley_Count += 1
        
        elif i == 'D' :
            
            is_Valley -= 1 
        
       
    
    return  valley_Count  


print (countingValleys(12,['D','D','U','U','D','D','U','D','U','U','U','D']))