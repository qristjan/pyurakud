import functools


def liida(*numbrid):
    return functools.reduce(lambda x, y: x + y, numbrid)
