# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 08:32:37 2018

@author: sonerk
"""
#Complete the sockMerchant function below.
#stepping with two if sequential elements are the same.
def sockMerchant(n, ar):
     
    res = 0
        
    ar.sort()
    
    loop_Ar = iter(range(n))
    #for i in range(n):
        
    for i in loop_Ar:
        
        
        if i == n-1:
            
            break
        
        if ar[i] == ar[i + 1] :
            
            res += 1
            next(loop_Ar)
        
        
        
    return res   


print(sockMerchant(9,[1,1,1,2,2,2,2,3,3]))