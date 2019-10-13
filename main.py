# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 20:51:58 2019
Finished on Sat Oct 12 11:00:51 2019
Version 1.0.0

@author: Alan Maldonado
"""

import numpy as np
import functions as fp

# Algorithm Variables (Don't modify)
max_iter = 100
tol = 1e-6

# Algorithm Functions

def algorithmStart(matA, matB, initPoint, Data, algo):
    print()
    print("======= ALGORITHM START =========")
    print()
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
    
    xk = initPoint[0]
    yk = initPoint[1]
    zk = initPoint[2]
    
    if(algo == 1): #JACOBI
        for ran in range(max_iter):
            sT1 = xk + yk + zk
            xA = fp.eqX(matA, matB, xi, yk, zk)
            yA = fp.eqY(matA, matB, yi, xk, zk)
            zA = fp.eqZ(matA, matB, zi, xk, yk)
            Data = np.concatenate((Data, np.array([[xA, yA, zA]])), axis=0)
            xk = xA
            yk = yA
            zk = zA
            sT2 = xk + yk + zk
            if abs(sT2 - sT1) <= tol:
                print("Algorithm found the solution in " + str(ran+1) + " iterations.")
                print()
                break
    else: #GAUSS-SEIDEL
        for ran in range(max_iter):
            sT1 = xk + yk + zk
            xk = fp.eqX(matA, matB, xi, yk, zk)
            yk = fp.eqY(matA, matB, yi, xk, zk)
            zk = fp.eqZ(matA, matB, zi, xk, yk)
            sT2 = xk + yk + zk
            Data = np.concatenate((Data, np.array([[xk, yk, zk]])), axis=0)
            if abs(sT2 - sT1) <= tol:
                print("Algorithm found the solution in " + str(ran+1) + " iterations.")
                print()
                break
            
    print(Data)
    print()
    print("======= ALGORITHM END =========")

### ALGORITHM STARTS HERE

matrix = np.array([[4,-1,1],[4,-8,1],[-2,1,5]])
resultMatrix = np.array([7,-21,15])
initPoint = (0,0,0)

Data = np.empty((0,3), float)
algorithmStart(matrix, resultMatrix, initPoint, Data, 2)
#Arguments = (NormalMatrix, ResultsMatrix, InitialPoint, DataStore(Don't change this), METHOD)
#Method Argument: 1 = JACOBI, 2 = GAUSS-SEIDEL