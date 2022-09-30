#%%
import plotly.graph_objects as go

class GrU_1d:
    def __init__(self, array, label, index):
        self.array = array
        self.label = label
        self.index = [i for i in range(len(array))] if index is None else index
    
    def line(self, title=None):
        self.fig = go.Figure()
        self.fig.add_trace(
            go.Scatter(
                x=self.index, 
                y=self.array,
                mode='markers+lines',
                name=self.label,
            )
        )
        self.fig.update_layout(title=title)
        return self.fig
# %%