class data:                             # This class is to quickly retrieve pre-processed datasets.

    def dummy():
        dummy_observations = [1,2,0,2,0,2,1,2,0,1,2,0,1,0,2]
        # such that M = 2
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
    