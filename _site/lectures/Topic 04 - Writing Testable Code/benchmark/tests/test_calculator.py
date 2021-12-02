import random
from functools import reduce
import calculator


def test_add():
    numbers = [random.random() for i in range(100000)]
    expected = sum(numbers)
    actual = calculator.add(*numbers)
    assert expected == actual


def test_subtract():
    numbers = [random.random() for i in range(100000)]
    expected = reduce(lambda x, y: x - y, numbers)
    actual = calculator.subtract(*numbers)
    assert expected == actual


def test_benchmark_add(benchmark):
    numbers = [random.random() for i in range(10000)]
    benchmark(calculator.add, *numbers)


def test_benchmark_subtract(benchmark):
    numbers = [random.random() for i in range(10000)]
    benchmark(calculator.subtract, *numbers)
