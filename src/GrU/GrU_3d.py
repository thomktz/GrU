class GrU_3d:
    def __init__(array, labels):
        self.array = array
        self.labels = [i for i in range(array.shape[0])] if labels is None else labels