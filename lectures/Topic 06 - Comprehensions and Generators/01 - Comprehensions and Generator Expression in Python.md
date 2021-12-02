---
layout: default
title: 01 - Comprehensions and Generator Expression in Python
parent: Topic 06 - Comprehensions and Generators
grand_parent: Lectures
nav_order: 1
---
# Comprehensions and Generator Expressions
[Source](https://towardsdatascience.com/comprehensions-and-generator-expression-in-python-2ae01c48fc50)

To understand Python’s Comprehension capabilities, it’s important to understand the concept of comprehension at first. Comprehension in programming is nothing but writing the (existing) code in a short and concise manner, mostly one single line. It is constructing a new sequence by shortening the existing one. Being good at code comprehension is fairly an important skill. You need to understand the implementation to apply the comprehension capabilities of programming. Python-3 supports comprehensions for:

* List
* Dictionary
* Set
* Generator

## Different ways to define a List in Python

## Directly listing out elements,

A list can be defined directly by enumerating/listing out all of its elements between square brackets separated by a comma.


```python
num_cube=[8,64,216,512,1000]
print(f"num_cube[] = {num_cube}")
```

    num_cube[] = [8, 64, 216, 512, 1000]


## Using for loop,

Define an empty list and add elements using built-in method `append()` in a for loop. Here we are creating a List of cubes of even numbers ranging between `1` to `10`. We have defined an empty List num_cube_floop and a for loop iterating over `range(1,11)`. Condition `n % 2 == 0` will makes sure only even numbers are evaluated for the output expression `n**3`.


```python
num_cube_floop=[]

for n in range(1,11):
    if n % 2 == 0:
        num_cube_floop.append(n**3)
        
print(f"num_cube_floop[] = {num_cube_floop}")
```

    num_cube_floop[] = [8, 64, 216, 512, 1000]


## Using `+=` operator,

Similar to the above example we have defined an empty List num_cube_op and for loop is iterating over the input file `list_input.txt`. We are separating the input data using `split( )` before adding it to the List using the operator `+=`.


```python
num_cube_op = []

with open("list_input.txt","r") as input_data:
    for i in input_data:
        num_cube_op += i.split()
        
print(f"num_cube_op[] = {num_cube_op}")
```

    num_cube_op[] = ['8', '64', '216', '512', '1000']


## Using map(),

Here, we are using `map()` to create a List from the existing List. For anyone new to `map()` and `lambda` expression,

* `map(function_to_apply, iterable)` — it applies ‘function’ to all the elements of an ‘iterable’.
* `lambda parameters:output expression` — anonymous function, it is defined without a name and does not follow normal python function conventions.

In the below code, `map( )` applies `lambda` expression(calculates a cube of the number) to existing List numbers and cast the output using `list( )` before the result is assigned to new List `num_cube_maps`.


```python
numbers=[2,4,6,8,10]
num_cube_map=list(map(lambda n: n**3, numbers))

print(f"num_cube_map[] = {num_cube_map}") 
```

    num_cube_map[] = [8, 64, 216, 512, 1000]



```python
def cube_number(num):
    return numm ** 3
```

There is yet another way of creating a List using Python’s Comprehension capabilities. It lets us create a List in a single line of code. It may seem a little difficult to understand at first as the syntax can be intimidating but here we are going to break it down for a simpler understanding.

## List Comprehension

List Comprehension’s general syntax is similar to [set-builder notation](https://en.wikipedia.org/wiki/Set-builder_notation). In set-theory, *“Set-builder notation is a mathematical notation of defining a set by either listing out all the elements of the set or by describing the properties that all set elements must satisfy.”*

![img1](https://miro.medium.com/max/754/1*utQceHZEfQNPUGwneddDKQ.png)

The left side of ‘|’ is an output expression and the right side is a rule which must be satisfied by all the elements of a set.

![img2](https://miro.medium.com/max/918/1*ZsTnY48v6js9hFXp8OV9wQ.png)

Here, output expression (n3) defines the elements of the set and rule is consists of input set (n ϵ N) and filter conditions (n<=10 and n!=0). 

The above set definition basically maps all the natural numbers in set N (0,1,2,….) and limits the input with n<=10 and n!=0. 

The resulting set is,

S1 = {8, 64, 216, 512, 1000}

S1 = {n3 ∣ n ϵ N, n<=10 and n !=0}

Similarly, the most basic syntax of List Comprehension is,
![img3](https://miro.medium.com/max/1032/1*7MZ15wfRvCVmO3EYiky8Tg.png)

## Examples

### With `for` loop


```python
# print the characters of a string as List
name="Python Programming"
name_ltr=[]

for letter in name:
    name_ltr.append(letter)
    
print(f"name_ltr[] = {name_ltr}")
```

    name_ltr[] = ['P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']



```python
# with List Comprehension
name_ltr_lc = [letter for letter in name]
print(f"With List-Comprehension = {name_ltr_lc}")
```

    With List-Comprehension = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']


In the above example, we need to create a List of all the characters of the string literal. The usual way of achieving this is by defining an empty List and using `append( )` method inside a for loop to add the elements to our List. Here for loop is iterating over the string literal name and `append( )` adds all single characters of the string literal to List `name_ltr`. The same result can be obtained using List Comprehension without even worrying about defining a List or using `append( )`.

![img4](https://miro.medium.com/max/1400/1*HZwXpipEKu4jLIXO4x7n5A.png)

If we examine the syntax, List Comprehension is nothing but the rearrangement of the for loop and the output expression. We put the output expression at the beginning of the comprehension syntax followed by the loop. It’s pretty straightforward.

![img5](attachment:08f7ec17-d2d5-4796-ad89-a87baa688330.png)

### With if statement

Let’s take this a little further by adding a conditional statement to it. At the beginning of the article, we saw four different ways of creating a List of the cube of even numbers, one was using for loop


```python
# creating a List of even numbers' cube
num_cube_floop=[]

for n in range(1,11):
    if n % 2 == 0:                               
        num_cube_floop.append(n**3)
        
print(f"num_cube_floop[] = {num_cube_floop}")
```

    num_cube_floop[] = [8, 64, 216, 512, 1000]



```python
# with List Comprehension
num_cube_lc=[n**3 for n in range(1,11) if n % 2 == 0]
print(f"With List-Comprehension = {num_cube_lc}")
```

    With List-Comprehension = [8, 64, 216, 512, 1000]


As we can see in the code block, four lines of code are reduced to a single line when using List Comprehension.

![img6](https://miro.medium.com/max/1400/1*E-Kj66cJddWqRu16SkQcmQ.png)

Let’s take another example, create a List of words starting from a specific letter of a given string literal.


```python
# list out words starting from letter 'P'
statement="List Comprehension is one of the famous features of Python Programming"
words=[]

for w in statement.split():
    if w.startswith('P'):
        words.append(w)

print(f"words[] = {words}")
```

    words[] = ['Python', 'Programming']



```python
# with List Comprehension

words_lc = [w for w in statement.split() if w.startswith('P')]
print(f"With List-Comprehension = {words_lc}")
```

    With List-Comprehension = ['Python', 'Programming']


Here, `statement.split( )` separates(default separator is white space)all the words within the string literal and for loop will be iterated through it to filter all the words starting from letter `P` and result will be added to the List using `words.append(w)`. While using List Comprehension, output expression(which is always placed at the beginning) `w` is placed first, for loop is iterating over the string literal followed by if-condition.

![img7](https://miro.medium.com/max/501/1*pM6S2suisZx65uhp0Z3UZA.png)

### With if-else statement

The placement of if-else statement is different than the previously discussed scenarios in List Comprehension. When if-else conditional block is used, it is placed right after the output expression as shown in the below image.

![img8](https://miro.medium.com/max/700/1*Ut6aXMocCWy08c-bdK-maQ.png)

Let’s create a List of numbers<10 where we have to calculate square for even numbers and cube for the odd.


```python
square_cube=[]  #creating a List of numbers - even number->square and odd number->cube

for num in range(10):
    if num % 2==0:
        square_cube.append(num**2)
    else:
        square_cube.append(num**3)
 
print(f"square_cube[] = {square_cube}")
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    square_cube[] = [0, 1, 4, 27, 16, 125, 36, 343, 64, 729]



```python
#with List Comprehension
square_cube_lc = [ n**2 if n%2==0 else n**3 for n in range(10) ]
print(f"With List-Conprehension = {square_cube_lc}")
```

    With List-Conprehension = [0, 1, 4, 27, 16, 125, 36, 343, 64, 729]


The above code block filters the numbers based on condition `num % 2 == 0` and accordingly execute either `square_cube.append(num ** 2)` or `square_cube.append(num ** 3)`. While using List Comprehension output expression associated with if-statement is placed first and the other condition is followed by the else keyword.

![img9](https://miro.medium.com/max/682/1*Gi8JeAsHOh_BgVwkaDkHmg.png)

It’s really up to us how to convert the usual for loops into List comprehension, in yet another odd/even numbers example, I have created two Lists within a List numbers and the code block is self-explanatory.


```python
#Creating a List of two Lists - one for even numbers another for odd numbers.(Lists within a List)
numbers=[]
even=[]
odd=[]

for num in range(10):
    if num%2==0:
        even.append(num**2)
    else:
        odd.append(num**3)

numbers = [even,odd]
print(f"numbers[] = {numbers}")
```

    numbers[] = [[0, 4, 16, 36, 64], [1, 27, 125, 343, 729]]



```python
#with list comprehension
numbers_lc=[[n**2 for n in range(10) if n%2==0],[n**3 for n in range(10)  if n%2!=0]]
print(f"With List-Conprehension = {numbers_lc}")
```

    With List-Conprehension = [[0, 4, 16, 36, 64], [1, 27, 125, 343, 729]]


The difference is how the List is constructed using comprehension, two separate expressions are defined in order to create two Lists within a List.

![img10](https://miro.medium.com/max/700/1*ehNIETFNQF5cYK9UvYx9Og.png)

### With nested-for loops

Let’s take another example before wrapping up the List Comprehension. It is pretty inclusive and most of the time it can be used neatly for nested loops. We need to create a List of the [cartesian product](https://en.wikipedia.org/wiki/Cartesian_product) of two existing Lists char_list and int_list. One for loop is iterating over `char_list` and another over `int_list`. Elements from both the Lists are added to the resulting List cartesian as a tuple using `cartesian.append((x,y))`.


```python
#cartesian product of two Lists
char_list=['a','b','c']
int_list=[0,1,2,3]
cartesian=[]

for x in char_list:
    for y in int_list:
        cartesian.append((x,y))
        
print(f"cartesian[] = \n {cartesian}")        
```

    cartesian[] = 
     [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('c', 0), ('c', 1), ('c', 2), ('c', 3)]



```python
#with List Comprehension
cartesian_lc = [(x,y) for x in char_list for y in int_list]
print(f"With List-Conprehension = \n {cartesian_lc}")
```

    With List-Conprehension = 
     [('a', 0), ('a', 1), ('a', 2), ('a', 3), ('b', 0), ('b', 1), ('b', 2), ('b', 3), ('c', 0), ('c', 1), ('c', 2), ('c', 3)]


Output expression is a tuple and hence it is parenthesized. In List Comprehension nested for loops are placed in the order they are expected to be executed.

![img11](https://miro.medium.com/max/544/1*mktIdr_N7xFXQg3i_dLrEw.png)

In the below code block, person is a List consisting of two dictionaries. Each of them has two keys, name and language. Now we have to create a List of values associated with a key, language. First for loop is iterating through the length of a List person and second, for loop is set up to get values of the key, language at the given index.


```python
#dictionary inside a list
person = [ {'name': "Emma", 'language': ["Python", "Java"]},
           {'name': "Harry", 'language': ["C++", "C#"]} 
         ]
language=[]

for p in range(len(person)):
    for l in person[p]['language']:
        language.append(l)
        
print(f"person[] = {language}")
```

    person[] = ['Python', 'Java', 'C++', 'C#']



```python
#with List Comprehension
person_lc=[l for p in range(len(person)) for l in person[p]['language']]  
print(f"With List-Conprehension = {person_lc}",)
```

    With List-Conprehension = ['Python', 'Java', 'C++', 'C#']


The same result is achieved using List Comprehension by rearranging for loops in a single line.

![img12](https://miro.medium.com/max/684/1*QTks_MSobwZFvs66QwIZnw.png)

## Set Comprehension

Set Comprehension functions the same way as List Comprehension except for the fact that it returns a Set and curly braces `{` `}` are used instead of square brackets `[` `]`. As it returns a Set, it will be of unique elements (Set property).

Consider the same example we have discussed earlier, a List person consisting of three dictionary entries. If we compare the syntax of List and Set Comprehension in the code block, the difference is just square brackets and curly braces. Though output is different, unlike List Comprehension, Set Comprehension returns unique values.


```python
#dictionary inside a list
person = [ {'name': "Emma", 'language': ["Python", "Java"]},
           {'name': "Harry", 'language': ["C++", "Python"]},
           {'name': "Lily", 'language': ["Python"]} 
         ]
```


```python
#with List Comprehension
person_lc=[l for p in range(len(person)) for l in person[p]['language']]  
print(f"With List-Conprehension = {person_lc}")
```

    With List-Conprehension = ['Python', 'Java', 'C++', 'Python', 'Python']



```python
#with Set Comprehension
person_sc = {l for p in range(len(person)) for l in person[p]['language']}
print(f"With Set-Conprehension = {person_sc}")
```

    With Set-Conprehension = {'Java', 'C++', 'Python'}


## Dictionary Comprehension

Unlike both List and Set Comprehension, Dictionary Comprehension is used when data is expected to be in a key-value pairing format. Let’s continue to the legacy of our number cube examples.


```python
numbers=[num for num in range(1,11)]    #creating a List of numbers from 1 to 10
print(numbers)
num_cube=[n**3 for n in numbers]        #creating a List of cubes of numbers from 1 to 10     
print(num_cube)

cubes={}

for (key,value) in zip(numbers,num_cube):
    cubes[key]=value
    
print(f"cubes = {cubes}")  
```

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    cubes = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}



```python
#with Dictionary Comprehension
cubes_dc = {key:value for (key,value) in zip(numbers,num_cube)}
print(f"With Dictionary-Comprehension = {cubes_dc}")
```

    With Dictionary-Comprehension = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}


Two Lists are created using List Comprehension we have discussed earlier.


```python
numbers=[num for num in range(1,11)]  
#numbers=[1,2,3,4,5,6,7,8,9,10]  

num_cube=[n**3 for n in numbers]
#num_cube=[1,8,27,64,125,216,343,512,729,1000]
```

We need to create a Dictionary where the value of a key is the number from List numbers and value comes from the second List `num_cubes`. for loop is iterating over `zip(numbers, num_cube)` for getting keys and values as tuple (key,value).

`zip(iterables)` — maps the similar indexes of multiple containers and returns an iterator which is a series of tuples containing elements from each iterable passed in argument.


```python
print(list(zip(numbers,num_cube)))
```

    [(1, 1), (2, 8), (3, 27), (4, 64), (5, 125), (6, 216), (7, 343), (8, 512), (9, 729), (10, 1000)]


The output expression key:value, maps the values returned from zip(numbers,num_cube) as shown in the below image.
![img.png](https://miro.medium.com/max/650/1*yaesbTnpD0JgAW5IyluUeQ.png)

## Generator Expression
The syntax of Generator Expression is similar to List Comprehension except it uses parentheses `(` `)` instead of square brackets `[` `]`. Generators are special iterators in Python which returns the generator object. The point of using it, is to generate a sequence of items without having to store them in memory and this is why you can use Generator only once.

Here, we have created a List num_cube_lc using List Comprehension and Generator Expression is defined as num_cube_generator.


```python
num_cube_lc=[n**3 for n in range(1,11) if n%2==0]    #List Comprehension
num_cube_generator=(num**3 for num in range(1,11) if num%2==0)  #Generator Expression

print(f"List Comprehension = {num_cube_lc}")
print(f"Generator Expression = {num_cube_generator}")

#sum(num_cube_generator)
print(f"Sum = {sum(num_cube_generator)}")
```

    List Comprehension = [8, 64, 216, 512, 1000]
    Generator Expression = <generator object <genexpr> at 0x7f9f187723c0>
    Sum = 1800


The output of Generator Expression is not like the one of List Comprehension; However, when used with sum( ) it does pass values generated from the expression.

## Conclusion
Comprehensions are surely an effective way to reduce the line of code in general. Code is easier to read and understand most of the time; however, if you have multiple nested loops in your program logic, using Comprehension does make you sacrifice readability. Though Comprehensions are considered a more pythonic way of coding by some, it’s really up to you to determine the best situation to use or avoid it. Some of the useful resources for the topic are,

* [Set-builder notation in set theory](https://en.wikipedia.org/wiki/Set-builder_notation#cite_note-2)
* [5.1.3 List Comprehension](https://docs.python.org/3/tutorial/datastructures.html)
* [Generator Expression and Comprehension](https://docs.python.org/3/howto/functional.html?highlight=generator%20compression)

The code used for this article can be accessed from the author's [GitHub Repository](https://github.com/PhoenixIM/Pure_Python/blob/master/comprehensions.ipynb)
