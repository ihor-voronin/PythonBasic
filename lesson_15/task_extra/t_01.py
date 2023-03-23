def add(n):
    pass


if __name__ == "__main__":
    assert add(1) == 1
    assert add(1)(2) == 3
    assert add(1)(2)(3) == 6
