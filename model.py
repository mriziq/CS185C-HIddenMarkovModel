from structures import Structures 
import os
import math
import numpy as np


class HMM:

    def getTestScore(A, B, pi, O):          # GET MODEL SCORE 
        T = len(O)
        N = len(pi)
        alpha = HMM.alpha_pass( A, B, pi, O)

        score = 0
        for i in range(0, N):
            score += alpha[T - 1][i]

        print("------ MODEL TEST SCORE OUTPUT -------\n", score, "\n -------")

        return score


    def alpha_pass(A, B, pi, O):            # ALPHA PASS ALG
        T = len(O)
        N = len(pi)
        C = [0] * T

        alpha = [ [0] * N for i in range(T) ]
        

        # Compute alpha[0][i]
        
        for i in range(0, N):
            alpha[0][i] = pi[i] * B[i][O[0]]
            C[0] = alpha[0][i]
        
        # Scale the alhpha[0][i]
        C[0] = 1.0 / C[0]
        for i in range(0, N):
            alpha[0][i] = C[0] * alpha[0][i]
        
        # Compute alpha[t][i]
        for t in range(1, T):
            for i in range(0, N):
                for j in range(0, N):
                    alpha[t][i] += alpha[t-1][j] * A[j][i]

                alpha[t][i] *= B[ i ][ O[t] ] # ! POF
                C[t] = alpha[t][i]
            
            # Scale alpha[t][i]
            C[t] = 1 / C[t] 
            for i in range(0, N):
                alpha[t][i] *= C[t]
        
        return alpha
    

    def beta_pass(A, B, pi, O):             # BETA PASS ALG
        T = HMM.T
        N = len(pi)
        beta = [ [0] * N for i in range(T) ]
        C = HMM.C

        # Let beta[T-1][i] = 1, scaled by c[t]
        for i in range(0, N):
            beta[T-1][i] = 1 / C[T-1] # ! Math says betaT-1[i] = 1 scaled by Ct-1


        for t in reversed(range(0, T-1)):
            for i in range(0, N):
                for j in range(0, N):
                    beta[t][i] = A[i][j] * B[j][O[t+1]] * beta[t+1][j]
                    
        # Scale beta[t][i] with same scale factor as alpha[t][i]
            for i in range(0, N):
                beta[t][i] = C[t] * beta[t][i]
        
        return beta


    def runHelper(A, B, Pi, O):  # helper function to test alpha/beta pass
        
        # alpha_helper = HMM.alpha_pass(A, B, Pi, O) # You must run alpha to get c scale
        # c_value = HMM.C
        # beta_helper = HMM.beta_pass(A, B, Pi, O)
        gamma_helper = HMM.gamma_calculations(A, B, Pi, O)
        
        print(" \n ------------------ HELPER OUTPUT --------- \n")

        # print("------ ALPHA PASS OUTPUT -------\n", alpha_helper, "\n-------")
        # print("------ SHAPE ALPHA MATRIX ------ \n", np.shape(alpha_helper),"\n ------------------" )
        # print("------ LENGTH ALPHA MATRIX ------ \n", len(alpha_helper),"\n ------------------" )

        # print("------ C SCALAR (after alpha before beta) -------\n", c_value, "\n-------")
        # print("------ SHAPE C SCALAR ------ \n", np.shape(c_value),"\n ------------------" )
        # print("------ LENGTH C SCALAR ------ \n", len(c_value),"\n ------------------" )
        
        # print("------ BETA PASS OUTPUT -------\n", beta_helper, "\n -------")
        # print("------ SHAPE BETA MATRIX ------ \n", np.shape(beta_helper),"\n ------------------" )
        # print("------ LENGTH BETA MATRIX ------ \n", len(beta_helper),"\n ------------------" )

        print("------ GAMMA CALC OUTPUT -------\n", gamma_helper, "\n -------")
        print("------ SHAPE GAMMA MATRIX ------ \n", np.shape(gamma_helper),"\n ------------------" )
        print("------ LENGTH GAMMA MATRIX ------ \n", len(gamma_helper),"\n ------------------" )

    
    def gamma_calculations(A, B, Pi, O): # Calculate Gamma matrix
        T = HMM.T
        N = len(Pi)

        alpha = HMM.alpha_pass(A, B, Pi, O)
        beta = HMM.beta_pass(A, B, Pi, O)
        gamma = [ [0] * N for i in range(T) ]

        # COMPUTING GAMMA 
        for t in range(0, T-1):
            denom = 0
            for i in range(0, N):
                for j in range(0,N):
                    x = alpha[t][i] * A[i][j] * B[j][O[t+1]] * beta[t+1][j]
                    denom += x

            for i in range(0, N):
                for j in range(0, N):
                    # !!  POF TODO: Fix denom by zero error due to zero values in returned beta
                    gamma[t][i] = alpha[t][i] * A[i][j] * B[j][O[t+1]]  / denom 
                    gamma[t][i] = gamma[t][i] +  gamma[t][j] 
        
        # Special case for gamma[T-1][i]
        denom = 0
        for i in range(0, N):
            denom += alpha[T-1][i]
        for i in range(0, N):
            gamma[T-1][i] = alpha[T-1][i] / denom 

        return gamma 


    def buildModel(O):                      # COMPILES MODEL
        
        # UNDER CONSTRUCTION
        logProb = 0.0
        oldLogProb = -math.inf
        iterations = 0
        iterate = True
        maxIterations = HMM.maxIterations

        # Import raw base (pi ,A, B)
        Pi = Structures.pi
        A = Structures.A
        B = Structures.B 

        # Get matricies' dimensions
        N = len(A)  
        M = len(B[0])
        T = len(O)
        
        while iterate:

            # Calling Gamma calculation (triggers Alpha & Beta pass)
            gamma = HMM.gamma_calculations(A,B,Pi, O)
            
            # Re-estimating pi
            for i in range(0,N):
                Pi[i] = gamma[0][i]

            # Re-estimating A
            for i in range(0,N):
                denom = 0
                for t in range(0,T-1):
                    denom += gamma[t][i]

                for j in range(0,N):
                    numer = 0
                    for t in range(0, T-1):
                        numer += gamma[t][i] +  gamma[t][j]
                    A[i][j] = numer / denom
            
            # Re-estimating B
            for i in range(0, N):
                denom = 0
                for t in range(0, T):
                    denom += gamma[t][i]
                for j in range(0, M):
                    numer = 0
                    for t in range(0, T):
                        if O[t] == j:
                            numer += gamma[t][i]
                    B[i][j] = numer / denom

            # Compute log[P(O | Lambda)]
            for i in range(0, T):
                logProb += math.log(HMM.c[i]) 
            
            logProb *= -1

            # To iterate or not to iterate, that is the question
            iterations += 1
            if iterations < maxIterations and logProb > oldLogProb:
                oldLogProb = logProb
                HMM.gamma_calculations(A, B, Pi, O)
            else:
                iterate = False
        
        print("--- MODEL OUTPUT PI --- \n ",Pi, "\n ---------\n")
        print("--- MODEL OUTPUT A --- \n ",A, "\n ---------\n")
        print("--- MODEL OUTPUT B --- \n ",B, "\n ---------\n")
        print("--- MODEL OUTPUT LEARNING EPOCHS --- \n ",iterations, "\n ---------\n")
        print("--- MODEL OUTPUT log[P(Observation | Lambda)] --- \n ",logProb, "\n ---------\n")
        
        return # Pi, A, B, iterations, logProb              # Might need to store model output?



#   --- TO DO --- 
#   * Clean up init C/T stuff then fix C before beta issue? Re-wire everything back and test through gamma.
#   * Input/Output clean up, function clean up
#   * Improve stochasticity of raw structures
#   * Output and save Test 1 - 6 models
#   * Add any missing documentation
