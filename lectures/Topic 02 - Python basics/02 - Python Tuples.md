---
layout: default
title: 02 - Python Tuples
parent: Topic 02 - Python basics
grand_parent: Lectures
nav_order: 2
---
# Python Tuple
[Python Tuple](https://www.programiz.com/python-programming/tuple)

## What is tuple?

In Python programming, a tuple is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas in a list, elements can be changed.

### Advantages of Tuple over List

Since, tuples are quite similiar to lists, both of them are used in similar situations as well.

However, there are certain advantages of implementing a tuple over a list. Below listed are some of the main advantages:

* We generally use tuple for heterogeneous (different) datatypes and list for homogeneous (similar) datatypes.
* Since tuple are immutable, iterating through tuple is faster than with list. So there is a slight performance boost.
* Tuples that contain immutable elements can be used as key for a dictionary. With list, this is not possible.
* If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

### Creating a Tuple
A tuple is created by placing all the items (elements) inside a parentheses (), separated by comma. The parentheses are optional but is a good practice to write it.

A tuple can have any number of items and they may be of different types (integer, float, list, string etc.).


```python
# empty tuple
# Output: ()
my_tuple = ()
print(type(my_tuple), my_tuple)
```

    <class 'tuple'> ()



```python
# tuple having integers
# Output: (1, 2, 3)
my_tuple = (1, 2, 3)
print(my_tuple)
```

    (1, 2, 3)



```python
# tuple with mixed datatypes
# Output: (1, "Hello", 3.4)
my_tuple = (1, "Hello", 3.4)
print(my_tuple)
```

    (1, 'Hello', 3.4)



```python
# nested tuple
# Output: ("mouse", [8, 4, 6], (1, 2, 3))
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)
```

    ('mouse', [8, 4, 6], (1, 2, 3))



```python
# tuple can be created without parentheses
# also called tuple packing
# Output: 3, 4.6, "dog"

my_tuple = 3, 4.6, "dog"
print(my_tuple)
```

    (3, 4.6, 'dog')


**Creating a tuple with one element is a bit tricky.**

Having one element within parentheses is not enough. We will need a trailing comma to indicate that it is in fact a tuple.


```python
# only parentheses is not enough
# Output: <class 'str'>
my_tuple = ("hello")

print(type(my_tuple))
```

    <class 'str'>



```python
# need a comma at the end
# Output: <class 'tuple'>
my_tuple = ("hello") 

print(type(my_tuple), my_tuple)
```

    <class 'str'> hello



```python
# what if i forget a comma
# Output: <class 'tuple'>
my_tuple = ("hello" "bye") 

print(type(my_tuple), my_tuple)
```

    <class 'str'> hellobye



```python
# parentheses is optional
# Output: <class 'tuple'>
my_tuple = "hello",

print(type(my_tuple))
```

    <class 'tuple'>


## Accessing Elements in a Tuple

### Indexing


```python
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(n_tuple[1][2])
```

    6



```python
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(type(n_tuple[0][2]), n_tuple[0][2])
```

    <class 'str'> u


### Negative indexing


```python
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(n_tuple[-1][-3], ' is the same as ', n_tuple[2][0])
```

    1  is the same as  1



```python
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(n_tuple[0][0], ' is the same as ', n_tuple[-3][-5])
```

    m  is the same as  m



```python
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(n_tuple[-1][1])
```

    2


### Slicing


```python
letter_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
```


```python
# prints items at position 0, 1, and 2 but not 3
print(letter_tuple[0:3])
```

    ('a', 'b', 'c')



```python
# prints items at position 3, 4, and 5 but not 6
print(letter_tuple[3:6])
```

    ('d', 'e', 'f')



```python
# start at the beginning
print(letter_tuple[:6])
```

    ('a', 'b', 'c', 'd', 'e', 'f')



```python
# go until the end
print(letter_tuple[3:])
```

    ('d', 'e', 'f', 'g', 'h', 'i', 'j')


### stepping over a tuple (or list)


```python
# every element
print(letter_tuple[0:10:1])
```

    ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')



```python
# every 3rd element
print(letter_tuple[0:10:3])
```

    ('a', 'd', 'g', 'j')



```python
# elements at even positions
print(letter_tuple[0::2])
```

    ('a', 'c', 'e', 'g', 'i')



```python
# elements at odd positions
print(letter_tuple[1::2])
```

    ('b', 'd', 'f', 'h', 'j')


### reversing a tuple (or list)


```python
print(letter_tuple[len(letter_tuple)::-1])
```

    ('j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a')



```python
print(letter_tuple[len(letter_tuple)::-2])
```

    ('j', 'h', 'f', 'd', 'b')


## Changing a Tuple

Unlike lists, tuples are immutable.

This means that elements of a tuple cannot be changed once it has been assigned. 


```python
x_tuple = (4, 2, 3, [6, 5])

x_tuple[1] = 8 # throws an error
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /var/folders/jd/pq0swyt521jb2424d6fvth840000gn/T/ipykernel_91254/2014519070.py in <module>
          1 x_tuple = (4, 2, 3, [6, 5])
          2 
    ----> 3 x_tuple[1] = 8 # throws an error
    

    TypeError: 'tuple' object does not support item assignment


But, if the element is itself a mutable datatype like list, its nested items can be changed.


```python
x_tuple[3][0] = 9 # but item of mutable element can be changed
print(x_tuple)
```

    (4, 2, 3, [9, 5])


## Deleting a Tuple

We cannot change the elements in a tuple. That also means we cannot delete or remove items from a tuple. But deleting a tuple entirely is possible using the keyword ```del```.


```python
a_tuple = (1, 2, 3)
print(a_tuple)
```

    (1, 2, 3)



```python
del a_tuple
print(a_tuple)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    /var/folders/jd/pq0swyt521jb2424d6fvth840000gn/T/ipykernel_91254/1119046425.py in <module>
          1 del a_tuple
    ----> 2 print(a_tuple)
    

    NameError: name 'a_tuple' is not defined


## Other Tuple Methods

* ```count(x)``` - Return the number of items that is equal to x
* ```index(x)``` - Return index of first item that is equal to x


```python
my_tuple = ('r', 'e', 'd', '', 'a', 'p', 'p', 'l', 'e',)
```


```python
print(my_tuple.count('p'))
```

    2



```python
print(my_tuple.index('p'))
```

    5



```python

```
