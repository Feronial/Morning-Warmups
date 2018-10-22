# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:31:33 2018

@author: sonerk
"""

def array_Check(arr1,arr2):
    
    result_list = list()
    
    for i in arr2:
        
       result_list.append(arr1.count(i))
            
    

    return result_list