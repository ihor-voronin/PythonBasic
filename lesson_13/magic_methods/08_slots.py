class Example:
    """
    my example class
    """
    __slots__ = ("slot_0", "slot_1")

    def __init__(self) -> None:
        self.slot_0 = "zero"
        self.slot_1 = "one"
        # self.slot_2 = "two"


if __name__ == "__main__":
    x1 = Example()
    print(x1.slot_0)
    print(x1.slot_1)
    print(x1.__dir__())
    print(x1.__doc__)
    print(x1.__module__)
    # print(x1.__annotations__)
    # print(x1.__dict__)
    # print(x1.__dict__.keys())
    # print(x1.__dict__.values())
