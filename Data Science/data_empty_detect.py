# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:08:36 2019

@author: sonerk
"""



def det_Start(df): # Data Frame empty value detection

    if not df.isna().values.any(): # Data Frame is full

        return -1

    else:

        df = df[df.isna().any(axis=1)]

        return df.index[0]