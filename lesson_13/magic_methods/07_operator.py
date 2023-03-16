# __add__(self, other)	To get called on add operation using + operator
# __sub__(self, other)	To get called on subtraction operation using - operator.
# __mul__(self, other)	To get called on multiplication operation using * operator.
# __floordiv__(self, other)	To get called on floor division operation using // operator.
# __truediv__(self, other)	To get called on division operation using / operator.
# __mod__(self, other)	To get called on modulo operation using % operator.
# __pow__(self, other[, modulo])	To get called on calculating the power using ** operator.
# __lt__(self, other)	To get called on comparison using < operator.
# __le__(self, other)	To get called on comparison using <= operator.
# __eq__(self, other)	To get called on comparison using == operator.
# __ne__(self, other)	To get called on comparison using != operator.
# __ge__(self, other)	To get called on comparison using >= operator.
from random import randint


class MyClass:
    def __init__(self):
        self.a = randint(0, 10)

    def __add__(self, other):
        print("call __add__")
        self.a += other
        return self.a

    def __lt__(self, other):
        print("call __lt__")
        return self.a < other


if __name__ == "__main__":
    instance = MyClass()
    print("a", instance.a)
    print(instance + 2)

    print("a", instance.a)
    print(instance < 2)
