#%%
import plotly.graph_objects as go

class GrU_2d:
    def __init__(self, array, labels, index):
        print(type(array), labels)
        self.array = array
        self.labels = labels
        self.index = [i for i in range(array.shape[1])] if index is None else index
    
    def line(self, title=None, mode='markers+lines'):
        self.fig = go.Figure()
        for i, row in enumerate(self.array):
            self.fig.add_trace(
                go.Scatter(
                    x=self.index, 
                    y=row,
                    mode=mode,
                    name=self.labels[i],
                    showlegend=True
                )
            )
        self.fig.update_layout(title=title)
        return self.fig
    
    def hist(self, title=None, normalized=False, horizontal=False, barmode="group", opacity=1, bargap=0, bargroupgap=0):
        """
        GrU_2d.hist - 2d histogram

         - title: str
         - normalized: bool
         - horizontal: bool
         - barmode: str -> One of "overlay", "stack", "group", "relative"
         - opacity: float
         - bargap: float -> Space between bars at different x-coordinates
         - bargroupgap: float -> Space between bars at the same x-coordinates (barmode="group"-specific)
        """

        self.fig = go.Figure()
        for i, row in enumerate(self.array):
            kwargs = dict(opacity=opacity, name=self.labels[i])
            if normalized:
                kwargs['histnorm'] = 'probability'
            if horizontal:
                kwargs['y'] = row
            else:
                kwargs['x'] = row
            self.fig.add_trace(
                go.Histogram(**kwargs)
            )

        self.fig.update_layout(title=title, barmode=barmode, bargap=bargap, bargroupgap=bargroupgap)
        return self.fig
# %%
