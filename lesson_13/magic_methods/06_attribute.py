# __getattr__(self, name)	Is called when the accessing attribute of a class that does not exist.
# __setattr__(self, name, value)	Is called when assigning a value to the attribute of a class.
# __delattr__(self, name)	Is called when deleting an attribute of a class.


class MyClass:
    def __getattr__(self, name):
        print("call __getattr__")
        return "__getattr__"

    def __setattr__(self, name, value):
        print("call __setattr__")
        return "__setattr__"

    def __delattr__(self, name):
        print("call __delattr__")
        return "__delattr__"


if __name__ == "__main__":
    instance = MyClass()
    print(instance.x)
    instance.y = 2
    print("y", instance.y)
    del instance.y

    print("getattr", getattr(instance, "x", False))