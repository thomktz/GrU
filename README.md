# Graph Utils
GrU - Graph Utils for Python
> Requirements are [plotly](https://github.com/plotly/plotly.py), [numpy](https://github.com/numpy/numpy) and [pandas](https://github.com/pandas-dev/pandas)

Easily plot all data structures with a unique constructor

```python
from GrU import GrU

gru_list = GrU([0,1,2,3,4])
gru_array = GrU(np.array([0,1,2,3,4]))
gru_2D_array = GrU(np.array([[0,1,2,3,4], [5,6,7,8,9]]), labels=['My first array', 'My second array'])
gru_series = GrU(pd.Series([0,1,2,3,4], index=[10,20,30,40,50]))
gru_dataframe = GrU(pd.DataFrame(np.array([[0,1,2,3,4], [5,6,7,8,9]]).T, columns=['My first column', 'My second column']))
```

Then, you can plot your `GrU` object using a compatible method:

```python
gru_object.line()
gru_object.hist()
gru_object.heatmap()
gru_object.image()
```

There is also a high-level API:

```python
from GrU.io import gru

gru_object = gru(my_object)

#Pandas specific methods
gru_series = my_series.gru()
gru_dataframe = my_dataframe.gru()
```

As well as high-level plotting functions

```python
from GrU.io import gline, ghist

fig_line = gline(my_object)
fig_hist = ghist(my_object)

# Or, for pandas objects
my_series.gline()

# Which is equivalent to:
GrU(my_series).line()

```





## Examples:

```python
my_array = np.sort(np.random.random((4,50))**2)
gru(my_array).line("Squared uniform distributions")
```
![sq](https://user-images.githubusercontent.com/60552083/193302023-4dba5382-5a7c-4301-bb58-c5d937525822.png)

```python
random_walks = pd.DataFrame(np.cumsum(np.random.random((5,1000))*2-1, axis=1).T, index=pd.date_range('08/06/2019', '05/01/2022'))
random_walks.gline(mode='lines', title='Random walk trajectories').show()
random_walks.ghist(horizontal=True, barmode='stack', title='Random walk distributions').show()
```

![rwww](https://user-images.githubusercontent.com/60552083/194341693-21b99af6-89a3-4704-ab62-25a33758ec37.png)
![rwwd](https://user-images.githubusercontent.com/60552083/194341711-b975ea4a-28bc-40eb-8d30-f0d245feb0bd.png)



```python 
PI = [int(e) for e in """3.1415926535897932384626433832795028841[...]""".replace('.','')]
gru(PI).hist(title='Frequency of digits in the first 1000 decimals of Pi', normalized=True)
```
![pi](https://user-images.githubusercontent.com/60552083/194286696-095c347b-a4aa-47e7-8fd0-69d99bad2fb0.png)
