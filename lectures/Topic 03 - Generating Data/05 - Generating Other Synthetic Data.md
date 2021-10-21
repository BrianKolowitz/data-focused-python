---
layout: default
title: 05 - Generating Other Synthetic Data
parent: Topic 03 - Generating Data
grand_parent: Lectures
nav_order: 5
---
# Generating Other Synthetic Data

[Source](https://towardsdatascience.com/synthetic-data-generation-a-must-have-skill-for-new-data-scientists-915896c0c1ae)

## What kind of data may be needed for a rich learning experience?

Imagine you are tinkering with a cool machine learning algorithm like SVM or a deep neural net. What kind of dataset you should practice them on? If you are learning from scratch, the advice is to start with simple, small-scale datasets which you can plot in two dimensions to understand the patterns visually and see for yourself the working of the ML algorithm in an intuitive fashion. For example, here is an [excellent article on various datasets you can try at various level of learning](https://www.analyticsvidhya.com/blog/2018/05/24-ultimate-data-science-projects-to-boost-your-knowledge-and-skills/).

## What is a synthetic dataset?

As the name suggests, quite obviously, a synthetic dataset is a repository of data that is generated programmatically. So, it is not collected by any real-life survey or experiment. Its main purpose, therefore, is to be flexible and rich enough to help an ML practitioner conduct fascinating experiments with various classification, regression, and clustering algorithms. Desired properties are,

* It can be numerical, binary, or categorical (ordinal or non-ordinal),
* The number of features and length of the dataset should be arbitrary
* It should preferably be random and the user should be able to choose a wide variety of statistical distribution to base this data upon i.e. the underlying random process can be precisely controlled and tuned,
* If it is used for classification algorithms, then the degree of class separation should be controllable to make the learning problem easy or hard,
* Random noise can be interjected in a controllable manner
* For a regression problem, a complex, non-linear generative process can be used for sourcing the data

## What about privacy concerns?

Although in this article, we keep our discussions limited to synthetic data for better ML algorithms, its purpose can be far reaching in cases where it helps get around security and privacy concerns with real datasets, that cannot be used or acquired for learning purpose. For example, think about medical or military data. [Here is an excellent summary article about such methods](https://www.ijstr.org/final-print/mar2017/A-Review-Of-Synthetic-Data-Generation-Methods-For-Privacy-Preserving-Data-Publishing.pdf).


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

## Regression problem generation

Regression problem generation: Scikit-learn’s ```dataset.make_regression``` function can create random regression problem with arbitrary number of input features, output targets, and controllable degree of informative coupling between them. It can also mix Gaussian noise.


```python
from sklearn.datasets import make_regression
```


```python
data1 = make_regression(n_samples=20, n_features=4, n_informative=2, n_targets=1, 
                        bias=0.0, effective_rank=None,tail_strength=0.5, 
                        noise=0.0, shuffle=True, coef=False, random_state=None)
df1 = pd.DataFrame(data1[0],columns=['x'+str(i) for i in range(1,5)])
df1['y'] = data1[1]
```


```python
df1.head()
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
      <th>x1</th>
      <th>x2</th>
      <th>x3</th>
      <th>x4</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.326839</td>
      <td>2.203741</td>
      <td>-0.152775</td>
      <td>-0.682349</td>
      <td>70.815411</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.584208</td>
      <td>0.097921</td>
      <td>-0.045379</td>
      <td>1.043689</td>
      <td>1.670565</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.100703</td>
      <td>-0.141215</td>
      <td>1.752348</td>
      <td>1.166683</td>
      <td>62.111800</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.308948</td>
      <td>1.741082</td>
      <td>1.159611</td>
      <td>-1.625781</td>
      <td>104.917778</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.320515</td>
      <td>2.320092</td>
      <td>1.882030</td>
      <td>-1.058409</td>
      <td>152.690260</td>
    </tr>
  </tbody>
</table>
</div>



### Plot


```python
plt.figure(figsize=(15,10))
for i in range(1,5):
    fit = np.polyfit(df1[df1.columns[i-1]],df1['y'],1)
    fit_fn = np.poly1d(fit)
    plt.subplot(2,2,i)
    plt.scatter(df1[df1.columns[i-1]],df1['y'],s=200,c='orange',edgecolor='k')
    plt.plot(df1[df1.columns[i-1]],fit_fn(df1[df1.columns[i-1]]),'b-',lw=3)
    plt.grid(True)
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_7_0.png)
    


### Data with Gaussian noise


```python
data2 = make_regression(n_samples=20, n_features=4, n_informative=2, n_targets=1, 
                        bias=0.0, effective_rank=None,tail_strength=0.5, 
                        noise=2.0, shuffle=True, coef=False, random_state=None)
df2 = pd.DataFrame(data2[0],columns=['x'+str(i) for i in range(1,5)])
df2['y'] = data2[1]
```

### Plot


```python
plt.figure(figsize=(15,10))
for i in range(1,5):
    fit = np.polyfit(df2[df2.columns[i-1]],df2['y'],1)
    fit_fn = np.poly1d(fit)
    plt.subplot(2,2,i)
    plt.scatter(df2[df2.columns[i-1]],df2['y'],s=200,c='orange',edgecolor='k')
    plt.plot(df2[df2.columns[i-1]],fit_fn(df2[df2.columns[i-1]]),'b-',lw=3)
    plt.grid(True)
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_11_0.png)
    


### Plot datasets with varying degree of noise


```python
plt.figure(figsize=(15,6))
df2 = pd.DataFrame(data=np.zeros((20,1)))
for i in range(3):
    data2 = make_regression(n_samples=20, n_features=1, n_informative=1, n_targets=1, 
                        bias=0.0, effective_rank=None,tail_strength=0.5, 
                        noise=i*10, shuffle=True, coef=False, random_state=None)
    df2['x'+str(i+1)]=data2[0]
    df2['y'+str(i+1)] = data2[1]

for i in range(3):
    fit = np.polyfit(df2['x'+str(i+1)],df2['y'+str(i+1)],1)
    fit_fn = np.poly1d(fit)
    plt.subplot(1,3,i+1)
    plt.scatter(df2['x'+str(i+1)],df2['y'+str(i+1)],s=200,c='orange',edgecolor='k')
    plt.plot(df2['x'+str(i+1)],fit_fn(df2['x'+str(i+1)]),'b-',lw=3)
    plt.grid(True)
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_13_0.png)
    


## Classification problem generation

Classification problem generation: Similar to the regression function above, ```dataset.make_classification``` generates a random multi-class classification problem (dataset) with controllable class separation and added noise. You can also randomly flip any percentage of output signs to create a harder classification dataset if you want.


```python
from sklearn.datasets import make_classification
```


```python
data3 = make_classification(n_samples=20, n_features=4, n_informative=4, n_redundant=0, n_repeated=0, 
                            n_classes=2, n_clusters_per_class=1, weights=None, flip_y=0.01, class_sep=1.0, 
                            hypercube=True, shift=0.0, scale=1.0, shuffle=True, random_state=None)
df3 = pd.DataFrame(data3[0],columns=['x'+str(i) for i in range(1,5)])
df3['y'] = data3[1]
```


```python
df3.head()
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
      <th>x1</th>
      <th>x2</th>
      <th>x3</th>
      <th>x4</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.937800</td>
      <td>0.620428</td>
      <td>1.710371</td>
      <td>-1.335103</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-1.843944</td>
      <td>1.498890</td>
      <td>-0.950427</td>
      <td>-0.315925</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.670669</td>
      <td>0.493982</td>
      <td>-0.687241</td>
      <td>-1.206348</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3.140552</td>
      <td>-2.195994</td>
      <td>1.571735</td>
      <td>-0.247905</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.602336</td>
      <td>-2.151781</td>
      <td>4.427198</td>
      <td>-4.207194</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### Plot


```python
from itertools import combinations
from math import ceil
lst_var=list(combinations(df3.columns[:-1],2))
len_var = len(lst_var)
plt.figure(figsize=(18,10))
for i in range(1,len_var+1):
    plt.subplot(2,ceil(len_var/2),i)
    var1 = lst_var[i-1][0]
    var2 = lst_var[i-1][1]
    plt.scatter(df3[var1],df3[var2],s=200,c=df3['y'],edgecolor='k')
    plt.xlabel(var1,fontsize=14)
    plt.ylabel(var2,fontsize=14)
    plt.grid(True)
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_19_0.png)
    


### Making class separation easy by tweaking `class_sep`


```python
data3 = make_classification(n_samples=20, n_features=4, n_informative=4, n_redundant=0, n_repeated=0, 
                            n_classes=2, n_clusters_per_class=1, weights=None, flip_y=0.01, class_sep=3.0, 
                            hypercube=True, shift=0.0, scale=1.0, shuffle=True, random_state=None)
df3 = pd.DataFrame(data3[0],columns=['x'+str(i) for i in range(1,5)])
df3['y'] = data3[1]
```


```python
from itertools import combinations
from math import ceil
lst_var=list(combinations(df3.columns[:-1],2))
len_var = len(lst_var)
plt.figure(figsize=(18,10))
for i in range(1,len_var+1):
    plt.subplot(2,ceil(len_var/2),i)
    var1 = lst_var[i-1][0]
    var2 = lst_var[i-1][1]
    plt.scatter(df3[var1],df3[var2],s=200,c=df3['y'],edgecolor='k')
    plt.xlabel(var1,fontsize=14)
    plt.ylabel(var2,fontsize=14)
    plt.grid(True)
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_22_0.png)
    


### Making class separation hard by tweaking `class_sep`


```python
data3 = make_classification(n_samples=20, n_features=4, n_informative=4, n_redundant=0, n_repeated=0, 
                            n_classes=2, n_clusters_per_class=1, weights=None, flip_y=0.01, class_sep=0.5, 
                            hypercube=True, shift=0.0, scale=1.0, shuffle=True, random_state=None)
df3 = pd.DataFrame(data3[0],columns=['x'+str(i) for i in range(1,5)])
df3['y'] = data3[1]
```


```python
from itertools import combinations
from math import ceil
lst_var=list(combinations(df3.columns[:-1],2))
len_var = len(lst_var)
plt.figure(figsize=(18,10))
for i in range(1,len_var+1):
    plt.subplot(2,ceil(len_var/2),i)
    var1 = lst_var[i-1][0]
    var2 = lst_var[i-1][1]
    plt.scatter(df3[var1],df3[var2],s=200,c=df3['y'],edgecolor='k')
    plt.xlabel(var1,fontsize=14)
    plt.ylabel(var2,fontsize=14)
    plt.grid(True)
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_25_0.png)
    


### Making data noisy by increasing `flip_y`


```python
plt.figure(figsize=(18,10))
for i in range(6):
    data3 = make_classification(n_samples=20, n_features=4, n_informative=4, n_redundant=0, n_repeated=0, 
                                n_classes=2, n_clusters_per_class=1, weights=None, flip_y=0.1*i, class_sep=1.0, 
                                hypercube=True, shift=0.0, scale=1.0, shuffle=False, random_state=101)
    df3 = pd.DataFrame(data3[0],columns=['x'+str(i) for i in range(1,5)])
    df3['y'] = data3[1]
    plt.subplot(2,3,i+1)
    plt.title(f"Plot for flip_y={round(0.1*i,2)}")
    plt.scatter(df3['x1'],df3['x2'],s=200,c=df3['y'],edgecolor='k')
    plt.xlabel('x1',fontsize=14)
    plt.ylabel('x2',fontsize=14)
    plt.grid(True)
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_27_0.png)
    


### Plot datasets with varying degree of class separation


```python
plt.figure(figsize=(18,5))
df2 = pd.DataFrame(data=np.zeros((20,1)))
for i in range(3):
    data2 = make_classification(n_samples=20, n_features=2, n_informative=2, n_redundant=0, n_repeated=0, 
                                n_classes=2, n_clusters_per_class=1, weights=None, flip_y=0, class_sep=i+0.5, 
                                hypercube=True, shift=0.0, scale=1.0, shuffle=False, random_state=101)
    df2['x'+str(i+1)+'1']=data2[0][:,0]
    df2['x'+str(i+1)+'2']=data2[0][:,1]
    df2['y'+str(i+1)] = data2[1]

for i in range(3):
    plt.subplot(1,3,i+1)
    plt.scatter(df2['x'+str(i+1)+'1'],df2['x'+str(i+1)+'2'],s=200,c=df2['y'+str(i+1)],edgecolor='k')
    plt.grid(True)
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_29_0.png)
    


## Clustering problem generation

Clustering problem generation: There are quite a few functions for generating interesting clusters. The most straightforward one is ```datasets.make_blobs```, which generates arbitrary number of clusters with controllable distance parameters.


```python
from sklearn.datasets import make_blobs
```


```python
data4 = make_blobs(n_samples=60, n_features=4, centers=3, cluster_std=1.0, 
                   center_box=(-5.0, 5.0), shuffle=True, random_state=None)
df4 = pd.DataFrame(data4[0],columns=['x'+str(i) for i in range(1,5)])
df4['y'] = data4[1]
```


```python
from itertools import combinations
from math import ceil
lst_var=list(combinations(df4.columns[:-1],2))
len_var = len(lst_var)
plt.figure(figsize=(18,10))
for i in range(1,len_var+1):
    plt.subplot(2,ceil(len_var/2),i)
    var1 = lst_var[i-1][0]
    var2 = lst_var[i-1][1]
    plt.scatter(df4[var1],df4[var2],s=200,c=df4['y'],edgecolor='k')
    plt.xlabel(var1,fontsize=14)
    plt.ylabel(var2,fontsize=14)
    plt.grid(True)
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_33_0.png)
    


### Making clusters compact and easily separable by tweaking `cluster_std`


```python
data4 = make_blobs(n_samples=60, n_features=4, centers=3, cluster_std=0.3, 
                   center_box=(-5.0, 5.0), shuffle=True, random_state=None)
df4 = pd.DataFrame(data4[0],columns=['x'+str(i) for i in range(1,5)])
df4['y'] = data4[1]
```


```python
from itertools import combinations
from math import ceil
lst_var=list(combinations(df4.columns[:-1],2))
len_var = len(lst_var)
plt.figure(figsize=(18,10))
for i in range(1,len_var+1):
    plt.subplot(2,ceil(len_var/2),i)
    var1 = lst_var[i-1][0]
    var2 = lst_var[i-1][1]
    plt.scatter(df4[var1],df4[var2],s=200,c=df4['y'],edgecolor='k')
    plt.xlabel(var1,fontsize=14)
    plt.ylabel(var2,fontsize=14)
    plt.grid(True)
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_36_0.png)
    


### Making clusters spread out and difficult to separate by tweaking `cluster_std`


```python
data4 = make_blobs(n_samples=60, n_features=4, centers=3, cluster_std=2.5, 
                   center_box=(-5.0, 5.0), shuffle=True, random_state=None)
df4 = pd.DataFrame(data4[0],columns=['x'+str(i) for i in range(1,5)])
df4['y'] = data4[1]
```


```python
from itertools import combinations
from math import ceil
lst_var=list(combinations(df4.columns[:-1],2))
len_var = len(lst_var)
plt.figure(figsize=(18,10))
for i in range(1,len_var+1):
    plt.subplot(2,ceil(len_var/2),i)
    var1 = lst_var[i-1][0]
    var2 = lst_var[i-1][1]
    plt.scatter(df4[var1],df4[var2],s=200,c=df4['y'],edgecolor='k')
    plt.xlabel(var1,fontsize=14)
    plt.ylabel(var2,fontsize=14)
    plt.grid(True)
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_39_0.png)
    


### Making anisotropically distributed clustering problem

Anisotropic cluster generation: With a simple transformation using matrix multiplication, you can generate clusters which is aligned along certain axis or anisotropically distributed.


```python
data5 = make_blobs(n_samples=50, n_features=2, centers=3,cluster_std=1.5)
```


```python
transformation = [[0.5, -0.5], [-0.4, 0.8]]
```


```python
data5_0=np.dot(data5[0],transformation)
df5 = pd.DataFrame(data5_0,columns=['x'+str(i) for i in range(1,3)])
df5['y'] = data5[1]
```


```python
plt.figure(figsize=(8,5))
plt.scatter(df5['x1'],df5['x2'],c=df5['y'],s=200,edgecolors='k')
plt.xlabel('x1',fontsize=14)
plt.ylabel('x2',fontsize=14)
plt.grid(True)
plt.show()
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_44_0.png)
    


### Making concentric circle clusters

Concentric ring cluster data generation: For testing affinity based clustering algorithm or Gaussian mixture models, it is useful to have clusters generated in a special shape. We can use ```datasets.make_circles``` function to accomplish that.


```python
from sklearn.datasets import make_circles
```


```python
data6 = make_circles(n_samples=50, shuffle=True, noise=None, random_state=None, factor=0.6)
df6 = pd.DataFrame(data6[0],columns=['x'+str(i) for i in range(1,3)])
df6['y'] = data6[1]
```


```python
plt.figure(figsize=(8,5))
plt.scatter(df6['x1'],df6['x2'],c=df6['y'],s=200,edgecolors='k')
plt.xlabel('x1',fontsize=14)
plt.ylabel('x2',fontsize=14)
plt.grid(True)
plt.show()
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_48_0.png)
    


### Introdue noise in the circle clusters


```python
data6 = make_circles(n_samples=50, shuffle=True, noise=0.15, random_state=None, factor=0.6)
df6 = pd.DataFrame(data6[0],columns=['x'+str(i) for i in range(1,3)])
df6['y'] = data6[1]
```


```python
plt.figure(figsize=(8,5))
plt.scatter(df6['x1'],df6['x2'],c=df6['y'],s=200,edgecolors='k')
plt.xlabel('x1',fontsize=14)
plt.ylabel('x2',fontsize=14)
plt.grid(True)
plt.show()
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_51_0.png)
    


### Make moon shape clusters

Moon-shaped cluster data generation: We can also generate moon-shaped cluster data for testing algorithms, with controllable noise using ```datasets.make_moons``` function.


```python
from sklearn.datasets import make_moons
```


```python
data7 = make_moons(n_samples=50, shuffle=True, noise=None, random_state=None)
df7 = pd.DataFrame(data7[0],columns=['x'+str(i) for i in range(1,3)])
df7['y'] = data7[1]
```


```python
plt.figure(figsize=(8,5))
plt.scatter(df7['x1'],df7['x2'],c=df7['y'],s=200,edgecolors='k')
plt.xlabel('x1',fontsize=14)
plt.ylabel('x2',fontsize=14)
plt.grid(True)
plt.show()
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_55_0.png)
    


### Introduce noise in the moon-shaped clusters


```python
data7 = make_moons(n_samples=50, shuffle=True, noise=0.1, random_state=None)
df7 = pd.DataFrame(data7[0],columns=['x'+str(i) for i in range(1,3)])
df7['y'] = data7[1]
```


```python
plt.figure(figsize=(8,5))
plt.scatter(df7['x1'],df7['x2'],c=df7['y'],s=200,edgecolors='k')
plt.xlabel('x1',fontsize=14)
plt.ylabel('x2',fontsize=14)
plt.grid(True)
plt.show()
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_58_0.png)
    


## Random regression/classification problem generation using symbolic function


```python
from Symbolic_regression_classification_generator import gen_regression_symbolic, gen_classification_symbolic
```

### Generate regression data with a symbolic expression of:
$$\frac{x_1^2}{2}-3x_2+20.\text{sin}(x_3)$$


```python
data8 = gen_regression_symbolic(m='((x1^2)/2-3*x2)+20*sin(x3)',n_samples=50,noise=0.01)
df8=pd.DataFrame(data8, columns=['x'+str(i) for i in range(1,4)]+['y'])
```


```python
df8.head()
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
      <th>x1</th>
      <th>x2</th>
      <th>x3</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-1.995143</td>
      <td>1.969439</td>
      <td>-6.585953</td>
      <td>-9.86940209041576</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.694431</td>
      <td>10.646075</td>
      <td>-9.944827</td>
      <td>0.416231121214657</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.824618</td>
      <td>-2.154371</td>
      <td>1.861316</td>
      <td>25.9776280245960</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-3.778498</td>
      <td>4.509513</td>
      <td>11.273044</td>
      <td>-25.6259760456950</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-1.664324</td>
      <td>3.435822</td>
      <td>-4.291008</td>
      <td>9.33521803074928</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize=(18,5))
for i in range(1,4):
    plt.subplot(1,3,i)
    plt.scatter(df8[df8.columns[i-1]],df8['y'],s=200,c='orange',edgecolor='k')
    plt.grid(True)
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_64_0.png)
    


### Generate regression data with a symbolic expression of:
$$x_1^2*sin(x_1)$$


```python
data8 = 0.1*gen_regression_symbolic(m='x1^2*sin(x1)',n_samples=200,noise=0.05)
df8=pd.DataFrame(data8, columns=['x'+str(i) for i in range(1,2)]+['y'])
```


```python
plt.figure(figsize=(8,5))
plt.scatter(df8['x1'],df8['y'],s=100,c='orange',edgecolor='k')
plt.grid(True)
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_67_0.png)
    


### Generate classification data with a symbolic expression of:
$$\frac{x_1^2}{3}-\frac{x_2^2}{15}$$


```python
data9 = gen_classification_symbolic(m='((x1^2)/3-(x2^2)/15)',n_samples=500,flip_y=0.01)
df9=pd.DataFrame(data9, columns=['x'+str(i) for i in range(1,3)]+['y'])
```


```python
df9.head()
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
      <th>x1</th>
      <th>x2</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.602170</td>
      <td>-6.029703</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3.255014</td>
      <td>0.452398</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.986863</td>
      <td>8.692522</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.936118</td>
      <td>3.508951</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4.838671</td>
      <td>4.002539</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize=(8,5))
plt.scatter(df9['x1'],df9['x2'],c=df9['y'],s=100,edgecolors='k')
plt.xlabel('x1',fontsize=14)
plt.ylabel('x2',fontsize=14)
plt.grid(True)
plt.show()
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_71_0.png)
    


### Generate classification data with a symbolic expression of:
$$x_1-3.\text{sin}\frac{x_2}{2}$$


```python
data9 = gen_classification_symbolic(m='x1-3*sin(x2/2)',n_samples=500,flip_y=0.01)
df9=pd.DataFrame(data9, columns=['x'+str(i) for i in range(1,3)]+['y'])
```


```python
plt.figure(figsize=(8,5))
plt.scatter(df9['x1'],df9['x2'],c=df9['y'],s=100,edgecolors='k')
plt.xlabel('x1',fontsize=14)
plt.ylabel('x2',fontsize=14)
plt.grid(True)
plt.show()
```


    
![png](05%20-%20Generating%20Other%20Synthetic%20Data_files/05%20-%20Generating%20Other%20Synthetic%20Data_74_0.png)
    


## Categorical data generation using “pydbgen” library

While many high-quality real-life datasets are available on the web for trying out cool machine learning techniques, from my personal experience, I found that the same is not true when it comes to learning SQL.

For data science expertise, having a basic familiarity of SQL is almost as important as knowing how to write code in Python or R. But access to a large enough database with real categorical data (such as name, age, credit card, SSN, address, birthday, etc.) is not nearly as common as access to toy datasets on Kaggle, specifically designed or curated for machine learning task.

Apart from the beginners in data science, [even seasoned software testers may find it useful to have a simple tool](https://www.riaktr.com/synthetic-data-become-major-competitive-advantage/) where with a few lines of code they can generate arbitrarily large data sets with random (fake) yet meaningful entries.

Enter pydbgen. [Read the docs here](http://pydbgen.readthedocs.io/en/latest/#).

It is a [lightweight, pure-python library](https://github.com/tirthajyoti/pydbgen) to generate random useful entries (e.g. name, address, credit card number, date, time, company name, job title, license plate number, etc.) and save them in either Pandas dataframe object, or as a SQLite table in a database file, or in a MS Excel file.

## Generate name, address, phone number, email etc. using `Faker` package

This is a package you need to install first with **`pip install faker`**.


```python
from faker import Faker
fake = Faker()
```

### Generate a fake name


```python
fake.name()
```




    'Valerie Lynch'



### Generate a license-plate (US style)


```python
fake.license_plate()
```




    '577-EQG'



### Generate a full data frame with random name, street address, SSN, email, date


```python
df = pd.DataFrame()
for i in range(20):
    data = {
        'name': fake.name(),
        'street_address': fake.street_address(),
        'city': fake.city(),
        'zip_code': fake.zipcode(),
        'ssn': fake.ssn(),
        'email': fake.email(),
        'date': fake.date()
    }
    df = df.append(data, True)
```


```python
df.head(5)
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
      <th>name</th>
      <th>street_address</th>
      <th>city</th>
      <th>zip_code</th>
      <th>ssn</th>
      <th>email</th>
      <th>date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Molly Cook</td>
      <td>5539 Gray Inlet Suite 416</td>
      <td>Whitestad</td>
      <td>23319</td>
      <td>524-03-0773</td>
      <td>anoble@example.com</td>
      <td>1987-03-17</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Katherine Jones</td>
      <td>070 Christina Wells Suite 498</td>
      <td>North Daniel</td>
      <td>04028</td>
      <td>586-43-5250</td>
      <td>esolis@example.net</td>
      <td>1984-05-21</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Julia Reese</td>
      <td>790 Teresa Cove Suite 479</td>
      <td>Espinozaton</td>
      <td>17207</td>
      <td>848-13-7165</td>
      <td>jhanson@example.org</td>
      <td>1974-11-02</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Christine Rogers</td>
      <td>0797 Gibson Cove Suite 290</td>
      <td>Silvachester</td>
      <td>52803</td>
      <td>406-94-4118</td>
      <td>williamschad@example.net</td>
      <td>1983-05-08</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Dennis Mccoy</td>
      <td>109 Michelle Rest</td>
      <td>Gomezville</td>
      <td>39863</td>
      <td>572-81-2883</td>
      <td>fosterjames@example.org</td>
      <td>1982-05-23</td>
    </tr>
  </tbody>
</table>
</div>




```python

```