# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 13:13:52 2018

@author: misti
"""

import numpy as np


def jumping_Puzzle(Arr):
    
    jump = 0
    count = 0
    
    for i in Arr:
        
        if jump == len(Arr) - 1:
            
            break
        
        if Arr[jump + 2] == 0:
            
            jump += 2
            
            count += 1
            
            continue
        
        elif Arr[jump + 1] == 0:
            
            jump += 1 
            
            count += 1 
                
            continue
    
        else:
            
            print ("Error : NO MOVE")
            return 0
            
    
    
    return count


print (jumping_Puzzle([0,0,1,0,0,1,0,0,0,1,0]))        