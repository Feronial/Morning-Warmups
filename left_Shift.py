# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 11:48:15 2018

@author: sonerk
"""


def left_Shift(arr, d):
    
    #Math based O(1) solution of left shift
    
    sub_a, sub_b = arr[0:d], arr[d:len(arr)]
    
    arr[len(arr) - d:len(arr)] = sub_a
    arr[0 : len(sub_b)] = sub_b
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    
    
    
    return arr