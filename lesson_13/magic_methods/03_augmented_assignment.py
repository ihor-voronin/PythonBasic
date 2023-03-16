# __iadd__(self, other)	To get called on addition with assignment e.g. a +=b.
# __isub__(self, other)	To get called on subtraction with assignment e.g. a -=b.
# __imul__(self, other)	To get called on multiplication with assignment e.g. a *=b.
# __ifloordiv__(self, other)	To get called on integer division with assignment e.g. a //=b.
# __idiv__(self, other)	To get called on division with assignment e.g. a /=b.
# __itruediv__(self, other)	To get called on true division with assignment
# __imod__(self, other)	To get called on modulo with assignment e.g. a%=b.
# __ipow__(self, other)	To get called on exponentswith assignment e.g. a **=b.
# __ilshift__(self, other)	To get called on left bitwise shift with assignment e.g. a<<=b.
# __irshift__(self, other)	To get called on right bitwise shift with assignment e.g. a >>=b.
# __iand__(self, other)	To get called on bitwise AND with assignment e.g. a&=b.
# __ior__(self, other)	To get called on bitwise OR with assignment e.g. a|=b.
# __ixor__(self, other)	To get called on bitwise XOR with assignment e.g. a ^=b.

class MyClass:
    def __iadd__(self, other):
        print("call __iadd__")
        print(other)
        return other

    def __ilshift__(self, other):
        print("call __ilshift__")
        print(other)
        return other

    def __imul__(self, other):
        print("call __imul__")
        print(other)
        return other


if __name__ == "__main__":
    instance = MyClass()
    instance2 = MyClass()

    instance2 += instance
    instance2 <<= instance
    instance2 *= instance
