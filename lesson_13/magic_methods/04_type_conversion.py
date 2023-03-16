# __int__(self)	To get called by built-int int() method to convert a type to an int.
# __float__(self)	To get called by built-int float() method to convert a type to float.
# __complex__(self)	To get called by built-int complex() method to convert a type to complex.
# __oct__(self)	To get called by built-int oct() method to convert a type to octal.
# __hex__(self)	To get called by built-int hex() method to convert a type to hexadecimal.
# __index__(self)	To get called on type conversion to an int when the object is used in a slice expression.


class MyClass:
    def __int__(self):
        print("call __int__")
        return 1

    def __float__(self):
        print("call __float__")
        return 2.0


if __name__ == "__main__":
    instance = MyClass()
    print(
        int(instance)
    )
    print(float(instance))