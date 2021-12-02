---
layout: default
title: 05 - Writing Your First Test
parent: Topic 04 - Writing Testable Code
grand_parent: Lectures
nav_order: 5
---
# Writing Your First Test
[Source](https://realpython.com/python-testing/)

Let’s bring together what you’ve learned so far and, instead of testing the built-in sum() function, test a simple implementation of the same requirement.

Let’s bring together what you’ve learned so far and, instead of testing the built-in sum() function, test a simple implementation of the same requirement.

Create a new project folder and, inside that, create a new folder called `my_sum`. Inside `my_sum`, create an empty file called `__init__.py`. Creating the `__init__.py` file means that the `my_sum` folder can be imported as a module from the parent directory.

Your project folder should look like this:

```text
project/
│
└── my_sum/
    └── __init__.py
```

Open up `my_sum/__init__.py` and create a new function called `sum()`, which takes an iterable (a list, tuple, or set) and adds the values together:


```python
# contents of my_sum/__init__.py
def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total
```

## Where to Write the Test
To get started writing tests, you can simply create a file called test.py, which will contain your first test case. Because the file will need to be able to import your application to be able to test it, you want to place test.py above the package folder, so your directory tree will look something like this:

```text
project/
│
├── my_sum/
│   └── __init__.py
|
└── test.py
```

You’ll find that, as you add more and more tests, your single file will become cluttered and hard to maintain, so you can create a folder called `tests/` and split the tests into multiple files. It is convention to ensure each file starts with test_ so all test runners will assume that Python file contains tests to be executed. Some very large projects split tests into more subdirectories based on their purpose or usage.

***Note:*** What if your application is a single script?

You can import any attributes of the script, such as classes, functions, and variables by using the built-in `__import__()` function. Instead of `from my_sum import sum`, you can write the following:

```python
target = __import__("my_sum.py")
sum = target.sum
```

The benefit of using `__import__()` is that you don’t have to turn your project folder into a package, and you can specify the file name. This is also useful if your filename collides with any standard library packages. For example, `math.py` would collide with the `math` module.

## How to Structure a Simple Test

Before you dive into writing tests, you’ll want to first make a couple of decisions:

1. What do you want to test?
2. Are you writing a unit test or an integration test?

Then the structure of a test should loosely follow this workflow:

1. Create your inputs
2. Execute the code being tested, capturing the output
3. Compare the output with an expected result

For this application, you’re testing sum(). There are many behaviors in sum() you could check, such as:

1. Can it sum a list of whole numbers (integers)?
2. Can it sum a tuple or set?
3. Can it sum a list of floats?
4. What happens when you provide it with a bad value, such as a single integer or a string?
5. What happens when one of the values is negative?

The most simple test would be a list of integers. Create a file, `test.py` with the following Python code:

```python
import unittest

from fractions import Fraction
from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(1, 2)]
        result = sum(data)
        self.assertEqual(result, 1)

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)

if __name__ == '__main__':
    unittest.main()
```


```python
!python -m nose2 test
```

    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 0.000s
    
    OK


## Isolating Behaviors in our Application

Side effects make unit testing harder since, each time a test is run, it might give a different result, or even worse, one test could impact the state of the application and cause another test to fail!

There are some simple techniques you can use to test parts of your application that have many side effects:

* Refactoring code to follow the Single Responsibility Principle
* Mocking out any method or function calls to remove side effects
* Using integration testing instead of unit testing for this piece of the application

If you’re not familiar with mocking, see [Python CLI Testing](https://realpython.com/python-cli-testing/#mocks) for some great examples.


```python

```
