from functools import reduce
import time

def add(*args):
    return reduce(lambda x, y: x + y, args)


def subtract(*args):
    time.sleep(3) # intentinally slowing code down so we can see it on the benchmark test
    return reduce(lambda x, y: x - y, args)