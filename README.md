Hidden Markov Model written by @mriziq

Use run.py to interface with model.

** Architecture ** 
preprocess.py --> Converts raw data into 0/1/2 symbols representing presence of opcodes in Malware families.

structures.py --> Generates stochatic initial, transition, and observation matrices used in model.py

data.py --> Class to easily call preprocess data into run.py

model.py --> Hidden Markov Model, run_model() compiles and runs recursive alpha-beta-gammas-re-estimation

run.py --> Interface with model.py by specificying observation sequence and max iterations.

** Output ** 

HMM.run_model() returns A, B, pi. It will print A, B, pi, and LogProb