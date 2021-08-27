---
layout: default
title: 02 - Lists and List Comprehensions
parent: Week 03 - Functions, Loops, Comprehensions and Generators
grand_parent: Lectures
nav_order: 4
---
# Python List Comprehensions
[Python List Comprehension Tutorial](https://www.datacamp.com/community/tutorials/python-list-comprehension)

When doing data science, you might find yourself wanting to read lists of lists, filtering column names, removing vowels from a list or flattening a matrix. You can easily use a lambda function or a for loop; As you well know, there are multiple ways to go about this. One other way to do this is by using list comprehensions.

## Python List Comprehension

List comprehensions are used to create lists programatically. List comprehensions in Python are constructed as follows:

```python
list_variable = [x for x in iterable]
```

### List Comprehension in Python: The Mathematics

Remember in maths, the common ways to describe lists (or sets, or tuples, or vectors) are:

```latex
S = {x² : x in {0 ... 9}}
V = (1, 2, 4, 8, ..., 2¹²)
M = {x | x in S and x even}
```

In other words, you'll find that the above definitions actually tell you the following:

* The sequence S is actually a sequence that contains values between 0 and 9 included that are raised to the power of two.
* The sequence V, on the other hand, contains the value 2 that is raised to a certain power. For the first element in the sequence, this is 0, for the second this is 1, and so on, until you reach 12.
* Lastly, the sequence M contains elements from the sequence S, but only the even ones.

If the above definitions give you a headache, take a look at the actual lists that these definitions would produce:

```latex
S = {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
V = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096}
M = {0, 4, 16, 36, 64}
```


```python
# S = {x² : x in {0 ... 9}}
S = []
for x in range(10):
    S.append(x**2)
print(S)
```

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



```python
# S = {x² : x in {0 ... 9}}
S = [x**2 for x in range(10)]
print(S)
```

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


*The list S is built up with the square brackets that you read above in the first section. In those brackets, you see that there is an element x, which is raised to the power of 10. Now, you just need to know for how many values (and which values!) you need to raise to the power of 2. This is determined in range(10). Considering all of this, you can derive that you'll raise all numbers, going from 0 to 9, to the power of 2.*


```python
# V = (1, 2, 4, 8, ..., 2¹²)
V = []
for i in range(13):
    V.append(2**i)
print(V)
```

    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]



```python
# V = (1, 2, 4, 8, ..., 2¹²)
V = [2**i for i in range(13)]
print(V)
```

    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]


*The list V contains the base value 2, which is raised to a certain power. Just like before, now you need to know which power or i is exactly going to be used to do this. You see that i in this case is part of range(13), which means that you start from 0 and go until 12. All of this means that your list is going to have 13 values - those values will be 2 raised to the power 0, 1, 2, ... all the way up to 12.*


```python
# M = {x | x in S and x even}
M = []
for x in S:
    if x % 2 == 0:
        M.append(x)
print(M)
```

    [0, 4, 16, 36, 64]



```python
# M = {x | x in S and x even}
M = [x for x in S if x % 2 == 0]
print(M)
```

    [0, 4, 16, 36, 64]


*Lastly, the list M contains elements that are part of S if -and only if- they can be divided by 2 without having any leftovers. The modulo needs to be 0. In other words, the list M is built up with the equal values that are stored in list S.*

## List Comprehension as an Alternative to...

List comprehension is a complete substitute to for loops, lambda function as well as the functions ```map()```, ```filter()``` and ```reduce()```.

### For Loops

List comprehensions are actually good alternatives to for loops, as they are more compact. 

#### For Loop Example


```python
numbers = range(0, 10)

# Initialize `new_list`
new_list = []

# Add values to `new_list`
for n in numbers:
    if n % 2 == 0:
        new_list.append(n**2)

# Print `new_list`
print(new_list)
```

    [0, 4, 16, 36, 64]


#### List Comprehension Alternative to For Loop


```python
numbers = range(0, 10)

# Create `new_list` 
new_list = [n**2 for n in numbers if n%2==0]

# Print `new_list`
print(new_list)
```

    [0, 4, 16, 36, 64]


#### Which is faster?

Let's study the difference in performance between the list comprehension and the for loop with a small test: you can set this up very quickly with the timeit library, which you can use to time small bits of Python code in a simple way. In this case, the small pieces of code that you will test are the for loop, which you will put in a function called power_two() for your convenience, and the exact list comprehension which you have formulated above.


```python
# Import `timeit`
import timeit
```


```python
# Print the execution time
print(timeit.timeit('[n**2 for n in range(10) if n%2==0]', number=10000))
```

    0.02274465499795042



```python
# Define `power_two()` 
def power_two(numbers):
    for n in numbers:
        if n%2==0:
            new_list.append(n**2)
    return new_list
```


```python
print(timeit.timeit('power_two(numbers)', globals=globals(), number=10000))
```

    0.023647074995096773


### Lambda Functions with map(), filter() and reduce()

Lambda functions are also called "anonymous functions" or "functions without name". That means that you only use this type of functions when they are created. Lambda functions borrow their name from the lambda keyword in Python, which is used to declare these functions instead of the standard def keyword.

You usually use these functions together with the ```map()```, ```filter()```, and ```reduce()``` functions.

### Replace map() and Lambda Functions with List Comprehensions

#### Map Example


```python
# Initialize the `kilometer` list 
kilometer = [39.2, 36.5, 37.3, 37.8]

# Construct `feet` with `map()`
feet = map(lambda x: 3280.8399*x, kilometer)

# Print `feet` as a list 
print(type(feet), list(feet))
```

    <class 'map'> [128608.92408000001, 119750.65635, 122375.32826999998, 124015.74822]


#### List Comprehension Alternative to Map


```python
# Convert `kilometer` to `feet` 
feet = []
for x in kilometer:
    feet.append(3280.8399*x)
print(feet)
```

    [128608.92408000001, 119750.65635, 122375.32826999998, 124015.74822]



```python
# Convert `kilometer` to `feet` 
feet = [3280.8399*x for x in kilometer]

# Print `feet`
print(feet)
```

    [128608.92408000001, 119750.65635, 122375.32826999998, 124015.74822]


### Replace filter() and Lambda Functions with List Comprehensions

#### Filter Example


```python
# Filter `feet` to only include uneven distances 
uneven = filter(lambda x: x % 2, feet)

# Check the type of `uneven`
type(uneven)

# Print `uneven` as a list
print(list(uneven))
```

    [128608.92408000001, 119750.65635, 122375.32826999998, 124015.74822]


#### List Comprehension Alternative to Filter


```python
# Constructing `feet` 
feet = [int(x) for x in feet]

# Print `feet`
print(feet)

# Get all uneven distances
uneven = [True if x%2 else False for x in feet]

# Print `uneven`
print(uneven)
```

    [128608, 119750, 122375, 124015]
    [False, False, True, True]


### Replace reduce() and Lambda Functions with List Comprehensions

#### Reduce Example


```python
# Import `reduce` from `functools` 
from functools import reduce

# Reduce `feet` to `reduced_feet`
reduced_feet = reduce(lambda x,y: x+y, feet)

# Print `reduced_feet`
print(reduced_feet)
```

    494748


#### List Comprehension Alternative to Reduce


```python
# Construct `reduced_feet`
reduced_feet = sum([float(3280.8399)*x for x in kilometer])

# Print `reduced_feet`
print(reduced_feet)
```

    494750.65692000004


## List Comprehensions with Conditionals


```python
# Define `uneven`
uneven = [int(x) for x in feet if x%2]

# Print `uneven` 
print(uneven)
```

    [122375, 124015]


## Multiple If Conditions

### Example


```python
divided = []

for x in range(100):
    if x%2 == 0 :
        if x%6 == 0:
            divided.append(x)

print(divided)
```

    [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]


### List Comprehension Alternative


```python
divided = [x for x in range(100) if x % 2 == 0 if x % 6 == 0]

print(divided)
```

    [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]


## if...else Conditions

### Example


```python
values = []
for x in feet:  
    if x >= 120000:
        x + 1
    else: 
        x + 5
    values.append(x)

print(values)
```

    [128608, 119750, 122375, 124015]


### List Comprehension Alternative


```python
values = [x+1 if x >= 120000 else x+5 for x in feet]
print(values)
```

    [128609, 119755, 122376, 124016]


## Nested List Comprehensions

Apart from conditionals, you can also adjust your list comprehensions by nesting them within other list comprehensions. This is handy when you want to work with lists of lists: generating lists of lists, transposing lists of lists or flattening lists of lists to regular lists, for example, becomes extremely easy with nested list comprehensions.

You see that most of the keywords and elements that are used in the example of the nested list comprehension are similar to the ones that you used in the simple list comprehension examples:

* Square brackets
* Two for keywords, followed by a variable that symbolizes an item of the list of lists (x) and a list item of a nested list (y); And
* Two in keywords, followed by a list of lists (list_of_list) and a list item (x).


```python
list_of_list = [[1,2,3],[4,5,6],[7,8]]
print(list_of_list)
print(list_of_list[0])
print(list_of_list[1])
print(list_of_list[1][1])
print(list_of_list[2])
```

    [[1, 2, 3], [4, 5, 6], [7, 8]]
    [1, 2, 3]
    [4, 5, 6]
    5
    [7, 8]



```python
# Flatten `list_of_list`
flat = []
for x in list_of_list:
    for y in x:
        flat.append(y)
print(flat)
```

    [1, 2, 3, 4, 5, 6, 7, 8]



```python
# Flatten `list_of_list`
flat = [y for x in list_of_list for y in x]
print(flat)
```

    [1, 2, 3, 4, 5, 6, 7, 8]


Let's now consider another example, where you see that you can also use two pairs of square brackets to change the logic of your nested list comprehension:


```python
matrix = [[1,2,3], [4,5,6],[7,8,9]]

[[row[i] for row in matrix] for i in range(len(matrix))]
```




    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]



Now practice: rewrite the code chunk above to a nested for loop. If you need some pointers on how to tackle this exercise, go to one of the previous sections of this tutorial.


```python
transposed = []
for i in range(len(matrix)):
     transposed_row = []
     for row in matrix:
            transposed_row.append(row[i])
     transposed.append(transposed_row)
print(transposed)
```

    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


You can also use nested list comprehensions when you need to create a list of lists that is actually a matrix. Check out the following example:


```python
matrix = []
for x in range(3):
    nested = []
    matrix.append(nested)
    for row in range(4):
        nested.append(0)
print(matrix)
```

    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]



```python
# rewritten as a list comprehension
matrix = [[0 for col in range(4)] for row in range(3)]
matrix
```




    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]




```python

```
