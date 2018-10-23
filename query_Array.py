# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:50:35 2018

@author: sonerk
"""
import numpy as np 


# Array Manipulation

def query_Adder(n , query):
    
    
    for i in query:
        
        sub_List = n[i[0] - 1 : i[1]]
        
        sub_List = list(map(lambda x: x + i[2], sub_List))
        
        n[i[0] - 1 : i[1] - 1] = sub_List

    return max(n)


def arrayManipulation(n, queries):
        
    list=[0]*(n+1)
    for _ in range(len(queries)) :
        a, b, k = map(int, (input().split()))
        list[a-1]=list[a-1]+k
        list[b] = list[b] - k;

    for i in range(1,n):
        list[i]+=list[i-1]

        return max(list)
    
    

    
print(arrayManipulation(10000000, a))
