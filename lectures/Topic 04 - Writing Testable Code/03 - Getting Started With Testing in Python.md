---
layout: default
title: 03 - Getting Started With Testing in Python
parent: Topic 04 - Writing Testable Code
grand_parent: Lectures
nav_order: 3
---
# Getting Started With Testing in Python
[Source](https://realpython.com/python-testing/)

## Automated vs. Manual Testing

* To have a complete set of manual tests, all you need to do is make a list of all the features your application has, the different types of input it can accept, and the expected results. Now, every time you make a change to your code, you need to go through every single item on that list and check it.
* Automated testing is the execution of your test plan (the parts of your application you want to test, the order in which you want to test them, and the expected responses) by a script instead of a human. Python already comes with a set of tools and libraries to help you create automated tests for your application. 

## Unit Tests vs. Integration Tests

The world of testing has no shortage of terminology, and now that you know the difference between automated and manual testing, it’s time to go a level deeper.

Think of how you might test the lights on a car. You would turn on the lights (known as the test step) and go outside the car or ask a friend to check that the lights are on (known as the test assertion). Testing multiple components is known as integration testing.

Think of all the things that need to work correctly in order for a simple task to give the right result. These components are like the parts to your application, all of those classes, functions, and modules you’ve written.

A major challenge with integration testing is when an integration test doesn’t give the right result. It’s very hard to diagnose the issue without being able to isolate which part of the system is failing. If the lights didn’t turn on, then maybe the bulbs are broken. Is the battery dead? What about the alternator? Is the car’s computer failing?

If you have a fancy modern car, it will tell you when your light bulbs have gone. It does this using a form of unit test.

A unit test is a smaller test, one that checks that a single component operates in the right way. A unit test helps you to isolate what is broken in your application and fix it faster.

You have just seen two types of tests:

* An integration test checks that components in your application operate with each other.
* A unit test checks a small component in your application.

You can write both integration tests and unit tests in Python. To write a unit test for the built-in function sum(), you would check the output of sum() against a known output.

For example, here’s how you check that the sum() of the numbers (1, 2, 3) equals 6:

To write a unit test for the built-in function sum(), you would check the output of sum() against a known output.


```python
assert sum([1, 2, 3]) == 6, "Should be 6"
```

If the result from sum() is incorrect, this will fail with an AssertionError and the message "Should be 6".


```python
assert sum([1, 1, 1]) == 6, "Should be 6"
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    /var/folders/jd/pq0swyt521jb2424d6fvth840000gn/T/ipykernel_3247/17110154.py in <module>
    ----> 1 assert sum([1, 1, 1]) == 6, "Should be 6"
    

    AssertionError: Should be 6


We can write a test function to encapsualte the test.


```python
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"
```

... and execute it as follows.


```python
test_sum()
print("Everything passed")
```

    Everything passed


However, instead of testing on the REPL, you’ll want to put this into a new Python file called test_sum.py and execute it again:


```python
!python test_sum.py
```

    Everything passed


Let's expand out test suite to include summing a tuple.


```python
def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"
```


```python
test_sum()
test_sum_tuple()
print("Everything passed")
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    /var/folders/jd/pq0swyt521jb2424d6fvth840000gn/T/ipykernel_3247/2054533739.py in <module>
          1 test_sum()
    ----> 2 test_sum_tuple()
          3 print("Everything passed")


    /var/folders/jd/pq0swyt521jb2424d6fvth840000gn/T/ipykernel_3247/2526289347.py in test_sum_tuple()
          1 def test_sum_tuple():
    ----> 2     assert sum((1, 2, 2)) == 6, "Should be 6"
    

    AssertionError: Should be 6


We've updated `test_sum_2.py` with the new code which can be executed as follows:


```python
!python test_sum_2.py
```

    Traceback (most recent call last):
      File "/Users/bk/Source/data-focused-python/lectures/Topic 04 - Writing Testable Code/test_sum_2.py", line 9, in <module>
        test_sum_tuple()
      File "/Users/bk/Source/data-focused-python/lectures/Topic 04 - Writing Testable Code/test_sum_2.py", line 5, in test_sum_tuple
        assert sum((1, 2, 2)) == 6, "Should be 6"
    AssertionError: Should be 6

