#%%
import numpy as np
import pandas as pd
from collections.abc import Iterable
from GrU_1d import GrU_1d
from GrU_2d import GrU_2d
from GrU_3d import GrU_3d
#%%

class GrU:
    """
    GrU - Graph Utils

    Main dispatch class, will return the correct-sized GrU object (1D, 2D or 3D)
    
    - 'labels' will always override pandas names/columns
    - pandas index will always override 'index'
    - 'index' must be 1d (for now)
    """
    
    def __new__(self, object, labels=None, index=None):
        # Numpy arrays
        if isinstance(object, np.ndarray):
            shape = object.shape
            if index is not None and len(index) != shape[1]:
                raise ValueError("Index must be thge same length as the array")
            if len(shape) == 1:
                if shape[0] == 0:
                    raise ValueError("Array is of length 0")
                if isinstance(labels, Iterable) and len(labels) != 1:
                    raise ValueError(f"Labels is of length {len(labels)}, while array is of shape (1, {shape[0]}).")
                if labels is None:
                    return GrU_1d(object, "0", index)
                elif isinstance(labels, Iterable):
                    return GrU_1d(object, labels[0], index)
                # If not iterable:
                return GrU_1d(object, str(labels), index)

            elif len(shape) == 2:
                if isinstance(labels, Iterable) and len(labels) != shape[0]:
                    raise ValueError(f"Length of labels ({len(labels)}) should be the same size as the number of rows ({shape[0]}), or be None.")
                if labels is not None:
                    raise ValueError(f"Labels should either be None, or the correct size ({shape[0]} instead of {len(labels)})")
                return GrU_2d(object, labels, index)
            
            elif len(shape) == 3:
                if isinstance(labels, np.ndarray) and labels.shape != shape[:2]:
                    raise ValueError(f"Shape of labels ({labels.shape}) should be the same as the of rows (shape[:2]), or be None.")
                return GrU_3d(object, labels)

            else:
                raise ValueError(f"Dimension of array should be 1, 2 or 3. Found {len(shape)}")

        # Pandas Series
        elif isinstance(object, pd.Series):
            if labels is not None:
                if isinstance(labels, Iterable) and len(labels) != 1:
                    raise ValueError(f"Labels should either be None, or the correct size (1 instead of {len(labels)})")
            if labels is None:
                return GrU_1d(object.values, "0", object.index)
            return GrU_1d(object.values, labels, object.index)
            
        # Pandas DataFrames
        elif isinstance(object, pd.DataFrame):
            # TODO
            pass

        # Builtin lists
        elif isinstance(object, list):
            return GrU(np.array(object), labels)

        else:
            raise ValueError(f"Type {type(object)} is not accepted.")



def gru(object, *args, **kwargs):
    return GrU(object, *args, **kwargs)

pd.Series.gru = gru
pd.DataFrame.gru = gru
