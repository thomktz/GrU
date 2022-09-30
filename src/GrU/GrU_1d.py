import plotly.graph_objects as go

class GrU_1d:
    def __init__(self, array, label, title, index):
        self.array = array
        self.label = label
        self.title = title
        self.index = [i for i in range(len(array))] if index is None else index
    
    def line(self):
        self.fig = go.Figure()
        