from functools import reduce

def add(*args):
    return reduce(lambda x, y: x + y, args)


def subtract(*args):
    return reduce(lambda x, y: x - y, args)