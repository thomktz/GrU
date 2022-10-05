#%%
import plotly.graph_objects as go

class GrU_1d:
    def __init__(self, array, label, index):
        self.array = array
        self.label = label
        self.index = [i for i in range(len(array))] if index is None else index
    
    def line(self, title=None, mode='markers+lines'):
        self.fig = go.Figure()
        self.fig.add_trace(
            go.Scatter(
                x=self.index, 
                y=self.array,
                mode=mode,
                name=self.label,
                showlegend=(self.label not in ["0", "", None])
            )
        )
        self.fig.update_layout(title=title)
        return self.fig

    def hist(self, title=None, normalized=False, horizontal=False):
        self.fig = go.Figure()
        kwargs = {}
        if normalized:
            kwargs['histnorm'] = 'probability'
        if horizontal:
            kwargs['y'] = self.array
        else:
            kwargs['x'] = self.array
        self.fig.add_trace(
            go.Histogram(**kwargs)
        )
        self.fig.update_layout(title=title, bargap=0.1)
        return self.fig
