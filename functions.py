# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 20:55:09 2019

@author: Alan Maldonado
"""
        
def findEquationIndex(mat, eq):
    m = mat.shape[0]

    if eq == "x":
        for i in range(m):
            if (abs(mat[i][0]) > (abs(mat[i][1]) + abs(mat[i][2]))):
                return i                    
    elif eq == "y":
        for i in range(m):
            if (abs(mat[i][1]) > (abs(mat[i][2]) + abs(mat[i][0]))):
                return i 
    elif eq == "z":
        for i in range(m):
            if (abs(mat[i][2]) > (abs(mat[i][0]) + abs(mat[i][1]))):
                return i 
    