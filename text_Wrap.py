# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 01:25:01 2018

@author: Soner Can KALKAN
"""

def wrap_Text(text, width):
    
    
    for i in range(0,len(text),width):
        
        print(text[i:i+width])
    

    
    return 0

wrap_Text('SonerSerra',6)