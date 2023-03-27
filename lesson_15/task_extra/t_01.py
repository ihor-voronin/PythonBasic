def add(n):
    pass


# def __call__
# class int|float

if __name__ == "__main__":
    assert add(1) == 1
    assert add(1)(2) == 3
    assert add(1)(2)(3) == 6
