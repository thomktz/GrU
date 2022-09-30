import numpy as np
import pandas as pd
from collections import Iterable
from Gru_1d import Gru_1d
from Gru_2d import Gru_2d
from Gru_3d import Gru_3d


class GrU:
    """
    GrU - Graph Utils

    Main dispatch class, will return the correct-sized GrU object (1D, 2D or 3D)
    """
    def __init__(object, labels=None):
        # Numpy arrays
        if isinstance(object, np.ndarray):
            shape = object.shape
            if len(shape) == 1:
                if shape[0] == 0:
                    raise ValueError("Array is of length 0")
                if isinstance(labels, Iterable) and len(labels) != 1:
                    raise ValueError(f"Labels is of length {len(labels)}, while array is of shape (1, {shape[0]}).")
                if labels is None:
                    return Gru_1d(object, "0")
                elif isinstance(labels, Iterable):
                    return Gru_1d(object, labels[0])
                # If not iterable:
                return Gru_1d(object, str(labels))

            elif len(shape) == 2:
                if isinstance(labels, Iterable) and len(labels) != shape[0]:
                    raise ValueError(f"Length of labels ({len(labels)}) should be the same size as the number of rows ({shape[0]}), or be None.")
                if labels is not None:
                    raise ValueError(f"Labels should either be None, or the correct size ({shape[0]} instead of {len(labels)})")
                return Gru_2d(object, labels)
            
            else len(shape) == 3:
                if isinstance(labels, np.ndarray) and labels.shape != shape[:2]:
                    raise ValueError(f"Shape of labels ({labels.shape}) should be the same as the of rows (shape[:2]), or be None.")
                return Gru_3d(object, labels)

        # Pandas Series
        elif isinstance(object, pd.Series):
            if labels is not None:
                if isinstance(labels, Iterable) and len(labels) != 1:
                    raise ValueError(f"Labels should either be None, or the correct size (1 instead of {len(labels)})")
                if labels is None:
                    return Gru_1d(object.values, "0")
                return Gru_1d(object.values, labels)
            
        # Pandas DataFrames
        elif isinstance(object, pd.DataFrame):
            # TODO
            pass

        # Builtin lists
        elif isinstance(object, list):
            return GrU(np.array(object, labels))

        else:
            raise ValueError(f"Type {type(object)} is not accepted.")