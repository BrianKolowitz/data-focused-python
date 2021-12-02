---
layout: default
title: 05 - 10 minutes to pandas
parent: Topic 10 - Data Processing and Visualization Part 1
grand_parent: Lectures
nav_order: 5
---
# 10 Minutes to pandas

[Source](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)

This is a short introduction to pandas, geared mainly for new users. You can see more complex recipes in the [Cookbook](http://pandas.pydata.org/pandas-docs/stable/cookbook.html#cookbook) 

Customarily, we import as follows:


```python
import pandas as pd
import numpy as np
```

## Object Creation

See the [Data Structure Intro section](http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dsintro) 

Creating a Series by passing a list of values, letting pandas create a default integer index:


```python
s = pd.Series([1,3,5,np.nan,6,8])
```


```python
s
```




    0    1.0
    1    3.0
    2    5.0
    3    NaN
    4    6.0
    5    8.0
    dtype: float64



Creating a [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame) by passing a numpy array, with a datetime index and labeled columns:


```python
dates = pd.date_range('20130101', periods=6)
```


```python
dates
```




    DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
                   '2013-01-05', '2013-01-06'],
                  dtype='datetime64[ns]', freq='D')




```python
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-0.534377</td>
      <td>-1.166835</td>
      <td>0.552817</td>
      <td>0.295235</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.168310</td>
      <td>0.852970</td>
      <td>-1.926660</td>
      <td>0.271516</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.494489</td>
      <td>-1.784271</td>
      <td>-0.122635</td>
      <td>-1.121595</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.635309</td>
      <td>-0.263418</td>
      <td>0.137195</td>
      <td>-0.353788</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.771968</td>
      <td>-0.698785</td>
      <td>-1.119105</td>
      <td>2.817852</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1.367584</td>
      <td>-1.239054</td>
      <td>-1.154439</td>
      <td>-0.714427</td>
    </tr>
  </tbody>
</table>
</div>



Creating a [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame) by passing a dict of objects that can be converted to series-like.


```python
df2 = pd.DataFrame({'A':1.,
                   'B':pd.Timestamp('20130102'),
                   'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                   'D':np.array([3]*4,dtype='int32'),
                   'E':pd.Categorical(["test","train","test","train"]),
                   'F':'foo'})
```


```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>2013-01-02</td>
      <td>1.0</td>
      <td>3</td>
      <td>test</td>
      <td>foo</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>2013-01-02</td>
      <td>1.0</td>
      <td>3</td>
      <td>train</td>
      <td>foo</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>2013-01-02</td>
      <td>1.0</td>
      <td>3</td>
      <td>test</td>
      <td>foo</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>2013-01-02</td>
      <td>1.0</td>
      <td>3</td>
      <td>train</td>
      <td>foo</td>
    </tr>
  </tbody>
</table>
</div>



The columns of the resulting [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame) have different [dtypes](http://pandas.pydata.org/pandas-docs/stable/basics.html#basics-dtypes)


```python
df2.dtypes
```




    A           float64
    B    datetime64[ns]
    C           float32
    D             int32
    E          category
    F            object
    dtype: object



If you’re using IPython, tab completion for column names (as well as public attributes) is automatically enabled. Here’s a subset of the attributes that will be completed:


```python
# df2.<TAB>
```

As you can see, the columns A, B, C, and D are automatically tab completed. E is there as well; the rest of the attributes have been truncated for brevity.

## Viewing Data

See the [Basics section](http://pandas.pydata.org/pandas-docs/stable/basics.html#basics) 

Here is how to view the top and bottom rows of the frame:


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-0.534377</td>
      <td>-1.166835</td>
      <td>0.552817</td>
      <td>0.295235</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.168310</td>
      <td>0.852970</td>
      <td>-1.926660</td>
      <td>0.271516</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.494489</td>
      <td>-1.784271</td>
      <td>-0.122635</td>
      <td>-1.121595</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.635309</td>
      <td>-0.263418</td>
      <td>0.137195</td>
      <td>-0.353788</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.771968</td>
      <td>-0.698785</td>
      <td>-1.119105</td>
      <td>2.817852</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.tail(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-04</th>
      <td>-0.635309</td>
      <td>-0.263418</td>
      <td>0.137195</td>
      <td>-0.353788</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.771968</td>
      <td>-0.698785</td>
      <td>-1.119105</td>
      <td>2.817852</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1.367584</td>
      <td>-1.239054</td>
      <td>-1.154439</td>
      <td>-0.714427</td>
    </tr>
  </tbody>
</table>
</div>



Display the index and columns


```python
df.index
```




    DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
                   '2013-01-05', '2013-01-06'],
                  dtype='datetime64[ns]', freq='D')




```python
df.columns
```




    Index(['A', 'B', 'C', 'D'], dtype='object')



`DataFrame.to_numpy()` gives a NumPy representation of the underlying data. Note that this can be an expensive operation when your DataFrame has columns with different data types, which comes down to a fundamental difference between pandas and NumPy: NumPy arrays have one dtype for the entire array, while pandas DataFrames have one dtype per column. When you call `DataFrame.to_numpy()`, pandas will find the NumPy dtype that can hold all of the dtypes in the DataFrame. This may end up being object, which requires casting every value to a Python object.

For df, our DataFrame of all floating-point values, `DataFrame.to_numpy()` is fast and doesn’t require copying data.


```python
df.to_numpy()
```




    array([[-0.53437674, -1.16683512,  0.55281704,  0.29523502],
           [-1.1683095 ,  0.85296952, -1.92665959,  0.27151637],
           [-0.49448947, -1.7842706 , -0.12263523, -1.12159537],
           [-0.63530907, -0.26341834,  0.13719517, -0.35378752],
           [-0.77196761, -0.69878492, -1.11910468,  2.81785201],
           [ 1.36758353, -1.23905373, -1.15443949, -0.71442688]])



For df2, the DataFrame with multiple dtypes, DataFrame.to_numpy() is relatively expensive.


```python
df2.to_numpy()
```




    array([[1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
           [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo'],
           [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
           [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo']],
          dtype=object)



[`describe`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe) shows a quick statistic summary of your data


```python
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>6.000000</td>
      <td>6.000000</td>
      <td>6.000000</td>
      <td>6.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>-0.372811</td>
      <td>-0.716566</td>
      <td>-0.605471</td>
      <td>0.199132</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.886671</td>
      <td>0.925725</td>
      <td>0.942023</td>
      <td>1.396911</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-1.168310</td>
      <td>-1.784271</td>
      <td>-1.926660</td>
      <td>-1.121595</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-0.737803</td>
      <td>-1.220999</td>
      <td>-1.145606</td>
      <td>-0.624267</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>-0.584843</td>
      <td>-0.932810</td>
      <td>-0.620870</td>
      <td>-0.041136</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>-0.504461</td>
      <td>-0.372260</td>
      <td>0.072238</td>
      <td>0.289305</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.367584</td>
      <td>0.852970</td>
      <td>0.552817</td>
      <td>2.817852</td>
    </tr>
  </tbody>
</table>
</div>



Transposing your data


```python
df.T
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2013-01-01</th>
      <th>2013-01-02</th>
      <th>2013-01-03</th>
      <th>2013-01-04</th>
      <th>2013-01-05</th>
      <th>2013-01-06</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>-0.534377</td>
      <td>-1.168310</td>
      <td>-0.494489</td>
      <td>-0.635309</td>
      <td>-0.771968</td>
      <td>1.367584</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-1.166835</td>
      <td>0.852970</td>
      <td>-1.784271</td>
      <td>-0.263418</td>
      <td>-0.698785</td>
      <td>-1.239054</td>
    </tr>
    <tr>
      <th>C</th>
      <td>0.552817</td>
      <td>-1.926660</td>
      <td>-0.122635</td>
      <td>0.137195</td>
      <td>-1.119105</td>
      <td>-1.154439</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.295235</td>
      <td>0.271516</td>
      <td>-1.121595</td>
      <td>-0.353788</td>
      <td>2.817852</td>
      <td>-0.714427</td>
    </tr>
  </tbody>
</table>
</div>



Sorting by an axis


```python
df.sort_index(axis=1, ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>D</th>
      <th>C</th>
      <th>B</th>
      <th>A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>0.295235</td>
      <td>0.552817</td>
      <td>-1.166835</td>
      <td>-0.534377</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>0.271516</td>
      <td>-1.926660</td>
      <td>0.852970</td>
      <td>-1.168310</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-1.121595</td>
      <td>-0.122635</td>
      <td>-1.784271</td>
      <td>-0.494489</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.353788</td>
      <td>0.137195</td>
      <td>-0.263418</td>
      <td>-0.635309</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>2.817852</td>
      <td>-1.119105</td>
      <td>-0.698785</td>
      <td>-0.771968</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>-0.714427</td>
      <td>-1.154439</td>
      <td>-1.239054</td>
      <td>1.367584</td>
    </tr>
  </tbody>
</table>
</div>



Sorting by value


```python
df.sort_values(by='B')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-03</th>
      <td>-0.494489</td>
      <td>-1.784271</td>
      <td>-0.122635</td>
      <td>-1.121595</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1.367584</td>
      <td>-1.239054</td>
      <td>-1.154439</td>
      <td>-0.714427</td>
    </tr>
    <tr>
      <th>2013-01-01</th>
      <td>-0.534377</td>
      <td>-1.166835</td>
      <td>0.552817</td>
      <td>0.295235</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.771968</td>
      <td>-0.698785</td>
      <td>-1.119105</td>
      <td>2.817852</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.635309</td>
      <td>-0.263418</td>
      <td>0.137195</td>
      <td>-0.353788</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.168310</td>
      <td>0.852970</td>
      <td>-1.926660</td>
      <td>0.271516</td>
    </tr>
  </tbody>
</table>
</div>



## Selection

>**Note:** While standard Python / Numpy expressions for selecting and setting are intuitive and come in handy for interactive work, for production code, we recommend the optimized pandas data access methods, .at, .iat, .loc, .iloc.

See the indexing documentation [Indexing and Selecting Data](http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing) and [MultiIndex / Advanced Indexing](http://pandas.pydata.org/pandas-docs/stable/advanced.html#advanced)

### Getting

Selecting a single column, which yields a Series, equivalent to df.A


```python
df['A']
```




    2013-01-01   -0.534377
    2013-01-02   -1.168310
    2013-01-03   -0.494489
    2013-01-04   -0.635309
    2013-01-05   -0.771968
    2013-01-06    1.367584
    Freq: D, Name: A, dtype: float64



Selecting via [], which slices the rows.


```python
df[0:3]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-0.534377</td>
      <td>-1.166835</td>
      <td>0.552817</td>
      <td>0.295235</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.168310</td>
      <td>0.852970</td>
      <td>-1.926660</td>
      <td>0.271516</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.494489</td>
      <td>-1.784271</td>
      <td>-0.122635</td>
      <td>-1.121595</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['20130102':'20130104']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>-1.168310</td>
      <td>0.852970</td>
      <td>-1.926660</td>
      <td>0.271516</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.494489</td>
      <td>-1.784271</td>
      <td>-0.122635</td>
      <td>-1.121595</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.635309</td>
      <td>-0.263418</td>
      <td>0.137195</td>
      <td>-0.353788</td>
    </tr>
  </tbody>
</table>
</div>



### Selection by Label

See more in [Selection by Label](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#indexing-label)

For getting a cross section using a label:


```python
df.loc[dates[0]]
```




    A   -0.534377
    B   -1.166835
    C    0.552817
    D    0.295235
    Name: 2013-01-01 00:00:00, dtype: float64



Selecting on a multi-axis by label:


```python
df.loc[:,['A','B']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-0.534377</td>
      <td>-1.166835</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.168310</td>
      <td>0.852970</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.494489</td>
      <td>-1.784271</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.635309</td>
      <td>-0.263418</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.771968</td>
      <td>-0.698785</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1.367584</td>
      <td>-1.239054</td>
    </tr>
  </tbody>
</table>
</div>



Showing label slicing, both endpoints are included


```python
df.loc['20130102':'20130104',['A','B']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>-1.168310</td>
      <td>0.852970</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.494489</td>
      <td>-1.784271</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.635309</td>
      <td>-0.263418</td>
    </tr>
  </tbody>
</table>
</div>



Reduction in the dimensions of the returned object


```python
df.loc['20130102',['A','B']]
```




    A   -1.16831
    B    0.85297
    Name: 2013-01-02 00:00:00, dtype: float64



For getting fast access to a scalar (equivalent to the prior method):


```python
df.loc[dates[0],'A']
```




    -0.5343767371269155



### Selection by Position

See more in [Selection by Position](http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-integer)

Select via the position of the passed integers


```python
df.iloc[3]
```




    A   -0.635309
    B   -0.263418
    C    0.137195
    D   -0.353788
    Name: 2013-01-04 00:00:00, dtype: float64



By integer slices, acting similar to numpy/python


```python
df.iloc[3:5,0:2]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-04</th>
      <td>-0.635309</td>
      <td>-0.263418</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.771968</td>
      <td>-0.698785</td>
    </tr>
  </tbody>
</table>
</div>



By lists of integer position locations, similar to the numpy/python style


```python
df.iloc[[1,2,4],[0,2]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>-1.168310</td>
      <td>-1.926660</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.494489</td>
      <td>-0.122635</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.771968</td>
      <td>-1.119105</td>
    </tr>
  </tbody>
</table>
</div>



For slicing rows explicitly


```python
df.iloc[1:3,:]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>-1.168310</td>
      <td>0.852970</td>
      <td>-1.926660</td>
      <td>0.271516</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.494489</td>
      <td>-1.784271</td>
      <td>-0.122635</td>
      <td>-1.121595</td>
    </tr>
  </tbody>
</table>
</div>



For slicing columns explicitly


```python
df.iloc[:,1:3]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-1.166835</td>
      <td>0.552817</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>0.852970</td>
      <td>-1.926660</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-1.784271</td>
      <td>-0.122635</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.263418</td>
      <td>0.137195</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.698785</td>
      <td>-1.119105</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>-1.239054</td>
      <td>-1.154439</td>
    </tr>
  </tbody>
</table>
</div>



For getting a value explicitly


```python
df.iloc[1,1]
```




    0.8529695184142756



For getting fast access to a scalar (equiv to the prior method)


```python
df.iat[1,1]
```




    0.8529695184142756



## Boolean Indexing

Using a single column’s values to select data.


```python
df[df["A"] > 0]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-06</th>
      <td>1.367584</td>
      <td>-1.239054</td>
      <td>-1.154439</td>
      <td>-0.714427</td>
    </tr>
  </tbody>
</table>
</div>



Selecting values from a DataFrame where a boolean condition is met.


```python
df[df > 0]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.552817</td>
      <td>0.295235</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>NaN</td>
      <td>0.85297</td>
      <td>NaN</td>
      <td>0.271516</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.137195</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.817852</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1.367584</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



Using the `isin()` method for filtering:


```python
df2 = df.copy()
```


```python
df2['E'] = ['one','one', 'two','three','four','three']
```


```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-0.534377</td>
      <td>-1.166835</td>
      <td>0.552817</td>
      <td>0.295235</td>
      <td>one</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.168310</td>
      <td>0.852970</td>
      <td>-1.926660</td>
      <td>0.271516</td>
      <td>one</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.494489</td>
      <td>-1.784271</td>
      <td>-0.122635</td>
      <td>-1.121595</td>
      <td>two</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.635309</td>
      <td>-0.263418</td>
      <td>0.137195</td>
      <td>-0.353788</td>
      <td>three</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.771968</td>
      <td>-0.698785</td>
      <td>-1.119105</td>
      <td>2.817852</td>
      <td>four</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1.367584</td>
      <td>-1.239054</td>
      <td>-1.154439</td>
      <td>-0.714427</td>
      <td>three</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2[df2['E'].isin(['two','four'])]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-03</th>
      <td>-0.494489</td>
      <td>-1.784271</td>
      <td>-0.122635</td>
      <td>-1.121595</td>
      <td>two</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.771968</td>
      <td>-0.698785</td>
      <td>-1.119105</td>
      <td>2.817852</td>
      <td>four</td>
    </tr>
  </tbody>
</table>
</div>



## Setting

Setting a new column automatically aligns the data by the indexes


```python
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102',periods=6))
```


```python
s1
```




    2013-01-02    1
    2013-01-03    2
    2013-01-04    3
    2013-01-05    4
    2013-01-06    5
    2013-01-07    6
    Freq: D, dtype: int64




```python
df['F'] = s1
```

Setting values by label


```python
df.at[dates[0],'A'] = 0
```

Settomg values by position


```python
df.iat[0,1] = 0
```

Setting by assigning with a numpy array


```python
df.loc[:,'D'] = np.array([5] * len(df))
```

The result of the prior setting operations


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.552817</td>
      <td>5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.168310</td>
      <td>0.852970</td>
      <td>-1.926660</td>
      <td>5</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.494489</td>
      <td>-1.784271</td>
      <td>-0.122635</td>
      <td>5</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.635309</td>
      <td>-0.263418</td>
      <td>0.137195</td>
      <td>5</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.771968</td>
      <td>-0.698785</td>
      <td>-1.119105</td>
      <td>5</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1.367584</td>
      <td>-1.239054</td>
      <td>-1.154439</td>
      <td>5</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>



A where operation with setting.


```python
df2 = df.copy()
```


```python
df2[df2 > 0] = -df2
```


```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-0.552817</td>
      <td>-5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.168310</td>
      <td>-0.852970</td>
      <td>-1.926660</td>
      <td>-5</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.494489</td>
      <td>-1.784271</td>
      <td>-0.122635</td>
      <td>-5</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.635309</td>
      <td>-0.263418</td>
      <td>-0.137195</td>
      <td>-5</td>
      <td>-3.0</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.771968</td>
      <td>-0.698785</td>
      <td>-1.119105</td>
      <td>-5</td>
      <td>-4.0</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>-1.367584</td>
      <td>-1.239054</td>
      <td>-1.154439</td>
      <td>-5</td>
      <td>-5.0</td>
    </tr>
  </tbody>
</table>
</div>



## Missing Data

pandas primarily uses the value `np.nan` to represent missing data. It is by default not included in computations. See the Missing Data section

Reindexing allows you to change/add/delete the index on a specified axis. This returns a copy of the data.


```python
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
```


```python
df1.loc[dates[0]:dates[1],'E'] = 1
```


```python
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>F</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.552817</td>
      <td>5</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.168310</td>
      <td>0.852970</td>
      <td>-1.926660</td>
      <td>5</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.494489</td>
      <td>-1.784271</td>
      <td>-0.122635</td>
      <td>5</td>
      <td>2.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.635309</td>
      <td>-0.263418</td>
      <td>0.137195</td>
      <td>5</td>
      <td>3.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



To drop any rows that have missing data.


```python
df1.dropna(how='any')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>F</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>-1.16831</td>
      <td>0.85297</td>
      <td>-1.92666</td>
      <td>5</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



Filling missing data


```python
df1.fillna(value=5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>F</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.552817</td>
      <td>5</td>
      <td>5.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.168310</td>
      <td>0.852970</td>
      <td>-1.926660</td>
      <td>5</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.494489</td>
      <td>-1.784271</td>
      <td>-0.122635</td>
      <td>5</td>
      <td>2.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.635309</td>
      <td>-0.263418</td>
      <td>0.137195</td>
      <td>5</td>
      <td>3.0</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>



To get the boolean mask where values are nan


```python
pd.isnull(df1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>F</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## Operations

See the [Basic section on Binary Ops](http://pandas.pydata.org/pandas-docs/stable/basics.html#basics-binop)

### Stats

Operations in general exclude missing data.

Performing a descriptive statistic


```python
df.mean()
```




    A   -0.283749
    B   -0.522093
    C   -0.605471
    D    5.000000
    F    3.000000
    dtype: float64



Same operation on the other axis


```python
df.mean(1)
```




    2013-01-01    1.388204
    2013-01-02    0.751600
    2013-01-03    0.919721
    2013-01-04    1.447694
    2013-01-05    1.282029
    2013-01-06    1.794818
    Freq: D, dtype: float64



Operating with objects that have different dimensionality and need alignment. In addition, pandas automatically broadcasts along the specified dimension.


```python
s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
```


```python
s
```




    2013-01-01    NaN
    2013-01-02    NaN
    2013-01-03    1.0
    2013-01-04    3.0
    2013-01-05    5.0
    2013-01-06    NaN
    Freq: D, dtype: float64




```python
df.sub(s, axis='index')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-1.494489</td>
      <td>-2.784271</td>
      <td>-1.122635</td>
      <td>4.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-3.635309</td>
      <td>-3.263418</td>
      <td>-2.862805</td>
      <td>2.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-5.771968</td>
      <td>-5.698785</td>
      <td>-6.119105</td>
      <td>0.0</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### Apply

Applying functions to the data


```python
df.apply(np.cumsum)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.552817</td>
      <td>5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-1.168310</td>
      <td>0.852970</td>
      <td>-1.373843</td>
      <td>10</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-1.662799</td>
      <td>-0.931301</td>
      <td>-1.496478</td>
      <td>15</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-2.298108</td>
      <td>-1.194719</td>
      <td>-1.359283</td>
      <td>20</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-3.070076</td>
      <td>-1.893504</td>
      <td>-2.478387</td>
      <td>25</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>-1.702492</td>
      <td>-3.132558</td>
      <td>-3.632827</td>
      <td>30</td>
      <td>15.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.apply(lambda x: x.max() - x.min())
```




    A    2.535893
    B    2.637240
    C    2.479477
    D    0.000000
    F    4.000000
    dtype: float64



### Histogramming

See more at [Histogramming and Discretization](http://pandas.pydata.org/pandas-docs/stable/basics.html#basics-discretization)


```python
s = pd.Series(np.random.randint(0, 7, size=10))
```


```python
s
```




    0    2
    1    6
    2    6
    3    0
    4    1
    5    6
    6    3
    7    0
    8    4
    9    3
    dtype: int64




```python
s.value_counts()
```




    6    3
    0    2
    3    2
    2    1
    1    1
    4    1
    dtype: int64



### String Methods

Series is equipped with a set of string processing methods in the str attribute that make it easy to operate on each element of the array, as in the code snippet below. Note that pattern-matching in str generally uses [regular expressions](https://docs.python.org/2/library/re.html) by default (and in some cases always uses them). See more at [Vectorized String Methods](http://pandas.pydata.org/pandas-docs/stable/text.html#text-string-methods).


```python
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
```


```python
s.str.lower()
```




    0       a
    1       b
    2       c
    3    aaba
    4    baca
    5     NaN
    6    caba
    7     dog
    8     cat
    dtype: object



## Merge

### Concat

pandas provides various facilities for easily combining together Series, DataFrame, and Panel objects with various kinds of set logic for the indexes and relational algebra functionality in the case of join / merge-type operations.

See the [Merging section](http://pandas.pydata.org/pandas-docs/stable/merging.html#merging)

Concatenating pandas objects together with concat():


```python
df = pd.DataFrame(np.random.randn(10, 4))
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.162034</td>
      <td>0.087086</td>
      <td>-0.142747</td>
      <td>0.558215</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.548816</td>
      <td>-0.803596</td>
      <td>1.334449</td>
      <td>0.847867</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.001181</td>
      <td>1.259244</td>
      <td>-0.325483</td>
      <td>0.138625</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.880145</td>
      <td>1.878703</td>
      <td>0.217188</td>
      <td>-0.343998</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.372847</td>
      <td>-0.923290</td>
      <td>-0.284173</td>
      <td>-0.869420</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.399153</td>
      <td>-1.378420</td>
      <td>1.009660</td>
      <td>1.317131</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.657825</td>
      <td>-1.498784</td>
      <td>1.135572</td>
      <td>0.450978</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.324518</td>
      <td>0.125814</td>
      <td>-0.158583</td>
      <td>0.311181</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.165542</td>
      <td>1.455108</td>
      <td>-0.897792</td>
      <td>0.829469</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.456223</td>
      <td>1.199397</td>
      <td>1.349931</td>
      <td>0.146795</td>
    </tr>
  </tbody>
</table>
</div>




```python
# break it into pieces
pieces = [df[:3], df[3:7], df[7:]]
```


```python
pd.concat(pieces)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.162034</td>
      <td>0.087086</td>
      <td>-0.142747</td>
      <td>0.558215</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.548816</td>
      <td>-0.803596</td>
      <td>1.334449</td>
      <td>0.847867</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.001181</td>
      <td>1.259244</td>
      <td>-0.325483</td>
      <td>0.138625</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.880145</td>
      <td>1.878703</td>
      <td>0.217188</td>
      <td>-0.343998</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.372847</td>
      <td>-0.923290</td>
      <td>-0.284173</td>
      <td>-0.869420</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.399153</td>
      <td>-1.378420</td>
      <td>1.009660</td>
      <td>1.317131</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.657825</td>
      <td>-1.498784</td>
      <td>1.135572</td>
      <td>0.450978</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.324518</td>
      <td>0.125814</td>
      <td>-0.158583</td>
      <td>0.311181</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.165542</td>
      <td>1.455108</td>
      <td>-0.897792</td>
      <td>0.829469</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.456223</td>
      <td>1.199397</td>
      <td>1.349931</td>
      <td>0.146795</td>
    </tr>
  </tbody>
</table>
</div>



>Note
>Adding a column to a DataFrame is relatively fast. However, adding a row requires a copy, and may be expensive. We recommend passing a pre-built list of records to the DataFrame constructor instead of building a DataFrame by iteratively appending records to it. See Appending to dataframe for more.

### Join

SQL style merges. See the [Database style joining](http://pandas.pydata.org/pandas-docs/stable/merging.html#merging-join)


```python
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
```


```python
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
```


```python
left
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>lval</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>foo</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>foo</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
right
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>rval</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>foo</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>foo</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(left, right, on='key')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>lval</th>
      <th>rval</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>foo</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>foo</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>foo</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>foo</td>
      <td>2</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



### Append

Append rows to a dataframe. See the [Appending](http://pandas.pydata.org/pandas-docs/stable/merging.html#merging-concatenation)


```python
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.867114</td>
      <td>1.426597</td>
      <td>0.840503</td>
      <td>2.261433</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.484687</td>
      <td>0.435644</td>
      <td>1.423093</td>
      <td>0.293836</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.004340</td>
      <td>-0.854240</td>
      <td>-0.934477</td>
      <td>0.760949</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.445353</td>
      <td>1.012254</td>
      <td>1.895479</td>
      <td>0.606886</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.123227</td>
      <td>-0.665844</td>
      <td>-0.513377</td>
      <td>-0.755661</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.094718</td>
      <td>0.925687</td>
      <td>-1.507613</td>
      <td>0.084735</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.508655</td>
      <td>-0.675627</td>
      <td>0.795865</td>
      <td>0.981134</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-1.617992</td>
      <td>0.991570</td>
      <td>-0.512536</td>
      <td>-1.758008</td>
    </tr>
  </tbody>
</table>
</div>




```python
s = df.iloc[3]
```


```python
df.append(s, ignore_index=True)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.867114</td>
      <td>1.426597</td>
      <td>0.840503</td>
      <td>2.261433</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.484687</td>
      <td>0.435644</td>
      <td>1.423093</td>
      <td>0.293836</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.004340</td>
      <td>-0.854240</td>
      <td>-0.934477</td>
      <td>0.760949</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.445353</td>
      <td>1.012254</td>
      <td>1.895479</td>
      <td>0.606886</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.123227</td>
      <td>-0.665844</td>
      <td>-0.513377</td>
      <td>-0.755661</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.094718</td>
      <td>0.925687</td>
      <td>-1.507613</td>
      <td>0.084735</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-0.508655</td>
      <td>-0.675627</td>
      <td>0.795865</td>
      <td>0.981134</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-1.617992</td>
      <td>0.991570</td>
      <td>-0.512536</td>
      <td>-1.758008</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.445353</td>
      <td>1.012254</td>
      <td>1.895479</td>
      <td>0.606886</td>
    </tr>
  </tbody>
</table>
</div>



## Grouping

By “group by” we are referring to a process involving one or more of the following steps

* **Splitting** the data into groups based on some criteria
* **Applying** a function to each group independently
* **Combining** the results into a data structure

See the [Grouping section](http://pandas.pydata.org/pandas-docs/stable/groupby.html#groupby)


```python
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                                    'B' : ['one', 'one', 'two', 'three','two', 'two', 'one', 'three'],
                                    'C' : np.random.randn(8),
                                     'D' : np.random.randn(8)})
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>foo</td>
      <td>one</td>
      <td>-0.197857</td>
      <td>0.836461</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bar</td>
      <td>one</td>
      <td>-1.836371</td>
      <td>-1.672314</td>
    </tr>
    <tr>
      <th>2</th>
      <td>foo</td>
      <td>two</td>
      <td>-0.805655</td>
      <td>-1.963117</td>
    </tr>
    <tr>
      <th>3</th>
      <td>bar</td>
      <td>three</td>
      <td>0.564109</td>
      <td>0.004886</td>
    </tr>
    <tr>
      <th>4</th>
      <td>foo</td>
      <td>two</td>
      <td>-0.588056</td>
      <td>0.420082</td>
    </tr>
    <tr>
      <th>5</th>
      <td>bar</td>
      <td>two</td>
      <td>0.188632</td>
      <td>0.220741</td>
    </tr>
    <tr>
      <th>6</th>
      <td>foo</td>
      <td>one</td>
      <td>0.327255</td>
      <td>-0.136870</td>
    </tr>
    <tr>
      <th>7</th>
      <td>foo</td>
      <td>three</td>
      <td>0.772913</td>
      <td>-1.430266</td>
    </tr>
  </tbody>
</table>
</div>



Grouping and then applying a function sum to the resulting groups.


```python
df.groupby('A').sum()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
      <th>D</th>
    </tr>
    <tr>
      <th>A</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <td>-1.083630</td>
      <td>-1.446687</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>-0.491399</td>
      <td>-2.273710</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby(['A','B']).sum()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>C</th>
      <th>D</th>
    </tr>
    <tr>
      <th>A</th>
      <th>B</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">bar</th>
      <th>one</th>
      <td>-1.836371</td>
      <td>-1.672314</td>
    </tr>
    <tr>
      <th>three</th>
      <td>0.564109</td>
      <td>0.004886</td>
    </tr>
    <tr>
      <th>two</th>
      <td>0.188632</td>
      <td>0.220741</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">foo</th>
      <th>one</th>
      <td>0.129399</td>
      <td>0.699591</td>
    </tr>
    <tr>
      <th>three</th>
      <td>0.772913</td>
      <td>-1.430266</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-1.393711</td>
      <td>-1.543035</td>
    </tr>
  </tbody>
</table>
</div>



## Reshaping

See the sections on [Hierarchical Indexing](http://pandas.pydata.org/pandas-docs/stable/advanced.html#advanced-hierarchical) and [Reshaping](http://pandas.pydata.org/pandas-docs/stable/reshaping.html#reshaping-stacking).

### Stack


```python
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                                ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))
```


```python
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
```


```python
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
```


```python
df2 = df[:4]
```


```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
    <tr>
      <th>first</th>
      <th>second</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">bar</th>
      <th>one</th>
      <td>-0.172437</td>
      <td>-0.112341</td>
    </tr>
    <tr>
      <th>two</th>
      <td>1.309232</td>
      <td>-1.193736</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">baz</th>
      <th>one</th>
      <td>-0.459612</td>
      <td>-1.163682</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-1.454387</td>
      <td>0.184935</td>
    </tr>
  </tbody>
</table>
</div>



The stack() method “compresses” a level in the DataFrame’s columns.


```python
stacked = df2.stack()
```


```python
stacked
```




    first  second   
    bar    one     A   -0.172437
                   B   -0.112341
           two     A    1.309232
                   B   -1.193736
    baz    one     A   -0.459612
                   B   -1.163682
           two     A   -1.454387
                   B    0.184935
    dtype: float64



With a “stacked” DataFrame or Series (having a MultiIndex as the index), the inverse operation of stack() is unstack(), which by default unstacks the **last level**:


```python
stacked.unstack()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
    <tr>
      <th>first</th>
      <th>second</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">bar</th>
      <th>one</th>
      <td>-0.172437</td>
      <td>-0.112341</td>
    </tr>
    <tr>
      <th>two</th>
      <td>1.309232</td>
      <td>-1.193736</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">baz</th>
      <th>one</th>
      <td>-0.459612</td>
      <td>-1.163682</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-1.454387</td>
      <td>0.184935</td>
    </tr>
  </tbody>
</table>
</div>




```python
stacked.unstack(1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>second</th>
      <th>one</th>
      <th>two</th>
    </tr>
    <tr>
      <th>first</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">bar</th>
      <th>A</th>
      <td>-0.172437</td>
      <td>1.309232</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-0.112341</td>
      <td>-1.193736</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">baz</th>
      <th>A</th>
      <td>-0.459612</td>
      <td>-1.454387</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-1.163682</td>
      <td>0.184935</td>
    </tr>
  </tbody>
</table>
</div>




```python
stacked.unstack(0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>first</th>
      <th>bar</th>
      <th>baz</th>
    </tr>
    <tr>
      <th>second</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">one</th>
      <th>A</th>
      <td>-0.172437</td>
      <td>-0.459612</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-0.112341</td>
      <td>-1.163682</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">two</th>
      <th>A</th>
      <td>1.309232</td>
      <td>-1.454387</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-1.193736</td>
      <td>0.184935</td>
    </tr>
  </tbody>
</table>
</div>



### Pivot Tables

See the section on [Pivot Tables](http://pandas.pydata.org/pandas-docs/stable/reshaping.html#reshaping-pivot).


```python
df = pd.DataFrame({'A' : ['one', 'one', 'two', 'three'] * 3,
                                    'B' : ['A', 'B', 'C'] * 4,
                                    'C' : ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                                    'D' : np.random.randn(12),
                                    'E' : np.random.randn(12)})
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>one</td>
      <td>A</td>
      <td>foo</td>
      <td>0.145715</td>
      <td>-1.022165</td>
    </tr>
    <tr>
      <th>1</th>
      <td>one</td>
      <td>B</td>
      <td>foo</td>
      <td>-0.281787</td>
      <td>0.478218</td>
    </tr>
    <tr>
      <th>2</th>
      <td>two</td>
      <td>C</td>
      <td>foo</td>
      <td>-0.302780</td>
      <td>-0.107945</td>
    </tr>
    <tr>
      <th>3</th>
      <td>three</td>
      <td>A</td>
      <td>bar</td>
      <td>-0.581474</td>
      <td>-0.024141</td>
    </tr>
    <tr>
      <th>4</th>
      <td>one</td>
      <td>B</td>
      <td>bar</td>
      <td>-0.647910</td>
      <td>-0.070459</td>
    </tr>
    <tr>
      <th>5</th>
      <td>one</td>
      <td>C</td>
      <td>bar</td>
      <td>-0.117996</td>
      <td>1.423829</td>
    </tr>
    <tr>
      <th>6</th>
      <td>two</td>
      <td>A</td>
      <td>foo</td>
      <td>1.048549</td>
      <td>-1.442322</td>
    </tr>
    <tr>
      <th>7</th>
      <td>three</td>
      <td>B</td>
      <td>foo</td>
      <td>0.303375</td>
      <td>-1.398654</td>
    </tr>
    <tr>
      <th>8</th>
      <td>one</td>
      <td>C</td>
      <td>foo</td>
      <td>0.291800</td>
      <td>-0.651896</td>
    </tr>
    <tr>
      <th>9</th>
      <td>one</td>
      <td>A</td>
      <td>bar</td>
      <td>0.491486</td>
      <td>-0.012319</td>
    </tr>
    <tr>
      <th>10</th>
      <td>two</td>
      <td>B</td>
      <td>bar</td>
      <td>-2.016146</td>
      <td>-0.884870</td>
    </tr>
    <tr>
      <th>11</th>
      <td>three</td>
      <td>C</td>
      <td>bar</td>
      <td>0.249340</td>
      <td>-0.056224</td>
    </tr>
  </tbody>
</table>
</div>



We can produce pivot tables from this data very easily:


```python
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
      <th>bar</th>
      <th>foo</th>
    </tr>
    <tr>
      <th>A</th>
      <th>B</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">one</th>
      <th>A</th>
      <td>0.491486</td>
      <td>0.145715</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-0.647910</td>
      <td>-0.281787</td>
    </tr>
    <tr>
      <th>C</th>
      <td>-0.117996</td>
      <td>0.291800</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">three</th>
      <th>A</th>
      <td>-0.581474</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>B</th>
      <td>NaN</td>
      <td>0.303375</td>
    </tr>
    <tr>
      <th>C</th>
      <td>0.249340</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">two</th>
      <th>A</th>
      <td>NaN</td>
      <td>1.048549</td>
    </tr>
    <tr>
      <th>B</th>
      <td>-2.016146</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>C</th>
      <td>NaN</td>
      <td>-0.302780</td>
    </tr>
  </tbody>
</table>
</div>



## Time Series

pandas has simple, powerful, and efficient functionality for performing resampling operations during frequency conversion (e.g., converting secondly data into 5-minutely data). This is extremely common in, but not limited to, financial applications. See the [Time Series section](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#timeseries)


```python
rng = pd.date_range('1/1/2012', periods=100, freq='S')
```


```python
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
```


```python
ts.resample('5Min').sum()
```




    2012-01-01    25406
    Freq: 5T, dtype: int64



Time zone representation


```python
rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
```


```python
ts = pd.Series(np.random.randn(len(rng)), rng)
```


```python
ts
```




    2012-03-06    2.403731
    2012-03-07    1.578758
    2012-03-08   -1.412283
    2012-03-09    1.585423
    2012-03-10   -0.447442
    Freq: D, dtype: float64




```python
ts_utc = ts.tz_localize('UTC')
```


```python
ts_utc
```




    2012-03-06 00:00:00+00:00    2.403731
    2012-03-07 00:00:00+00:00    1.578758
    2012-03-08 00:00:00+00:00   -1.412283
    2012-03-09 00:00:00+00:00    1.585423
    2012-03-10 00:00:00+00:00   -0.447442
    Freq: D, dtype: float64




Convert to another time zone


```python
ts_utc.tz_convert('US/Eastern')
```




    2012-03-05 19:00:00-05:00    2.403731
    2012-03-06 19:00:00-05:00    1.578758
    2012-03-07 19:00:00-05:00   -1.412283
    2012-03-08 19:00:00-05:00    1.585423
    2012-03-09 19:00:00-05:00   -0.447442
    Freq: D, dtype: float64




Converting between time span representations


```python
rng = pd.date_range('1/1/2012', periods=5, freq='M')
```


```python
ts = pd.Series(np.random.randn(len(rng)), index=rng)
```


```python
ts
```




    2012-01-31    0.415257
    2012-02-29   -0.843090
    2012-03-31    0.306608
    2012-04-30    0.861638
    2012-05-31    0.579553
    Freq: M, dtype: float64




```python
ps = ts.to_period()
```


```python
ps
```




    2012-01    0.415257
    2012-02   -0.843090
    2012-03    0.306608
    2012-04    0.861638
    2012-05    0.579553
    Freq: M, dtype: float64




```python
ps.to_timestamp()
```




    2012-01-01    0.415257
    2012-02-01   -0.843090
    2012-03-01    0.306608
    2012-04-01    0.861638
    2012-05-01    0.579553
    Freq: MS, dtype: float64



Converting between period and timestamp enables some convenient arithmetic functions to be used. In the following example, we convert a quarterly frequency with year ending in November to 9am of the end of the month following the quarter end:


```python
prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
```


```python
ts = pd.Series(np.random.randn(len(prng)), prng)
```


```python
ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
```


```python
ts.head()
```




    1990-03-01 09:00    2.540545
    1990-06-01 09:00   -1.301051
    1990-09-01 09:00    0.504866
    1990-12-01 09:00    3.159323
    1991-03-01 09:00   -0.520955
    Freq: H, dtype: float64



## Categoricals

pandas can include categorical data in a DataFrame. For full docs, see the categorical introduction and the API documentation.


```python
df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a', 'b', 'b', 'a', 'a', 'e']})
```

Convert the raw grades to a categorical data type.


```python
df["grade"] = df["raw_grade"].astype("category")
```


```python
df["grade"]
```




    0    a
    1    b
    2    b
    3    a
    4    a
    5    e
    Name: grade, dtype: category
    Categories (3, object): ['a', 'b', 'e']



Rename the categories to more meaningful names (assigning to Series.cat.categories is inplace!)


```python
df["grade"].cat.categories = ["very good", "good", "very bad"]
```

Reorder the categories and simultaneously add the missing categories (methods under Series .cat return a new Series per default).


```python
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
```


```python
df["grade"]
```




    0    very good
    1         good
    2         good
    3    very good
    4    very good
    5     very bad
    Name: grade, dtype: category
    Categories (5, object): ['very bad', 'bad', 'medium', 'good', 'very good']



Sorting is per order in the categories, not lexical order.


```python
df.sort_values(by="grade")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>raw_grade</th>
      <th>grade</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>e</td>
      <td>very bad</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>b</td>
      <td>good</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>b</td>
      <td>good</td>
    </tr>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>a</td>
      <td>very good</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>a</td>
      <td>very good</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>a</td>
      <td>very good</td>
    </tr>
  </tbody>
</table>
</div>



Grouping by a categorical column shows also empty categories.


```python
df.groupby("grade").size()
```




    grade
    very bad     1
    bad          0
    medium       0
    good         2
    very good    3
    dtype: int64



## Plotting
[Plotting](http://pandas.pydata.org/pandas-docs/stable/visualization.html#visualization) docs.


```python
import matplotlib.pyplot as plt
plt.close("all")
```


```python
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
```


```python
ts = ts.cumsum()
```


```python
ts.plot()
```




    <AxesSubplot:>




    
![png](05%20-%2010%20minutes%20to%20pandas_files/05%20-%2010%20minutes%20to%20pandas_220_1.png)
    


On DataFrame, plot() is a convenience to plot all of the columns with labels:


```python
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns=['A', 'B', 'C', 'D'])
```


```python
df = df.cumsum()
```


```python
plt.figure(); df.plot(); plt.legend(loc='best')
```




    <matplotlib.legend.Legend at 0x7fd7e8a55cd0>




    <Figure size 432x288 with 0 Axes>



    
![png](05%20-%2010%20minutes%20to%20pandas_files/05%20-%2010%20minutes%20to%20pandas_224_2.png)
    


## Getting Data In/Out

### CSV
[Writing to a csv file](http://pandas.pydata.org/pandas-docs/stable/io.html#io-store-in-csv)


```python
df.to_csv('foo.csv')
```

[Reading from a csv file](http://pandas.pydata.org/pandas-docs/stable/io.html#io-read-csv-table)


```python
pd.read_csv('foo.csv')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000-01-01</td>
      <td>0.384817</td>
      <td>0.513609</td>
      <td>-1.705235</td>
      <td>1.399450</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000-01-02</td>
      <td>-1.177765</td>
      <td>-0.886053</td>
      <td>-1.922768</td>
      <td>1.704903</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000-01-03</td>
      <td>-2.197236</td>
      <td>-0.092119</td>
      <td>-1.403218</td>
      <td>2.196858</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000-01-04</td>
      <td>-2.374139</td>
      <td>0.518876</td>
      <td>-2.551855</td>
      <td>1.828393</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000-01-05</td>
      <td>-3.560139</td>
      <td>2.067079</td>
      <td>-2.901068</td>
      <td>2.602319</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>995</th>
      <td>2002-09-22</td>
      <td>-37.367730</td>
      <td>35.506805</td>
      <td>7.181577</td>
      <td>29.633260</td>
    </tr>
    <tr>
      <th>996</th>
      <td>2002-09-23</td>
      <td>-37.688242</td>
      <td>36.428275</td>
      <td>7.138265</td>
      <td>29.185347</td>
    </tr>
    <tr>
      <th>997</th>
      <td>2002-09-24</td>
      <td>-37.739469</td>
      <td>37.258316</td>
      <td>7.570954</td>
      <td>29.158169</td>
    </tr>
    <tr>
      <th>998</th>
      <td>2002-09-25</td>
      <td>-38.741428</td>
      <td>38.066170</td>
      <td>6.919066</td>
      <td>30.099116</td>
    </tr>
    <tr>
      <th>999</th>
      <td>2002-09-26</td>
      <td>-40.062920</td>
      <td>37.444626</td>
      <td>7.426596</td>
      <td>29.419724</td>
    </tr>
  </tbody>
</table>
<p>1000 rows × 5 columns</p>
</div>



### HDF5
Reading and writing to [HDFStores](http://pandas.pydata.org/pandas-docs/stable/io.html#io-hdf5)

Writing to a HDF5 Store


```python
df.to_hdf('foo.h5','df')
```

Reading from a HDF5 Store


```python
pd.read_hdf('foo.h5','df')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.384817</td>
      <td>0.513609</td>
      <td>-1.705235</td>
      <td>1.399450</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>-1.177765</td>
      <td>-0.886053</td>
      <td>-1.922768</td>
      <td>1.704903</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>-2.197236</td>
      <td>-0.092119</td>
      <td>-1.403218</td>
      <td>2.196858</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>-2.374139</td>
      <td>0.518876</td>
      <td>-2.551855</td>
      <td>1.828393</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>-3.560139</td>
      <td>2.067079</td>
      <td>-2.901068</td>
      <td>2.602319</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2002-09-22</th>
      <td>-37.367730</td>
      <td>35.506805</td>
      <td>7.181577</td>
      <td>29.633260</td>
    </tr>
    <tr>
      <th>2002-09-23</th>
      <td>-37.688242</td>
      <td>36.428275</td>
      <td>7.138265</td>
      <td>29.185347</td>
    </tr>
    <tr>
      <th>2002-09-24</th>
      <td>-37.739469</td>
      <td>37.258316</td>
      <td>7.570954</td>
      <td>29.158169</td>
    </tr>
    <tr>
      <th>2002-09-25</th>
      <td>-38.741428</td>
      <td>38.066170</td>
      <td>6.919066</td>
      <td>30.099116</td>
    </tr>
    <tr>
      <th>2002-09-26</th>
      <td>-40.062920</td>
      <td>37.444626</td>
      <td>7.426596</td>
      <td>29.419724</td>
    </tr>
  </tbody>
</table>
<p>1000 rows × 4 columns</p>
</div>



### Excel

Reading and writing to [MS Excel](http://pandas.pydata.org/pandas-docs/stable/io.html#io-excel)

Writing to an excel file


```python
df.to_excel('foo.xlsx', sheet_name='Sheet1')
```

Reading from an excel file


```python
pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2000-01-01</td>
      <td>0.384817</td>
      <td>0.513609</td>
      <td>-1.705235</td>
      <td>1.399450</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2000-01-02</td>
      <td>-1.177765</td>
      <td>-0.886053</td>
      <td>-1.922768</td>
      <td>1.704903</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2000-01-03</td>
      <td>-2.197236</td>
      <td>-0.092119</td>
      <td>-1.403218</td>
      <td>2.196858</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2000-01-04</td>
      <td>-2.374139</td>
      <td>0.518876</td>
      <td>-2.551855</td>
      <td>1.828393</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2000-01-05</td>
      <td>-3.560139</td>
      <td>2.067079</td>
      <td>-2.901068</td>
      <td>2.602319</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>995</th>
      <td>2002-09-22</td>
      <td>-37.367730</td>
      <td>35.506805</td>
      <td>7.181577</td>
      <td>29.633260</td>
    </tr>
    <tr>
      <th>996</th>
      <td>2002-09-23</td>
      <td>-37.688242</td>
      <td>36.428275</td>
      <td>7.138265</td>
      <td>29.185347</td>
    </tr>
    <tr>
      <th>997</th>
      <td>2002-09-24</td>
      <td>-37.739469</td>
      <td>37.258316</td>
      <td>7.570954</td>
      <td>29.158169</td>
    </tr>
    <tr>
      <th>998</th>
      <td>2002-09-25</td>
      <td>-38.741428</td>
      <td>38.066170</td>
      <td>6.919066</td>
      <td>30.099116</td>
    </tr>
    <tr>
      <th>999</th>
      <td>2002-09-26</td>
      <td>-40.062920</td>
      <td>37.444626</td>
      <td>7.426596</td>
      <td>29.419724</td>
    </tr>
  </tbody>
</table>
<p>1000 rows × 5 columns</p>
</div>



### Gotchas
If you are trying an operation and you see an exception like:


```python
if pd.Series([False, True, False]):
    print("I was true")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    /var/folders/jd/pq0swyt521jb2424d6fvth840000gn/T/ipykernel_71440/2648304181.py in <module>
    ----> 1 if pd.Series([False, True, False]):
          2     print("I was true")


    ~/opt/miniconda3/envs/cmu39/lib/python3.9/site-packages/pandas/core/generic.py in __nonzero__(self)
       1535     @final
       1536     def __nonzero__(self):
    -> 1537         raise ValueError(
       1538             f"The truth value of a {type(self).__name__} is ambiguous. "
       1539             "Use a.empty, a.bool(), a.item(), a.any() or a.all()."


    ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().


See [Comparisons](http://pandas.pydata.org/pandas-docs/stable/basics.html#basics-compare) for an explanation and what to do.

See [Gotchas](http://pandas.pydata.org/pandas-docs/stable/gotchas.html#gotchas) as well.


```python

```
