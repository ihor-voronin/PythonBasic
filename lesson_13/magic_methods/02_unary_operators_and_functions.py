# __pos__(self)	To get called for unary positive e.g. +someobject.
# __neg__(self)	To get called for unary negative e.g. -someobject.
# __abs__(self)	To get called by built-in abs() function.
# __invert__(self)	To get called for inversion using the ~ operator.
# __round__(self,n)	To get called by built-in round() function.
# __floor__(self)	To get called by built-in math.floor() function.
# __ceil__(self)	To get called by built-in math.ceil() function.
# __trunc__(self)	To get called by built-in math.trunc() function.
from math import floor


class MyClass:
    def __pos__(self):
        print("call pos")
        return 1

    def __neg__(self):
        print("call neg")
        return 2

    def __abs__(self):
        print("call abs")
        return 3

    def __invert__(self):
        print("call invert")
        return 4

    def __round__(self, n=None):
        print("call round")
        return 5

    def __floor__(self):
        print("call floor")
        return 6


if __name__ == "__main__":
    instance = MyClass()
    print(+instance)
    print(-instance)
    print(abs(instance))  # |-5| = 5
    print(~instance)
    print(round(instance))
    print(floor(instance))
