#%%
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
# %%
