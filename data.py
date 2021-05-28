import random as r

class data:                                                     # This class is to quickly retrieve pre-processed datasets.

    def counter(lst, x):                                        # Helper function to return element count
        return lst.count(x)

    def splitDataList(list_malware, percent):                   # Helper function to partition datasets
        howManyNumbers = int(round(percent*len(list_malware)))
        shuffled = list_malware[:]
        r.shuffle(shuffled)
        return shuffled[howManyNumbers:], shuffled[:howManyNumbers]
    
    def dummy(T, M):
        dummy_observations = []
        for x in range(0, T+1):
            for i in range(0, M):
                i = r.randint(0, M-1)
                dummy_observations.append(i)

        return dummy_observations

    def train_winwebsec():
        path = "training-data/trainingset_winwebsec.txt"

        with open(path, "r") as y:
            train_winwebsec = y.read()

        winwebsec_observations = train_winwebsec.split()

        for x in range(0, len(winwebsec_observations)):
            winwebsec_observations[x] = int(winwebsec_observations[x])

        train_winwebsec = winwebsec_observations
        
        return train_winwebsec

    def train_zbot():
        path = "training-data/trainingset_zbot.txt"

        with open(path, "r") as y:
            train_zbot = y.read()

        zbot_observations = train_zbot.split()

        for x in range(0, len(zbot_observations)):
            zbot_observations[x] = int(zbot_observations[x])

        train_zbot = zbot_observations
        
        return train_zbot

    def train_zeroaccess():
        path = "training-data/trainingset_zeroaccess.txt"

        with open(path, "r") as y:
            train_zeroaccess = y.read()

        zeroaccess_observations = train_zeroaccess.split()

        for x in range(0, len(zeroaccess_observations)):
            zeroaccess_observations[x] = int(zeroaccess_observations[x])

        train_zeroaccess = zeroaccess_observations
        
        return train_zeroaccess

