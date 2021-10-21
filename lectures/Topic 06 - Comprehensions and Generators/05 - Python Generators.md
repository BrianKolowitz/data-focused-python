---
layout: default
title: 05 - Python Generators
parent: Topic 06 - Comprehensions and Generators
grand_parent: Lectures
nav_order: 5
---
# Python Generators
[Source](https://realpython.com/introduction-to-python-generators/)

todo : add content


```python
def infinite_sequence():
    num = 0
    while True:
        num += 1
    return num
```


```python
x = infinite_sequence()
print(x)
```


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    /var/folders/jd/pq0swyt521jb2424d6fvth840000gn/T/ipykernel_93378/1323376258.py in <module>
    ----> 1 x = infinite_sequence()
          2 print(x)


    /var/folders/jd/pq0swyt521jb2424d6fvth840000gn/T/ipykernel_93378/3775151451.py in infinite_sequence()
          2     num = 0
          3     while True:
    ----> 4         num += 1
          5     return num


    KeyboardInterrupt: 



```python
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
```


```python
seq = infinite_sequence()
print(next(seq))
for i in range(0, 10):
    print(next(seq))
```


```python
for index, value in enumerate(seq):
    print(value)
    if index > 10:
        break
```


```python
print(next(seq))
```


```python
import random
def my_sequence():
    num = 0
    while True:
        yield num
        num += random.randint(0, 10)
        if num > 20:
            break
```


```python
seq = my_sequence()
print(next(seq))
```


```python
print(next(seq))
```


```python
print(next(seq))
```


```python
print(next(seq))
```

    12



```python
print(next(seq))
```

    14



```python
print(next(seq))
```

    20



```python
print(next(seq))
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-20-d9775cae3656> in <module>
    ----> 1 print(next(seq))
    

    StopIteration: 



```python
seq2 = my_sequence()
print(next(seq2))
```

    0



```python
image_db = [ 1, 2, 5, 7, 10]
meds_db = [ 3, 5, 7, 9 ]

i = get_next_image_patient()
m = get_next_med_patient()

def get_next_patient()
    while no_match:
        if i == m:
            yield i
        elif i > m:
            i = get_next_image_patient()
        elif m < i:
            m = get_next_med_patient()
            
for patient in get_next_patient():
    # do something
```
