from numpy.lib.arraysetops import unique
from structures import Structures 
import os
import math
import numpy as np
from data import data

class HMM:
    
    def __init__(self):
        # Import raw base (pi ,A, B)
        self.pi = Structures.pi
        self.A = Structures.A
        self.B = Structures.B
        self.M = Structures.M\
         
    def start_engine(self, O, maxIters):    # CONSTRUCTOR //
                                            # O = observation set [1xT]


        self.O = O                          # Observation sequence
        self.T = len(self.O)                # Length of Observations 
        self.N = len(self.pi)               # Number of states in the model

        self.c_scale = [0] * len(self.O)    # C Scale
        
        self.iterate = True                 # Boolean to turn on loop
        self.iters = 0                      # Iteration counter
        self.maxIters = maxIters            # maxIters = max iterations int

        self.logProb = 0.0                  # HMM Model logRob
        self.oldLogProb = float('-inf')     # 

        self.alpha = [ [0] * self.N         # P( observation k, state q | model )
            for i in range(self.T) ]        
        
        self.beta = [ [0] * self.N          # P( observation k | state q, model )
            for i in range(self.T) ]

        self.digamma = [[ [0] * self.N ] * self.N] * self.T     #
        self.gamma = [ [0] * self.N for i in range(self.T) ]    #


    def getTestScore(self):
        
        HMM.alpha_pass(self)
        # Sum of Alpha Pass
        score = 0
        for i in range(0, self.N):           # SUM(P( observation k, state q | model ))
            score += self.alpha[self.T - 1][i]   

        print("------ MODEL TEST SCORE OUTPUT -------\n", score, "\n -------")
        
        return score

    
    def alpha_pass(self):                   # FORWARD ALG
        alpha = self.alpha

        # Alpha Pass alpha[0]
        self.c_scale[0] = 0
        
        for i in range(0, self.N):
            alpha[0][i] = self.B[i][self.O[0]] * self.pi[i]
            self.c_scale[0] += alpha[0][i]
        
        # Scale alhpha[0][i]
        self.c_scale[0] = 1.0 / self.c_scale[0]
        for i in range(0, self.N):
            alpha[0][i] *= self.c_scale[0]
        
        # Alpha Pass 
        for t in range(1, self.T):
            self.c_scale[t] = 0
            for i in range(0, self.N):
                alpha[t][i] = 0
                for j in range(0, self.N):
                    alpha[t][i] += alpha[t-1][j] * self.A[j][i]

                alpha[t][i] *= self.B[ i ][ self.O[t] ] 
                self.c_scale[t] += alpha[t][i]
            
            # Scale Alpha
            self.c_scale[t] = 1 / self.c_scale[t] 
            for i in range(0, self.N):
                alpha[t][i] *= self.c_scale[t]

        self.alpha = alpha
        return self.alpha
    

    def beta_pass(self):                       # BACKWARD ALG
        beta = self.beta

        # Beta Pass beta[T-1]
        for i in range(0, self.N):
            beta[self.T-1][i] = 1 / self.c_scale[self.T-1] 

        # Beta Pass
        for t in reversed(range(0, self.T-1)):
            for i in range(0, self.N):
                for j in range(0, self.N):
                    beta[t][i] = beta[t][i] + self.A[i][j] * self.B[j][self.O[t+1]] * beta[t+1][j]
                    
            # Scale Beta
            for i in range(0, self.N):
                beta[t][i] = self.c_scale[t] * beta[t][i]
        
        self.beta = beta
        return self.beta


    def gamma_pass(self):

        # Complile forward and backward layers
        HMM.alpha_pass(self)
        HMM.beta_pass(self)
        
        gamma = self.gamma
        digamma = self.digamma
        
        # Gamma and Digamma computation
        for t in range(0, self.T-1):
            denom = 0
            for i in range(0, self.N):
                for j in range(0, self.N):
                    denom += self.alpha[t][i] * self.A[i][j] * self.B[j][ self.O[t+1] ] * self.beta[t+1][j]
                    
            for i in range(0, self.N):
                gamma[t][i] = 0
                for j in range(0, self.N):
                    digamma[t][i][j] = self.alpha[t][i] * self.A[i][j] * self.B[j][self.O[t+1]] * self.beta[t+1][j] / denom
                    gamma[t][i] += digamma[t][i][j]

        # Special case for Gamma[T-1][i]
        denom = 0
        for i in range(0, self.N):
            denom += self.alpha[self.T-1][i]

        for i in range(0,self.N):
            gamma[self.T-1][i] = self.alpha[self.T-1][i] / denom

        self.gamma = gamma
        self.digamma = digamma
        return self.gamma, self.digamma


    def run_model(self):

        while(self.iterate):
            
            # Run compiled alpha pass, beta pass, gammas transformation
            HMM.gamma_pass(self)
            print(self.alpha)

            # Re-estimate pi
            for i in range(0, self.N):
                self.pi[i] = self.gamma[0][i]
            
            # Re-estimate A
            for i in range(0, self.N):
                denom = 0
                for t in range(0, self.T-1):
                    denom += self.gamma[t][i]
                
                for j in range(0,self.N):
                    numer = 0
                    for t in range(0, self.T-1):
                        numer += self.digamma[t][i][j]
                
                    self.A[i][j] = numer / denom

            # Re-estimate B
            for i in range(0, self.N):
                denom = 0
                for t in range(0, self.T):
                    denom += self.gamma[t][i]
                for j in range(0, self.M):
                    numer = 0
                    for t in range(0, self.T):
                        if self.O[t] == j:
                            numer += self.gamma[t][i]
                    
                    self.B[i][j] = numer / denom

            self.logProb = 0.0
            for i in range(0, self.T):
                self.logProb += math.log(self.c_scale[i])
            
            self.logProb *= -1

            self.iters += 1
            if self.iters < self.maxIters and self.logProb > self.oldLogProb:
                self.oldLogProb = self.logProb
                # go to alpha -> beta -> gammas
            else:
                self.iterate = False
        
        print("\n------------ MODEL OUTPUT -------------\n")
        print("\n------------ Lambda(pi) -------------\n", self.pi, "\n-------------------------")
        print("\n------------ Lambda(A) -------------\n", self.A, "\n-------------------------")
        print("\n------------ Lambda(B) -------------\n", self.B, "\n-------------------------")
        print("\n------------ LogProb(O | Lambda) -------------\n", self.logProb, "\n-------------------------")
        
        return self.pi, self.A, self.B
