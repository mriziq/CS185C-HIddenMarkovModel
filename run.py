from model import HMM
from data import data 

# -------------------------------------------------------------------------------- #
# TODO: Something wrong with initial state matrix after a few iterations.
# pi matrix[i] = gamma[0][i], looks like issue in scaling.
# All values in A, pi matrices seem to be equal ... this is wrong.


#   * Double check recursion alpha, beta, gammas
#   * Improve stochasticity of raw structures
#   * Output and save Test 1 - 6 models
#   * Add any missing documentation
#   * Adjust training split through data.train_malwarefamily(x)?
#
#  Math note on syntax: B = {bj (k)} <-- B[j] = [0.5, 0.5]
# -------------------------------------------------------------------------------- #

dummy_data = data.dummy(300, 3)     # Generate dummy data to test model with parameters T & M (TODO: Make sure dummy data is random using entropy)
maxIter = 100                       # Define maximum iterations
key = data.train_winwebsec()        # Data class retrieves preprocessed training sets
model = HMM()                       # Initialize HMM using start_engine method
print(model.start_engine(key, maxIter))    # Parameters = Observation sequence, Maximum iterations

# model.run_model()                 # Run specific algorithms or run complete model.
# print(model.alpha_pass())
# print(model.beta_pass())
# print(model.gamma_pass())           # Runs alpha, beta pass and gamma/digamma calculations. Returns gammas
# model.getTestScore()              # Returns score = SUM(P( observation k, state q | model ))

