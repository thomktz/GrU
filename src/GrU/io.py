"""
Higher-level API for Graph-Utils

"""
import numpy as np
import pandas as pd
from GrU import GrU

def gru(object, *args, **kwargs):
    return GrU(object, *args, **kwargs)

def gline(object, *args, **kwargs):
    """
    GrU-line:
    Equivalent to calling GrU(object).line(*args, **kwargs)
    """
    return GrU(object).line(*args, **kwargs)

def ghist(object, *args, **kwargs):
    """
    GrU-histogram:
    Equivalent to calling GrU(object).hist(*args, **kwargs)
    """
    return GrU(object).hist(*args, **kwargs)

pd.Series.gru = gru
pd.DataFrame.gru = gru

pd.Series.gline = gline
pd.DataFrame.gline = gline

pd.Series.ghist = ghist
pd.DataFrame.ghist = ghist