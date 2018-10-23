# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 16:40:55 2018

@author: sonerk
"""

def reverse(arr):
    
    reversed_List = list()
    
    for i in range(len(arr)):
        
        reversed_List.append(arr.pop())
    
    
    return reversed_List