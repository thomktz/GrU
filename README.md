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

## Examples:

```python
my_array = np.sort(np.random.random((4,50))**2)
gru(my_array).line("Squared uniform distributions")
```
![sq](https://user-images.githubusercontent.com/60552083/193302023-4dba5382-5a7c-4301-bb58-c5d937525822.png)

```python
random_walks = pd.DataFrame(np.cumsum(np.random.random((5,1000))*2-1, axis=1).T)
random_walks.gru().line(title='Uniform random walks', mode='lines')
```

![rw](https://user-images.githubusercontent.com/60552083/193304458-0fb328c3-5336-4d54-b6bb-291eccfcac6c.png)
