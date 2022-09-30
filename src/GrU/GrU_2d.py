class GrU_2d:
    def __init__(self, array, labels, title, index):
        self.array = array
        self.labels = [i for i in range(array.shape[0])] if labels is None else labels