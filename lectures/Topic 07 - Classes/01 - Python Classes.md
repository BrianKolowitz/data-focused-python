---
layout: default
title: 01 - Python Classes
parent: Topic 07 - Classes
grand_parent: Lectures
nav_order: 1
---
# Python Classes
[Object-Oriented Programming (OOP) in Python](https://realpython.com/python3-object-oriented-programming/)

## Classes in Python

Focusing first on the data, each thing or object is an instance of some class.

Classes are used to create new user-defined data structures that contain arbitrary information about something. In the case of an person, we could create a Person() class to track properties about the Person like the name and age.

It’s important to note that a class just provides structure—it’s a blueprint for how something should be defined, but it doesn’t actually provide any real content itself. The Person() class may specify that the name and age are necessary for defining an person, but it will not actually state what a specific person’s name or age is.

It may help to think of a class as an idea for how something should be defined.

## Python Objects (Instances)

While the class is the blueprint, an instance is a copy of the class with actual values, literally an object belonging to a specific class. It’s not an idea anymore; it’s an actual person, like a person named Bill who’s twenty years old.

Put another way, a class is like a form or questionnaire. It defines the needed information. After you fill out the form, your specific copy is an instance of the class; it contains actual information relevant to you.

You can fill out multiple copies to create many different instances, but without the form as a guide, you would be lost, not knowing what information is required. Thus, before you can create individual instances of an object, we must first specify what is needed by defining a class.

## How To Define a Class in Python


```python
class Person:
    pass
```

## Instance Attributes

All classes create objects, and all objects contain characteristics called attributes (referred to as properties in the opening paragraph). Use the ```__init__()``` method to initialize (e.g., specify) an object’s initial attributes by giving them their default value (or state). This method must have at least one argument as well as the self variable, which refers to the object itself (e.g., Person).


```python
class Person:
    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

In the case of our Person() class:
* each person has a specific name and age, which is obviously important to know for when you start actually creating different persons. *Remember: the class is just for defining the Person, not actually creating instances of individual persons with specific names and ages; we’ll get to that shortly.*
* Similarly, the ```self``` variable is also an instance of the class. Since instances of a class have varying values we could state Person.name = name rather than self.name = name. But since not all persons share the same name, we need to be able to assign different values to different instances. Hence the need for the special self variable, which will help to keep track of individual instances of each class.

*Note: You will never have to call the ```__init__()``` method; it gets called automatically when you create a new ‘Person’ instance.*

## Class Attributes

While instance attributes are specific to each object, class attributes are the same for all instances—which in this case is all persons. So while each person has a unique name and age, every person is a homo sapien.


```python
class Person:
    
    # Class Attribute
    species = 'homo sapien'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

## Instantiating Objects

Instantiating is a fancy term for creating a new, unique instance of a class.


```python
class Animal:
    pass
```


```python
a = Animal()
print('a is type', type(a), 'value', a)

b = Animal()
print('b is type', type(b), 'value', b)

c = b
```

    a is type <class '__main__.Animal'> value <__main__.Animal object at 0x7ff4b06b02b0>
    b is type <class '__main__.Animal'> value <__main__.Animal object at 0x7ff4b06b0a30>



```python
a == b
```




    False




```python
print(a == c)
print(b == c)
```

    False
    True



```python
# Instantiate the Person object
ben = Person("Ben", 37)
geno = Person("Geno", 32)

# Access the instance attributes
print(f"{ben.name} is {ben.age} and {geno.name} is {geno.age}.")

# Is Ben a mammal?
if ben.species == "homo sapien":
    print(f"{ben.name} is a {ben.species}!")
```

    Ben is 37 and Geno is 32.
    Ben is a homo sapien!


## Instance Methods

Instance methods are defined inside a class and are used to get the contents of an instance. They can also be used to perform operations with the attributes of our objects. Like the ```__init__``` method, the first argument is always self:


```python
class Dog:
    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
```


```python
# Instantiate the Dog object
mikey = Dog("Mikey", 6)
```


```python
# call our instance methods
print(mikey.description())
print(mikey.speak("Gruff Gruff"))
```

    Mikey is 6 years old
    Mikey says Gruff Gruff


### Modifying Attributes

You can change the value of attributes based on some behavior:


```python
class Email:
    def __init__(self):
        self.is_sent = False
    
    def send_email(self):
        self.is_sent = True
```


```python
my_email = Email()
my_email.is_sent
```




    False




```python
my_email.send_email()
my_email.is_sent
```




    True



## Python Object Inheritance

Inheritance is the process by which one class takes on the attributes and methods of another. Newly formed classes are called child classes, and the classes that child classes are derived from are called parent classes.

It’s important to note that child classes override or extend the functionality (e.g., attributes and behaviors) of parent classes. In other words, child classes inherit all of the parent’s attributes and behaviors but can also specify different behavior to follow. The most basic type of class is an object, which generally all other classes inherit as their parent.

## [Dog Park Example](https://realpython.com/python3-object-oriented-programming/)

Let’s pretend that we’re at a dog park. There are multiple Dog objects engaging in Dog behaviors, each with different attributes. In regular-speak that means some dogs are running, while some are stretching and some are just watching other dogs. Furthermore, each dog has been named by its owner and, since each dog is living and breathing, each ages.


```python
class Dog:
    def __init__(self, breed):
        self.breed = breed
```


```python
spencer = Dog("German Shepard")
spencer.breed
```




    'German Shepard'




```python
sara = Dog("Boston Terrier")
sara.breed
```




    'Boston Terrier'



### Extending the Functionality of a Parent Class


```python
# Parent class
class Dog:

    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
```


```python
# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
```


```python
# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
```


```python
# Child classes inherit attributes and
# behaviors from the parent class
jim = Bulldog("Jim", 12)
print(jim.description())
```

    Jim is 12 years old



```python
# Child classes have specific attributes
# and behaviors as well
print(jim.run("slowly"))
```

    Jim runs slowly


## Parent vs. Child Classes

The ```isinstance()``` function is used to determine if an instance is also an instance of a certain parent class.


```python
# Child classes inherit attributes and
# behaviors from the parent class
jim = Bulldog("Jim", 12)

# Is jim an instance of Dog()?
print(isinstance(jim, Dog))
```

    True



```python
print(isinstance(jim, Bulldog))
```

    True



```python
print(isinstance(jim, RussellTerrier))
```

    False


## Overriding the Functionality of a Parent Class

Remember that child classes can also override attributes and behaviors from the parent class. For examples:


```python
class FrenchBulldog(Bulldog):
    species = 'french bulldog'
```


```python
sleepy = FrenchBulldog('sleepy', 2)
```


```python
print(sleepy.species)
```

    french bulldog



```python
print(isinstance(sleepy, Bulldog))
```

    True



```python
print(isinstance(sleepy, FrenchBulldog))
```

    True



```python

```
