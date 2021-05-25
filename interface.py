from model import HMM
from structures import Structures


maxIter = 100

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

# model = HMM.buildModel(winwebsec_observations)

run_helper = HMM.runHelper(a_matrix, b_matrix, pi_matrix, winwebsec_observations)
