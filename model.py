from structures import Structures 
import os
import math



class HMM:
    
    c = []

    def getTestScore(a, b, pi, o):          # GET MODEL SCORE 
        T = len(o)
        N = len(pi)
        alpha = HMM.alpha_pass( a, b, pi, o)

        score = 0
        for i in range(0, N):
            score += alpha[T - 1][i]

        return score

    def alpha_pass(a, b, pi, o):            # ALPHA PASS ALG
        T = len(o)
        N = len(pi)
        alpha = [ [0] * N for i in range(T) ]

        # Compute alpha[0][j]
        HMM.c.append(0)
        for i in range(0, N):
            for j in range(0, T):
                k = pi[i] * b[o[0]][i]
                alpha[0][i] = k
            HMM.c[0] += alpha[0][i]
        
        # print("first transformation of c:", HMM.c)
        # Scale the alhpha[0][i]
        HMM.c[0] = 1.0 / HMM.c[0]
        for i in range(0, N):
            alpha[0][i] = HMM.c[0] * alpha[0][i]

        # Compute alpha[t][i]
        for t in range(1, T):
            HMM.c.append(0)
            
            for i in range(0, N):

                for j in range(0, N):
                    alpha[t][i] += alpha[t-1][j] * a[j][i]

                
                alpha[t][i] *= b[o[t]][i]
                HMM.c[t] += alpha[t][i]
        
        # print("BEFORE CALING ALPHA: ", alpha)
    
        # Scale alpha[t][i]
        for t in range(0, T):
            HMM.c[t] = 1 / HMM.c[t] 
            for i in range(0, N):
                alpha[t][i] = HMM.c[t] * alpha[t][i]
            
        return alpha
    
    def beta_pass(a, b, pi, o):             # BETA PASS ALG
        T = len(o)
        N = len(pi)
        beta = [ [0] * N for i in range(T) ]
        # print(HMM.c)
        
        # Let beta[T-1][i] = 1, scaled by c[t]
        for i in range(0, N):
            beta[T-1][i] = 1 / HMM.c[T-1]
        
        # print("PRINTING b ------ \n",b)
        # print("PRINTING beta ------ \n",beta)

        for t in reversed(range(0, T-1)):
            for i in range(0, N):
                beta[t][i] = 0
                for j in range(0, N):
                    
                    # print("PRINTING o[t+1] ------ \n",o[t+1])
                    # print("PRINTING j ------ \n", j)
                    x = beta[t+1][j] *  a[i][j] * b[o[t+1]][j]
                    beta[t][i] += x
                    
        # print("BEFORE SCALING BETA: ",beta)
        # Scale beta[t][i] with sam scale factor as alpha[t][i]
        for t in reversed(range(0, T-1)):
            for i in range(0, N):
                beta[t][i] = HMM.c[t] * beta[t][i]
        
        return beta

    def gamma_calculations(A, B, Pi, O): # Calculate Gamma matrix
        T = len(O)
        N = len(Pi)

        alpha = HMM.alpha_pass(A, B, Pi, O)
        beta = HMM.beta_pass(A, B, Pi, O)
        gamma = [[0]*N]*T

        # COMPUTING GAMMA 
        for t in range(0, T-1):
            denom = 0
            for i in range(0, N):
                for j in range(0,N):
                    x = alpha[t][i] * A[i][j] * B[O[t+1]][j] * beta[t+1][j]
                    denom += x

            for i in range(0, N):
                for j in range(0, N):
                    # !! TODO: Fix denom by zero error due to zero values in returned beta
                    gamma[t][i] = alpha[t][i] * A[i][j] * B[O[t+1]][j] # / denom 
                    gamma[t][i] = gamma[t][i] +  gamma[t][j] 
        
        # Special case for gamma[T-1][i]
        denom = 0
        for i in range(0, N):
            denom += alpha[T-1][i]
        for i in range(0, N):
            gamma[T-1][i] = alpha[T-1][i] / denom 

        return gamma # // Everything the same
    
    def runHelper(A, B, Pi, O):  # helper function to test alpha/beta pass
            alpha2 = HMM.alpha_pass(A, B, Pi, O) # You must run alpha to get c scale
            beta2 = HMM.beta_pass(A, B, Pi, O)

    def buildModel(O):                      # COMPILES MODEL
        # UNDER CONSTRUCTION
        logProb = 0.0
        oldLogProb = -math.inf
        iterations = 0
        iterate = True
        maxIterations = 100 

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
        return # Pi, A, B, iterations, logProb


N = Structures.N
M = Structures.M

pi_matrix = Structures.pi
a_matrix = Structures.A
b_matrix = Structures.B
dummy_observations = [1,2,0,2,0,2,1,2,0,1,2,0,1,0,2]

#import winwebsec training data
path = "training-data/trainingset_winwebsec.txt"
with open(path, "r") as y:
    train_winwebsec = y.read()

winwebsec_observations = train_winwebsec.split()

for x in range(0, len(winwebsec_observations)):
    winwebsec_observations[x] = int(winwebsec_observations[x])

# score = HMM.getTestScore(a_matrix, b_matrix, pi_matrix, winwebsec_observations)
# alpha = HMM.alpha_pass(a_matrix, b_matrix, pi_matrix, winwebsec_observations)
# beta = HMM.beta_pass(a_matrix, b_matrix, pi_matrix, winwebsec_observations)
# gamma = HMM.gamma_calculations(a_matrix, b_matrix, pi_matrix, dummy_observations)
# helper = HMM.runHelper(a_matrix, b_matrix, pi_matrix, winwebsec_observations)
model = HMM.buildModel(winwebsec_observations)


# TO DO:
# * Put init code in its own main.py file
# * Improve stochasticity of raw structures
# * Fix naming conventions of A/B/Pi throughout HMM Class
# * Add any missing documentation