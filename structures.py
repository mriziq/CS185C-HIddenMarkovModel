import random as r 
from random import randint


class Structures:
    # columnxrows
    N = 2
    M = 3
    A = [[0] * N] * N
    B = [[0] * N] * M
    pi = [[0] * N]

    trainSeq = []
    testSeq = [] 

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
    begin = 0.00000000000000001
    end = 0.99999999999999999

    piRowSum = 0
    aRowSums = []
    bRowSums = []
    rowSum = 0
    
    # Generate NxN matrix of random numbers not yet stochastic
    for i in range(0, len(A)):
        for j in range(len(A[i])):
            randomValue = min1 + (max1 - min1) * r.random()
            A[i][j] = randomValue
            rowSum += A[i][j]
        aRowSums.append(rowSum)
        rowSum = 0

    # Generate NxM matrix of random numbers not yet stochastic
    for i in range(0, len(B)):
        for j in range(len(B[i])):
            randomValue = min1 + (max1 - min1) * r.random()
            B[i][j] = randomValue
            rowSum += B[i][j]
        bRowSums.append(rowSum)
        rowSum = 0


    # Generate 1xN matrix of random numbers not yet stochastic
    for i in range(0, len(pi)):
        randomValue = min1 + (max1 - min1) * r.random()
        pi.append(randomValue)
        pi[i] = randomValue

    for i in range(len(pi)):
        piRowSum += pi[i]


    misCalc = 0 #How off the sum of a row is from 1
    reCalc = 0  #How much needs to be distributed or subtracted from each element

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




## DEBUG OUTPUT
# print("\n RAW RANDOME GENERATED STRUCTURES \n")
# print("A: ", Structures.A)
# print("B: ", Structures.B)
# print("pi: ", Structures.pi)

# print("\n RAW SUM OF GENERATED STRUCTURES \n")
# print("piRowSum: ", Structures.piRowSum)
# print("aRowSums: ", Structures.aRowSums)
# print("bRowSums: ", Structures.bRowSums, "\n")

