# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:37:05 2018

@author: sonerk
"""

def min_Swaps(arr):
        
    array_Pos = [*enumerate(arr)] 

    array_Pos.sort(key = lambda it:it[1]) 

    visited = {k:False for k in range(n)} 
      

    ans = 0
    for i in range(len(arr) ): 
          

        if visited[i] or array_Pos[i][0] == i: 
            continue
              

        cycle_size = 0
        j = i 
        while not visited[j]: 
              

            visited[j] = True
     

            j = array_Pos[j][0] 
            cycle_size += 1
              

        if cycle_size > 0: 
            ans += (cycle_size - 1) 

            
    return ans 