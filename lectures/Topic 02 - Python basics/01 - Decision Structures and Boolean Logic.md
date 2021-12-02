---
layout: default
title: 01 - Decision Structures and Boolean Logic
parent: Topic 02 - Python basics
grand_parent: Lectures
nav_order: 1
---
```python
if condition:
    # statement
    # statement
```

# if statement
if 2 > 1:
    print("2 is greater than 1")


```python
# boolean expressions
1 > 2
```




    False




```python
'a' > 'b'
```




    False




```python
'a' > 'A'
```




    True




```python
chr(65)
```




    'A'




```python
ord('A')
```




    65




```python
ord('a')
```




    97




```python
balance = 119
payment = 20
```


```python
balance == 0
```




    False




```python
payment != balance
```




    True




```python
if payment == balance:
    print('paid in full')
else:
    print('you owe ' + str(balance - payment))
```

    you owe 99



```python

```
