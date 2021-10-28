---
layout: default
title: 04- Choosing a Test Runner
parent: Topic 04 - Writing Testable Code
grand_parent: Lectures
nav_order: 4
---
# Choosing a Test Runner
[Source](https://realpython.com/python-testing/)

* [Pytest](https://docs.pytest.org/en/latest/)
* [Getting Started with Pytest](https://docs.pytest.org/en/latest/getting-started.html)

There are many test runners available for Python. The one built into the Python standard library is called unittest. In this tutorial, you will be using unittest test cases and the unittest test runner. The principles of unittest are easily portable to other frameworks. The three most popular test runners are:

* unittest
* nose or nose2
* pytest

Choosing the best test runner for your requirements and level of experience is important.

## unittest

unittest has been built into the Python standard library since version 2.1. You’ll probably see it in commercial Python applications and open-source projects.

unittest contains both a testing framework and a test runner. unittest has some important requirements for writing and executing tests.

unittest requires that:

* You put your tests into classes as methods
* You use a series of special assertion methods in the unittest.TestCase class instead of the built-in assert statement

To convert the earlier example to a unittest test case, you would have to:

1. Import unittest from the standard library
2. Create a class called TestSum that inherits from the TestCase class
3. Convert the test functions into methods by adding self as the first argument
4. Change the assertions to use the self.assertEqual() method on the TestCase class
5. Change the command-line entry point to call unittest.main()

```python
# test_sum_unittest.py
import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()
```

If you execute this at the command line, you’ll see one success (indicated with .) and one failure (indicated with F):


```python
!python test_sum_unittest.py
```

    .F
    ======================================================================
    FAIL: test_sum_tuple (__main__.TestSum)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/Users/bk/Source/data-focused-python/lectures/Topic 04 - Writing Testable Code/test_sum_unittest.py", line 10, in test_sum_tuple
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
    AssertionError: 5 != 6 : Should be 6
    
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s
    
    FAILED (failures=1)


## nose

You may find that over time, as you write hundreds or even thousands of tests for your application, it becomes increasingly hard to understand and use the output from unittest.

nose is compatible with any tests written using the unittest framework and can be used as a drop-in replacement for the unittest test runner. The development of nose as an open-source application fell behind, and a fork called nose2 was created. If you’re starting from scratch, it is recommended that you use nose2 instead of nose.

To get started with nose2, install nose2 from PyPI and execute it on the command line. nose2 will try to discover all test scripts named test*.py and test cases inheriting from unittest.TestCase in your current directory:

```bash
pip install nose2
python -m nose2
```


```python
!python -m nose2 test_sum_unittest
```

    .F
    ======================================================================
    FAIL: test_sum_tuple (test_sum_unittest.TestSum)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/Users/bk/Source/data-focused-python/lectures/Topic 04 - Writing Testable Code/test_sum_unittest.py", line 10, in test_sum_tuple
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
    AssertionError: 5 != 6 : Should be 6
    
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s
    
    FAILED (failures=1)


You have just executed the test you created in test_sum_unittest.py from the nose2 test runner. nose2 offers many command-line flags for filtering the tests that you execute. For more information, you can explore the [Nose 2 documentation](https://nose2.readthedocs.io/).

## pytest

[pytest](https://realpython.com/pytest-python-testing/) supports execution of unittest test cases. The real advantage of pytest comes by writing pytest test cases. pytest test cases are a series of functions in a Python file starting with the name test_.

pytest has some other great features:

* Support for the built-in assert statement instead of using special `self.assert*()` methods
* Support for filtering for test cases
* Ability to rerun from the last failing test
* An ecosystem of hundreds of plugins to extend the functionality

Writing the TestSum test case example for pytest would look like this:


```python
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"
```

You have dropped the TestCase, any use of classes, and the command-line entry point.

More information can be found at the [Pytest Documentation Website](https://docs.pytest.org/en/latest/).
