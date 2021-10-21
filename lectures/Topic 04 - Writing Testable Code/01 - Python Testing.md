---
layout: default
title: 01 - Python Testing
parent: Topic 04 - Writing Testable Code
grand_parent: Lectures
nav_order: 1
---
# 8 Benefis of Unit Testing
[8 benefits of unit testing](https://dzone.com/articles/top-8-benefits-of-unit-testing)

The goal of unit testing is to segregate each part of the program and test that the individual parts are working correctly. 
1. It isolates the smallest piece of testable software from the remainder of the code and determines whether it behaves exactly as you expect. 
1. Unit testing has proven its value in that a large percentage of defects are identified during its use. 
1. It allows automation of the testing process, reduces difficulties of discovering errors contained in more complex pieces of the application, and enhances test coverage because attention is given to each unit.

## 1. Makes the Process Agile
One of the main benefits of unit testing is that it makes the coding process more Agile. When you add more and more features to a software, you sometimes need to change old design and code. However, changing already-tested code is both risky and costly. If we have unit tests in place, then we can proceed for refactoring confidently.

Unit testing really goes hand-in-hand with agile programming of all flavors because it builds in tests that allow you to make changes more easily. In other words, unit tests facilitate safe refactoring. 

## 2. Quality of Code
Unit testing improves the quality of the code. It identifies every defect that may have come up before code is sent further for integration testing. Writing tests before actual coding makes you think harder about the problem. It exposes the edge cases and makes you write better code. 

## 3. Finds Software Bugs Early
Issues are found at an early stage. Since unit testing is carried out by developers who test individual code before integration, issues can be found very early and can be resolved then and there without impacting the other pieces of the code. This includes both bugs in the programmer’s implementation and flaws or missing parts of the specification for the unit.

## 4. Facilitates Changes and Simplifies Integration
Unit testing allows the programmer to refactor code or upgrade system libraries at a later date and make sure the module still works correctly. Unit tests detect changes that may break a design contract. They help with maintaining and changing the code.

Unit testing reduces defects in the newly developed features or reduces bugs when changing the existing functionality. 

Unit testing verifies the accuracy of the each unit. Afterward, the units are integrated into an application by testing parts of the application via unit testing. Later testing of the application during the integration process is easier due to the verification of the individual units.

## 5. Provides Documentation
Unit testing provides documentation of the system. Developers looking to learn what functionality is provided by a unit and how to use it can look at the unit tests to gain a basic understanding of the unit’s interface (API).

## 6. Debugging Process
Unit testing helps simplify the debugging process. If a test fails, then only the latest changes made in the code need to be debugged.

## 7. Design
Writing the test first forces you to think through your design and what it must accomplish before you write the code. This not only keeps you focused; it makes you create better designs. Testing a piece of code forces you to define what that code is responsible for. If you can do this easily, that means the code’s responsibility is well-defined and therefore that it has high cohesion.

## 8. Reduce Costs
Since the bugs are found early, unit testing helps reduce the cost of bug fixes. Just imagine the cost of a bug found during the later stages of development, like during system testing or during acceptance testing. Of course, bugs detected earlier are easier to fix because bugs detected later are usually the result of many changes, and you don’t really know which one caused the bug. 

# Getting Started With Testing in Python
[Getting Started With Testing in Python
](https://realpython.com/python-testing/)

## Automated vs. Manual Testing

* To have a complete set of manual tests, all you need to do is make a list of all the features your application has, the different types of input it can accept, and the expected results. Now, every time you make a change to your code, you need to go through every single item on that list and check it.
* Automated testing is the execution of your test plan (the parts of your application you want to test, the order in which you want to test them, and the expected responses) by a script instead of a human. Python already comes with a set of tools and libraries to help you create automated tests for your application. 

## Unit Tests vs. Integration Tests

* Think of how you might test the lights on a car. You would turn on the lights (known as the test step) and go outside the car or ask a friend to check that the lights are on (known as the test assertion). Testing multiple components is known as integration testing.
* Think of all the things that need to work correctly in order for a simple task to give the right result. These components are like the parts to your application, all of those classes, functions, and modules you’ve written.
  
You have just seen two types of tests:

1. An integration test checks that components in your application operate with each other.
1. A unit test checks a small component in your application.

You can write both integration tests and unit tests in Python.


```python
# To write a unit test for the built-in function sum(), you would check the output of sum() against a known output.
assert sum([1, 2, 3]) == 6, "Should be 6"
```


```python
# If the result from sum() is incorrect, this will fail with an AssertionError and the message "Should be 6".
assert sum([1, 1, 1]) == 6, "Should be 6"
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    /var/folders/jd/pq0swyt521jb2424d6fvth840000gn/T/ipykernel_91889/1130538575.py in <module>
          1 # If the result from sum() is incorrect, this will fail with an AssertionError and the message "Should be 6".
    ----> 2 assert sum([1, 1, 1]) == 6, "Should be 6"
    

    AssertionError: Should be 6



```python
# Instead of testing on the REPL, you’ll want to put this into a new Python file called test_sum.py and execute it again:
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"
```


```python
test_sum()
print("Everything passed")
```

    Everything passed



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

    /var/folders/jd/pq0swyt521jb2424d6fvth840000gn/T/ipykernel_91889/2054533739.py in <module>
          1 test_sum()
    ----> 2 test_sum_tuple()
          3 print("Everything passed")


    /var/folders/jd/pq0swyt521jb2424d6fvth840000gn/T/ipykernel_91889/2526289347.py in test_sum_tuple()
          1 def test_sum_tuple():
    ----> 2     assert sum((1, 2, 2)) == 6, "Should be 6"
    

    AssertionError: Should be 6


# Choosing a Test Runner
* [Pytest](https://docs.pytest.org/en/latest/)
* [Getting Started with Pytest](https://docs.pytest.org/en/latest/getting-started.html)

There are many test runners available for Python. The one built into the Python standard library is called unittest. In this tutorial, you will be using unittest test cases and the unittest test runner. The principles of unittest are easily portable to other frameworks. The three most popular test runners are:

* unittest
* nose or nose2
* **pytest** *(we'll use pytest)*

content of [test_sample.py](test_sample.py)


```python
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
```


```python
!pytest test_sample.py
```

    [1m============================= test session starts ==============================[0m
    platform darwin -- Python 3.9.7, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
    rootdir: /Users/bk/Source/data-focused-python/lectures/Topic 04 - Writing Testable Code
    plugins: Faker-9.3.1, anyio-3.3.3
    collected 1 item                                                               [0m
    
    test_sample.py [31mF[0m[31m                                                         [100%][0m
    
    =================================== FAILURES ===================================
    [31m[1m_________________________________ test_answer __________________________________[0m
    
        [94mdef[39;49;00m [92mtest_answer[39;49;00m():
    >       [94massert[39;49;00m inc([94m3[39;49;00m) == [94m5[39;49;00m
    [1m[31mE       assert 4 == 5[0m
    [1m[31mE        +  where 4 = inc(3)[0m
    
    [1m[31mtest_sample.py[0m:7: AssertionError
    =========================== short test summary info ============================
    FAILED test_sample.py::test_answer - assert 4 == 5
    [31m============================== [31m[1m1 failed[0m[31m in 0.10s[0m[31m ===============================[0m


contents of [test_sysexit.py](test_sysexit.py)


```python
# content of test_sysexit.py
import pytest
def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()
```


```python
# Execute the test function with “quiet” reporting mode:
!pytest -q test_sysexit.py
```

    [32m.[0m[32m                                                                        [100%][0m
    [32m[32m[1m1 passed[0m[32m in 0.02s[0m[0m


## Group multiple tests in a class

Once you develop multiple tests, you may want to group them into a class. pytest makes it easy to create a class containing more than one test.

pytest discovers all tests following its Conventions for Python test discovery, so it finds both test_ prefixed functions. There is no need to subclass anything. We can simply run the module by passing its filename:

contentx of [test_class.py](test_class.py)


```python
# content of test_class.py
class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
```


```python
!pytest -q test_class.py
```

    [32m.[0m[31mF[0m[31m                                                                       [100%][0m
    =================================== FAILURES ===================================
    [31m[1m______________________________ TestClass.test_two ______________________________[0m
    
    self = <test_class.TestClass object at 0x7fafb0d4ec70>
    
        [94mdef[39;49;00m [92mtest_two[39;49;00m([96mself[39;49;00m):
            x = [33m"[39;49;00m[33mhello[39;49;00m[33m"[39;49;00m
    >       [94massert[39;49;00m [96mhasattr[39;49;00m(x, [33m'[39;49;00m[33mcheck[39;49;00m[33m'[39;49;00m)
    [1m[31mE       AssertionError: assert False[0m
    [1m[31mE        +  where False = hasattr('hello', 'check')[0m
    
    [1m[31mtest_class.py[0m:9: AssertionError
    =========================== short test summary info ============================
    FAILED test_class.py::TestClass::test_two - AssertionError: assert False
    [31m[31m[1m1 failed[0m, [32m1 passed[0m[31m in 0.08s[0m[0m


## Request a unique temporary directory for functional tests¶

pytest provides Builtin fixtures/function arguments to request arbitrary resources, like a unique temporary directory:

contents of [test_tmpdir.py](test_tmpdir.py)


```python
# content of test_tmpdir.py
def test_needsfiles(tmpdir):
    print(tmpdir)
    assert 0
```


```python
!pytest -q test_tmpdir.py
```

    [32m.[0m[32m                                                                        [100%][0m
    [32m[32m[1m1 passed[0m[32m in 0.03s[0m[0m


You can use the tmp_path fixture which will provide a temporary directory unique to the test invocation, created in the base temporary directory.

contents of [test_tmppath.py](test_tmppath.py)


```python
# content of test_tmp_path.py
import os

CONTENT = u"content"


def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(CONTENT)
    assert p.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 1
```


```python

```
