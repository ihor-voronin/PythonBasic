def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging


@logged
def f(x):
    """does some math"""
    return x + x * x


print("Base decorator")
print("__name__", f.__name__)
print("__doc__", f.__doc__)
print(f(10))


from functools import wraps


def logged2(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging


@logged2
def f2(x):
    """does some math"""
    return x + x * x


print()
print("Decorator with wraps")
print("__name__", f2.__name__)
print("__doc__", f2.__doc__)
print(f2(10))
