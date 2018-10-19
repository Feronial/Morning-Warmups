# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 11:09:34 2018

@author: sonerk
"""


def plus_Notr_Minus(arr):
    
    
    count_Zero = 0
    
    count_Pos = 0

    count_Neg = 0

    
    for i in arr:
        
        if i == 0:
        
            count_Zero += 1
            
        elif i > 0:
            
            count_Pos += 1

        
        else:
        
            count_Neg += 1

    
    
    return count_Pos / len(arr), count_Neg / len(arr), count_Zero / len(arr)


print(plus_Notr_Minus([-4,3,-9,0,4,1]))