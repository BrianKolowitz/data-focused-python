---
layout: default
title: 09 - Testing for Performance Degradation Between Changes
parent: Topic 04 - Writing Testable Code
grand_parent: Lectures
nav_order: 9
---
# Testing for Performance Degradation Between Changes
[Source](https://realpython.com/python-testing/)

There are many ways to benchmark code in Python. The standard library provides the `timeit` module, which can time functions a number of times and give you the distribution. This example will execute `test()` 100 times and `print()` the output:


```python
import random
from functools import reduce
    
def add(numbers):
    total = reduce(lambda x, y: x + y, numbers)
    return total

if __name__ == '__main__':
    import timeit
    numbers = [random.random() for i in range(100000)]
    print(timeit.timeit(f"add({numbers})", setup="from __main__ import add", number=100))
```

    0.5682077080000454


Another option, if you decided to use pytest as a test runner, is the pytest-benchmark plugin. This provides a pytest fixture called benchmark. You can pass benchmark() any callable, and it will log the timing of the callable to the results of pytest.

You can install pytest-benchmark from PyPI using pip:

```bash
pip install pytest-benchmark
```

Then, you can add a test that uses the fixture and passes the callable to be executed:

```python
def test_my_function(benchmark):
    result = benchmark(test)
```

More information is available at the [Documentation Website](https://pytest-benchmark.readthedocs.io/en/latest/)

See the `benchmark` folder for a runnable example.


```python

```
