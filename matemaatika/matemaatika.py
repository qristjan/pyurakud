import functools


def liida(*numbrid):
    return functools.reduce(lambda x, y: x + y, numbrid)


def korruta(*numbrid):
    return functools.reduce(lambda x, y: x * y, numbrid)
