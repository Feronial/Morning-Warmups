# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 20:00:44 2018

@author: misti
"""

import numpy as np



def hour_Glass(Arr):
    
    max_List = list()
    
    for x in range(Arr.shape[0] - 2): # 1 row from top 1 row from bottom
        
        x += 1 # Starting from second row
    
        for y in range(Arr.shape[1] - 2):
            
            y += 1
            
            b = Arr[x - 1 , y - 1]
            
            result = (Arr[x - 1, y - 1] + Arr[x - 1, y] + Arr[x - 1, y + 1 ] + 
                      Arr[x,y]+ Arr[x + 1, y - 1] + Arr[x + 1, y] + 
                      Arr[x + 1, y +  1])
                
            max_List.append(result)
    
    
    max_List.sort()
    
    return max_List.pop()
    
    
    
k = np.random.randint(0,5,[6,6])
    
print(hour_Glass(k))