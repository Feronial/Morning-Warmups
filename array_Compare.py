# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 10:27:44 2018

@author: sonerk
"""

def compareArr(a, b):
    a_point = 0 
    b_point = 0
    count = 0
    
    for i in a :
        
        compare_Elem = i - b[count]
        
        if compare_Elem < 0:
            
            b_point += 1 
            count += 1
        
        elif compare_Elem == 0:
            count += 1
            continue
        
        else:
            a_point += 1
            count += 1
    
    return a_point, b_point

print (compareArr([1,2,3],[4,5,6]))