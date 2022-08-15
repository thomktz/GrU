#%%
import numpy as np
import plotly.graph_objects as go

def hist_1d(array, *args, **kwargs):
    if len(array.shape) != 1:
        raise ValueError("Array must be one-dimentional")
    
    fig = go.Figure(data=[go.Histogram(x=array)])
    return fig
        
def hist_2d(array, *args, **kwargs):
    if len(array.shape) != 2:
        raise ValueError("Array must be two-dimentional")
    fig = go.Figure()
    for array_1d in array:
        fig.add_trace(go.Histogram(x=array_1d))
    return fig
        
def hist(array, *args, **kwargs):
    num_dim = len(array.shape)
    if num_dim == 1:
        return hist_1d(array, *args, **kwargs)
    elif num_dim == 2:
        return hist_2d(array, *args, **kwargs)
    else:
        raise ValueError(f"Array must be 1 or 2-dimentional. Found {num_dim} dimentions.")
    

class Gru(np.ndarray):
    def __new__(cls, a):
        obj = np.asarray(a).view(cls)
        return obj
    def hist(self, *args, **kwargs):
        return hist(self, *args, **kwargs)

