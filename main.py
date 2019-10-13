# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 20:51:58 2019

@author: Alan Maldonado
"""

import numpy as np
import functions as fp

matA = np.array([[4,-1,1],[4,-8,1],[-2,1,5]])
matB = np.array([7,-21,15])

# Basic Functions

def algorithmStart(matA, matB):
    m = matA.shape[0]
    n = matA.shape[1]
    
    if(m != n):
        print("-> Error: Matrix is not a Square Matrix")
        return
    
    if(m > 3 or n > 3):
        print("-> Error: Max matrix size is 3 rows and 3 columns.")
    
    xi = fp.findEquationIndex(matA, "x")
    yi = fp.findEquationIndex(matA, "y")
    zi = fp.findEquationIndex(matA, "z")
    print("Equation for X is in Row: " + str(xi))
    print("Equation for Y is in Row: " + str(yi))
    print("Equation for Z is in Row: " + str(zi))
    
algorithmStart(matA, matB)