# GrU
Graph Utils for Python

Easily plot all data structures with a unique constructor

```python
from GrU import GrU

gru_list = GrU([0,1,2,3,4], labels='My list')
gru_array = GrU(np.array([0,1,2,3,4]), labels='My numpy array')
gru_2D_array = GrU(np.array([[0,1,2,3,4], [5,6,7,8,9]]), labels=['My first array', 'My second array'])
gru_series = GrU(pd.Series([0,1,2,3,4], name='My pandas Series'))
gru_dataframe = GrU(pd.DataFrame(np.array([[0,1,2,3,4], [5,6,7,8,9]]).T, columns=['My first column', 'My second column']))
```
