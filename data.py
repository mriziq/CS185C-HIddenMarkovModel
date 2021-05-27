class data:

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

    