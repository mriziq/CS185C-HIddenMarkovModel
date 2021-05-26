from model import HMM
from data import data
import numpy as np

maxIter = 100

dummy_data = data.dummy()
key = data.train_winwebsec()

model = HMM() 
model.start_engine(key, maxIter)

# model.alpha_pass()
# model.beta_pass()
# model.gamma_pass()
model.run_model()

#   --- TO DO --- 
#   * Double check recursion alpha, beta, gammas
#   * Check calculations of alpha & beta, they're probabailities..
#   * Improve stochasticity of raw structures
#   * Output and save Test 1 - 6 models
#   * Add any missing documentation
#   * Adjust training split through data.train_malwarefamily(x)?
#
#  Math note on syntax: B = {bj (k)} <-- B[j] = [0.5, 0.5]
