# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 15:37:04 2018

@author: sonerk
"""

import numpy as np


def flatten_List(arr):
    
    temp_arr = list()
    
    
    for i in arr:
        
        for k in i:
            
            temp_arr.append(k)
    
    return temp_arr

def duplicated(arr):
    
    temp_List = list()
    
    result_List = list()
    
    for i in arr:
        
        for k in i:
            
            if k not in temp_List:
            
                temp_List.append(k)
        
        #elif i  in temp_List and i  in result_List:
        
            #continue
        
            else:
            
                result_List.append(k)
     
            
    return result_List
        
            

def manifactureList(arr):
    
    static_List = list()
    
    for i in range(len(arr)**2 ):
    
        i += 1
        
        static_List.append(i)
    
    
    return static_List



def magicSquare(arr):
    
    
    
    result = 0
    
    static_List = manifactureList(arr)
    
    dynamic_List = list()
    
    duplicated_List = duplicated(arr)
    
    arr = flatten_List(arr)
    
    for i in static_List:
           
        if i not in arr:
            
            dynamic_List.append(i)
    
    for i in duplicated_List:
        
        temp_Diff_List = list()
        
        for k in dynamic_List:
            
            temp_Diff_List.append( abs(arr[arr.index(i)] - k))
        
        result += min(temp_Diff_List)
        
        arr[arr.index(i)] = dynamic_List.pop()
        
         
    
    return  result

a = np.random.randint(1,9,[3,3]).tolist()

#a = [[4,8,2],[4,5,7],[6,1,6]]

print(magicSquare(a)) 
