# Graph Utils
GrU - Graph Utils for Python

Easily plot all data structures with a unique constructor

```python
from GrU import GrU

gru_list = GrU([0,1,2,3,4])
gru_array = GrU(np.array([0,1,2,3,4]))
gru_2D_array = GrU(np.array([[0,1,2,3,4], [5,6,7,8,9]]), labels=['My first array', 'My second array'])
gru_series = GrU(pd.Series([0,1,2,3,4], index=[10,20,30,40,50]))
gru_dataframe = GrU(pd.DataFrame(np.array([[0,1,2,3,4], [5,6,7,8,9]]).T, columns=['My first column', 'My second column']))
```

You can also use a builder function:

```python
from GrU import gru

gru_object = gru(my_object)
```

or, for `pandas` objects, builder methods:

```python
from GrU import _

gru_series = my_series.gru()
gru_dataframe = my_dataframe.gru()
```

Then, you can plot your `GrU` object using a compatible method:

```python
gru_object.line()
gru_object.hist()
gru_object.heatmap()
gru_object.image()
```
