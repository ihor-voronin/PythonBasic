# __new__(cls, other)	To get called in an object's instantiation.
# __init__(self, other)	To get called by the __new__ method.
# __del__(self)	Destructor method.


class MyClass:

    def __new__(cls, *args, **kwargs):
        print("call new")
        # custom conditions
        return super().__new__(cls)

    def __init__(self):
        print("call init")

    def __del__(self):
        print("call del")


if __name__ == "__main__":
    instance = MyClass()
    del instance
