---
layout: default
title: 03 - Pandas Introduction
parent: Week 05 - Data Processing and Visualization Part 2
grand_parent: Lectures
nav_order: 4
---

# Pandas Tutorial: DataFrames in Python
[Source](https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python)

Explore data analysis with Python. Pandas DataFrames make manipulating your data easy, from selecting or replacing columns and indices to reshaping your data.
Pandas is a popular Python package for data science, and with good reason: it offers powerful, expressive and flexible data structures that make data manipulation and analysis easy, among many other things. The DataFrame is one of these structures.

This tutorial covers Pandas DataFrames, from basic manipulations to advanced operations, by tackling 11 of the most popular questions so that you understand -and avoid- the doubts of the Pythonistas who have gone before you.

Content
1. How To Create a Pandas DataFrame
2. How To Select an Index or Column From a DataFrame
3. How To Add an Index, Row or Column to a DataFrame
4. How To Delete Indices, Rows or Columns From a DataFrame
5. How To Rename the Columns or Indices of a DataFrame
6. How To Format the Data in Your DataFrame
7. How To Create an Empty DataFrame
8. Does Pandas Recognize Dates When Importing Data?
9. When, Why and How You Should Reshape Your DataFrame
10. How To Iterate Over a DataFrame
11. How To Write a DataFrame to a File

## What Are Pandas Data Frames?

Before you start, let’s have a brief recap of what DataFrames are.

Those who are familiar with R know the data frame as a way to store data in rectangular grids that can easily be overviewed. Each row of these grids corresponds to measurements or values of an instance, while each column is a vector containing data for a specific variable. This means that a data frame’s rows do not need to contain, but can contain, the same type of values: they can be numeric, character, logical, etc.

Now, ```DataFrames``` in Python are very similar: they come with the **Pandas** library, and they are defined as a two-dimensional labeled data structures with columns of potentially different types.

In general, you could say that the Pandas DataFrame consists of three main components: the data, the index, and the columns.

Firstly, the ```DataFrame``` can contain data that is:
* a Pandas ```DataFrame```
* a Pandas ```Series```: a one-dimensional labeled array capable of holding any data type with axis labels or index. An example of a ```Series``` object is one column from a ```DataFrame```.
* a NumPy ```ndarray```, which can be a record or structured
* a two-dimensional ```ndarray```
* dictionaries of one-dimensional ```ndarray```’s, ```list```'s, ```dictionarie```'s or ```Series```.

Note the difference between ```np.ndarray``` and ```np.array()```. The former is an actual **data type**, while the latter is a **function** to make arrays from other data structures.

Structured arrays allow users to manipulate the data by named fields: in the example below, a structured array of three tuples is created. 

The first element of each tuple will be called ```foo``` and will be of type ```int```, while the second element will be named ```bar``` and will be a ```float```.


```python
import numpy as np
import pandas as pd
```


```python
# A structured array
my_array = np.ones(3, dtype=([('foo', int), ('bar', float)]))

# Print the structured array
print(type(my_array['foo']), my_array['foo'])
```

    <class 'numpy.ndarray'> [1 1 1]


**Record arrays**, on the other hand, expand the properties of structured arrays. They allow users to access fields of structured arrays by attribute rather than by index. You see below that the ```foo``` values are accessed in the ```r2``` record array.


```python
# A record array
my_array2 = my_array.view(np.recarray)

# Print the record array
print(type(my_array2.foo), my_array2.foo)
```

    <class 'numpy.ndarray'> [1 1 1]


Besides data, you can also specify the index and column names for your ```DataFrame```. The index, on the one hand, indicates the difference in rows, while the column names indicate the difference in columns. You will see later that these two components of the DataFrame will come in handy when you’re manipulating your data.

*Note that in this post, most of the times, the libraries that you need have already been loaded in. The Pandas library is usually imported under the alias ```pd```, while the NumPy library is loaded as ```np```. Remember that when you code in your own data science environment, you shouldn’t forget this import step, which you write just like this:*

```python
import numpy as np
import pandas as pd
```

## 1. How To Create a Pandas DataFrame

Obviously, making your DataFrames is your first step in almost anything that you want to do when it comes to data munging in Python. Sometimes, you will want to start from scratch, but you can also convert other data structures, such as lists or NumPy arrays, to Pandas DataFrames. In this section, you’ll will only cover the latter. 

Among the many things that can serve as input to make a ```DataFrame```, a NumPy ndarray is one of them. To make a data frame from a NumPy array, you can just pass it to the ```DataFrame()``` function in the data argument.


```python
columns = ['Col1', 'Col2']
index = ['Row1', 'Row2']
data = [[1, 2], [3, 4]]
                
df = pd.DataFrame(data=data,
                  index=index,
                  columns=columns)

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
      <th>Col1</th>
      <th>Col2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Row1</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Row2</th>
      <td>3</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
data = np.array([['','Col1','Col2'],
                ['Row1',1,2],
                ['Row2',3,4]])
                
df = pd.DataFrame(data=data[1:,1:],
                  index=data[1:,0],
                  columns=data[0,1:])

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
      <th>Col1</th>
      <th>Col2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Row1</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Row2</th>
      <td>3</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



Pay attention to how the code chunks above select elements from the NumPy array to construct the DataFrame: 
* you first select the values that are contained in the lists that start with Row1 and Row2 
* then you select the index or row numbers Row1 and Row2 and then the column names Col1 and Col2

Next, you also see that, in the chunk above, you printed out a small selection of the data. This works the same as subsetting 2D NumPy arrays: you first indicate the row that you want to look in for your data, then the column. 

Don’t forget that the indices start at **0**! For data in the example above, you go and look in the rows at index 1 to end and you select all elements that come after index 1. As a result, you end up selecting 1, 2, 3 and 4.

This approach to making DataFrames will be the same for all the structures that ```DataFrame()``` can take on as input.


```python
# Take a 2D array as input to your DataFrame 
my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print(my_2darray)
```

    [[1 2 3]
     [4 5 6]]



```python
# Take a dictionary as input to your DataFrame 
my_dict = {
    1: ['1', '3'], 
    2: ['1', '2'], 
    3: ['2', '4']}
my_df = pd.DataFrame(my_dict)
my_df
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
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>2</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Take a DataFrame as input to your DataFrame 
my_df = pd.DataFrame(
    data=[4,5,6,7], 
    index=range(0,4), 
    columns=['A'])
my_df
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Take a Series as input to your DataFrame
my_series = pd.Series({
    "Belgium":"Brussels", 
    "India":"New Delhi", 
    "United Kingdom":"London",
    "United States":"Washington"})

my_series
```




    Belgium             Brussels
    India              New Delhi
    United Kingdom        London
    United States     Washington
    dtype: object



Note that the index of your Series (and DataFrame) contains the keys of the original dictionary, but that they are sorted: Belgium will be the index at 0, while United States will be the index at 3.

After you have created your DataFrame, you might want to know a little bit more about it. You can use the shape property or the ```len()``` function in combination with the ```.index``` property:


```python
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]))

# Use the `shape` property
print(df.shape)
```

    (2, 3)



```python
# Or use the `len()` function with the `index` property
print(len(df.index))
```

    2


These two options give you slightly different information on your DataFrame: 
* the ```shape``` property will give you the dimensions of your DataFrame. That means that you will get to know the width and the height of your DataFrame. 
* the ```len()``` function, in combination with the index property, will only give you information on the height of your DataFrame.

This all is totally not extraordinary, though, as you explicitly give in the index property.

You could also use ```df[0].count()``` to get to know more about the height of your DataFrame, but this will exclude the NaN values (if there are any). That is why calling ```.count()`` on your DataFrame is not always the better option.

If you want more information on your DataFrame columns, you can always execute ```list(df.columns.values)```.


```python
list(df.columns.values)
```




    [0, 1, 2]



## 2. How To Select an Index or Column From a Pandas DataFrame

Before you start with adding, deleting and renaming the components of your DataFrame, you first need to know how you can select these elements. So, how do you do this?

Even though you might still remember how to do it from the previous section: selecting an index, column or value from your DataFrame isn’t that hard, quite the contrary. 

It’s similar to what you see in other languages (or packages!) that are used for data analysis. If you aren’t convinced, consider the following: In R, you use the [,] notation to access the data frame’s values.

Now, let’s say you have a DataFrame like this one


```python
def create_df():
    vals = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    d = { k:v for (k, v) in zip('ABC', vals)}
    df = pd.DataFrame(d)
    return df
```


```python
df = create_df()
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



And you want to access the value that is at index 0, in column ‘A’.

There are various options that exist to get your value 1 back:


```python
# Using `iloc[]`
print(df.iloc[0][0])

# Using `loc[]`
print(df.loc[0]['A'])

# Using `at[]`
print(df.at[0,'A'])

# Using `iat[]`
print(df.iat[0,0])
```

    1
    1
    1
    1


The **most important** ones to remember are, without a doubt, ```.loc[]``` and ```.iloc[]```. The subtle differences between these two will be discussed in the next sections.

Enough for now about selecting values from your DataFrame. What about selecting rows and columns? In that case, you would use:


```python
# Use `iloc[]` to select row `0`
print(df.iloc[0])
```

    A    1
    B    2
    C    3
    Name: 0, dtype: int64



```python
# Use `loc[]` to select column `'A'`
print(df.loc[:,'A'])
```

    0    1
    1    4
    2    7
    Name: A, dtype: int64


For now, it’s enough to know that you can either access the values by calling them by their label or by their position in the index or column. If you don’t see this, look again at the slight differences in the commands: one time, you see ```[0][0]```, the other time, you see ```[0,'A']``` to retrieve your value 1.

## 3. How To Add an Index, Row or Column to a Pandas DataFrame

Now that you have learned how to select a value from a DataFrame, it’s time to get to the real work and add an index, row or column to it!

Adding an Index to a DataFrame
When you create a DataFrame, you have the option to add input to the ```index``` argument to make sure that you have the index that you desire. When you don’t specify this, your DataFrame will have, by default, a numerically valued index that starts with 0 and continues until the last row of your DataFrame.

However, even when your index is specified for you automatically, you still have the power to re-use one of your columns and make it your index. You can easily do this by calling ```set_index()``` on your DataFrame.


```python
# Print out your DataFrame `df` to check it out
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Set 'C' as the index of your DataFrame
df.set_index('C')
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
    <tr>
      <th>C</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>9</th>
      <td>7</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



Adding Rows to a DataFrame
Before you can get to the solution, it’s first a good idea to grasp the concept of loc and how it differs from other indexing attributes such as ```.iloc[]``` and ```.ix[]```:

* ```.loc[]``` works on labels of your index. This means that if you give in ```loc[2]```, you look for the values of your DataFrame that have an index labeled 2.
* ```.iloc[]``` works on the positions in your index. This means that if you give in ```iloc[2]```, you look for the values of your DataFrame that are at index ’2`.
* ```.ix[]``` is a more complex case: when the index is integer-based, you pass a label to ```.ix[]``` ```.ix[2]``` then means that you’re looking in your DataFrame for values that have an index labeled 2. This is just like ```.loc[]```! However, if your index is not solely integer-based, ```ix``` will work with positions, just like ```.iloc[]```.

This all might seem very complicated. Let’s illustrate all of this with a small example:


```python
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 
                  index=[2, 'A', 4], 
                  columns=[48, 49, 50])
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
      <th>48</th>
      <th>49</th>
      <th>50</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>A</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Pass `2` to `loc`
df.loc[2]
```




    48    1
    49    2
    50    3
    Name: 2, dtype: int64




```python
# Pass `2` to `iloc`
print(df.iloc[2])
```

    48    7
    49    8
    50    9
    Name: 4, dtype: int64



```python
# Pass `2` to `ix`
print(df.ix[2])
```

    48    7
    49    8
    50    9
    Name: 4, dtype: int64


    /Users/kolobj/anaconda/envs/cmu3/lib/python3.6/site-packages/ipykernel_launcher.py:2: DeprecationWarning: 
    .ix is deprecated. Please use
    .loc for label based indexing or
    .iloc for positional indexing
    
    See the documentation here:
    http://pandas.pydata.org/pandas-docs/stable/indexing.html#ix-indexer-is-deprecated
      


Note that in this case you used an example of a DataFrame that is not solely integer-based as to make it easier for you to understand the differences. You clearly see that passing 2 to ```.loc[]``` or ```.iloc[]```/```.ix[]``` does not give back the same result!

* You know that ```.loc[]``` will go and look at the values that are at label 2. The result that you get back, will be
```
48    1
49    2
50    3
```
* You also know that ```.iloc[]``` will go and look at the positions in the index. When you pass 2, you will get back:
```
48    7
49    8
50    9
```
* Since the index doesn’t only contain integers, ```.ix[]``` will have the same behavior as iloc and look at the positions in the index. You will get back the same result as ```.iloc[]```.

Now that the difference between ```.iloc[]```, ```.loc[]``` and ```.ix[]``` is clear, you are ready to give adding rows to your DataFrame a go!

*Tip: as a consequence of what you have just read, you understand now also that the general recommendation is that you use ```.loc``` to insert rows in your DataFrame. That is because if you would use ```df.ix[]```, you might try to reference a numerically valued index with the index value and accidentally overwrite an existing row of your DataFrame. You better avoid this!*

Check out the difference once more in the DataFrame below:


```python
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 
                  index= [2.5, 12.6, 4.8], 
                  columns=[48, 49, 50])
```


```python
# There's no index labeled `2`, so you will change the index at position `2`
df.ix[2] = [60, 50, 40]
print(df)
```

          48  49  50
    2.5    1   2   3
    12.6   4   5   6
    4.8   60  50  40


    /Users/kolobj/anaconda/envs/cmu3/lib/python3.6/site-packages/ipykernel_launcher.py:2: DeprecationWarning: 
    .ix is deprecated. Please use
    .loc for label based indexing or
    .iloc for positional indexing
    
    See the documentation here:
    http://pandas.pydata.org/pandas-docs/stable/indexing.html#ix-indexer-is-deprecated
      



```python
# This will make an index labeled `2` and add the new values
df.loc[2] = [11, 12, 13]
print(df)
```

          48  49  50
    2.5    1   2   3
    12.6   4   5   6
    4.8   60  50  40
    2.0   11  12  13


### Adding a Column to Your DataFrame

In some cases, you want to make your index part of your DataFrame. You can easily do this by taking a column from your DataFrame or by referring to a column that you haven’t made yet and assigning it to the ```.index``` property, just like this:


```python
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 
                  columns=['A', 'B', 'C'])
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Use `.index`
df['D'] = df.index

# Print `df`
print(df)
```

       A  B  C  D
    0  1  2  3  0
    1  4  5  6  1
    2  7  8  9  2


In other words, you tell your DataFrame that it should take column A as its index.

However, if you want to append columns to your DataFrame, you could also follow the same approach as when you would add an index to your DataFrame: you use ```.loc[]``` or .```iloc[]```. 

In this case, you add a Series to an existing DataFrame with the help of ```.loc[]```:


```python
# Study the DataFrame `df`
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
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Append a column to `df`
df.loc[:, 'E'] = pd.Series(['5', '6', '7'], index=df.index)

# Print out `df` again to see the changes
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
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>1</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>2</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>



Remember a Series object is much like a column of a DataFrame; That explains why you can easily add a Series to an existing DataFrame. 

*Note also that the observation that was made earlier about ```.loc[]``` still stays valid, also when you’re adding columns to your DataFrame!*

### Resetting the Index of Your DataFrame

When your index doesn’t look entirely the way you want it to, you can opt to reset it. You can easily do this with .reset_index(). However, you should still watch out, as you can pass several arguments that can make or break the success of your reset:


```python
# Check out the weird index of your dataframe
df = df.set_index('C')
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
      <th>D</th>
      <th>E</th>
    </tr>
    <tr>
      <th>C</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>4</td>
      <td>5</td>
      <td>1</td>
      <td>6</td>
    </tr>
    <tr>
      <th>9</th>
      <td>7</td>
      <td>8</td>
      <td>2</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Use `reset_index()` to reset the values. 
df = df.reset_index(level=0, drop=True)
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
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>1</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>2</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>



## 4. How to Delete Indices, Rows or Columns From a Pandas Data Frame

Now that you have seen how to select and add indices, rows, and columns to your DataFrame, it’s time to consider another use case: removing these three from your data structure.

### Deleting an Index from Your DataFrame

If you want to remove the index from your DataFrame, you should reconsider because DataFrames and Series always have an index.

However, what you *can* do is, for example:

* resetting the index of your DataFrame (go back to the previous section to see how it is done)
* remove the index name, if there is any, by executing ```del df.index.name```
* remove duplicate index values by resetting the index, dropping the duplicates of the index column that has been added to your DataFrame and reinstating that duplicateless column again as the index:


```python
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [40, 50, 60], [23, 35, 37]]), 
                  index= [2.5, 12.6, 4.8, 4.8, 2.5], 
                  columns=[48, 49, 50])
                  
print(df)
```

          48  49  50
    2.5    1   2   3
    12.6   4   5   6
    4.8    7   8   9
    4.8   40  50  60
    2.5   23  35  37



```python
x = df.reset_index().drop_duplicates(subset='index', keep='last').set_index('index')
print(x)
```

           48  49  50
    index            
    12.6    4   5   6
    4.8    40  50  60
    2.5    23  35  37


### Deleting a Column from Your DataFrame

To get rid of (a selection of) columns from your DataFrame, you can use the drop() method:


```python
# Check out the DataFrame `df`
df = create_df()
print(df)
```

       A  B  C
    0  1  2  3
    1  4  5  6
    2  7  8  9



```python
# Drop the column with label 'A'                  
df.drop('A', axis=1, inplace=True)
print(df)
```

       B  C
    0  2  3
    1  5  6
    2  8  9



```python
# Drop the column at position 1
df.drop(df.columns[[1]], axis=1)
print(df)
```

       B  C
    0  2  3
    1  5  6
    2  8  9


You might think now: well, this is not so straightforward; There are some extra arguments that are passed to the ```drop()``` method!

* The axis argument is either 0 when it indicates rows and 1 when it is used to drop columns.
* You can set inplace to ```True``` to delete the column without having to reassign the DataFrame.

### Removing a Row from Your DataFrame
You can remove duplicate rows from your DataFrame by executing ```df.drop_duplicates()```. You can also remove rows from your DataFrame, taking into account only the duplicate values that exist in one column.


```python
# Check out your DataFrame `df`
df = create_df()
df = df.append({ 'A': 1, 'B': 2, 'C': 3}, ignore_index=True)
print(df)
```

       A  B  C
    0  1  2  3
    1  4  5  6
    2  7  8  9
    3  1  2  3



```python
# Drop the duplicates in `df`
x = df.drop_duplicates(subset='A', keep='last')
print(x)
```

       A  B  C
    1  4  5  6
    2  7  8  9
    3  1  2  3

