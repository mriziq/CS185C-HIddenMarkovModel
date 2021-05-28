import random as r 
from random import randint
import numpy as np


class Structures:     # This class generates stochatic initial, transition, and observation matrices used in model.py
    # columnxrows
    N = 2
    M = 3
    A = [[0] * N] * N
    B = [[0] * M] * N
    pi = [[0] * N]

    # Scales for randomizing stochastic matricies.
    scale1 = 1.0 / N
    scale2 = 1.0 / M
    
    # Scales for 1/N for A structure
    min1 = scale1 - 0.01
    max1 = scale1 + 0.01

    # Scales for 1/M for B structure
    min2 = scale2 - 0.01
    max2 = scale2 + 0.01

    #Random seed uniform distirbution range
    begin = 0.0
    end = 1.0

    piRowSum = 0
    aRowSums = []
    bRowSums = []
    rowSum = 0
    
    # Generate A NxN matrix of random numbers not yet stochastic
    for i in range(0, len(A)):
        for j in range(len(A[i])):
            randomValue = min1 + (max1 - min1) * np.random.normal()
            A[i][j] = randomValue
            rowSum += A[i][j]
        aRowSums.append(rowSum)
        rowSum = 0

    # Generate B NxM matrix of random numbers not yet stochastic
    for i in range(0, len(B)):
        for j in range(len(B[i])):
            randomValue = min2 + (max2 - min2) * np.random.normal()
            B[i][j] = randomValue
            rowSum += B[i][j]
        bRowSums.append(rowSum)
        rowSum = 0


    # Generate Pi 1xN matrix of random numbers not yet stochastic
    for i in range(0, len(pi)):
        randomValue = min1 + (max1 - min1) * np.random.normal()
        pi.append(randomValue)
        pi[i] = randomValue

    for i in range(len(pi)):
        piRowSum += pi[i]


    misCalc = 0 #How off the sum of a row is from 1
    reCalc = 0  #How much needs to be distributed or subtracted from each element

    # Pi adjustment for stochasticity 
    if piRowSum > 1:
        misCalc = piRowSum - 1
        reCalc = misCalc / len(pi)

        for i in range(0, len(pi)):
            pi[i] -= reCalc

    else:
        misCalc = 1 - piRowSum
        reCalc = misCalc / len(pi)

        for i in range(0, len(pi)):
            pi[i] += reCalc

   # Reseting values
    misCalc = 0 #How off the sum of a row is from 1
    reCalc = 0  #How much needs to be distributed or subtracted from each element

    # A adjustment for stochasticity 
    for i in range(0, len(A)):
        if aRowSums[i] > 1:
            misCalc = aRowSums[i] - 1
            reCalc = misCalc / len(A[i])

            for j in range(0, len(A[i])):
                A[i][j] -= reCalc
        
        else:
            misCalc = 1 - aRowSums[i]
            reCalc = misCalc / (len(A[i]))
            
            for j in range(0, len(A[i])):
                A[i][j] += reCalc
    # Reseting values
    misCalc = 0 #How off the sum of a row is from 1
    reCalc = 0  #How much needs to be distributed or subtracted from each element
    
    # B adjustment for stochasticity 
    for i in range(0, len(B)):
        if bRowSums[i] > 1:
            misCalc = bRowSums[i] - 1
            reCalc = misCalc / len(B[i])

            for j in range(0, len(B[i])):
                B[i][j] -= reCalc
        
        else:
            misCalc = 1 - bRowSums[i]
            reCalc = misCalc / (len(B[i]))
            
            for j in range(0, len(B[i])):
                B[i][j] += reCalc
   
    # Reseting values
    misCalc = 0 #How off the sum of a row is from 1
    reCalc = 0  #How much needs to be distributed or subtracted from each element


################################### DEBUGGER ###################################
## Output raw generated random values to compare with stochastic checker
# print("--- RAW RANDOMLY GENERATED STRUCTURES --- \n A \n---", Structures.A, "\n ---")
# print("--- RAW RANDOMLY GENERATED STRUCTURES --- \n B \n---", Structures.B, "\n ---")
# print("--- RAW RANDOMLY GENERATED STRUCTURES --- \n Pi \n---", Structures.pi, "\n ---")

# Stochastoc check for each M row in all three output structures | if Raw Sum ~ 1, we're good!
# print("--- RAW SUM OF GENERATED STRUCTURES --- \n Pi \n---", Structures.piRowSum)
# print("--- RAW SUM OF GENERATED STRUCTURES --- \n A \n---", Structures.aRowSums)
# print("--- RAW SUM OF GENERATED STRUCTURES --- \n B \n---", Structures.bRowSums)

# Checking initial state, transition, and observation matricies
# print("------ SHAPE: A MATRIX ------ \n", np.shape(Structures.A),"\n ------------------" )
# print("------ LENGTH: A MATRIX ------ \n", len(Structures.A),"\n ------------------" )

# print("------ SHAPE: B MATRIX ------ \n", np.shape(Structures.B),"\n ------------------" )
# print("------ LENGTH: B MATRIX ------ \n", len(Structures.B),"\n ------------------" )