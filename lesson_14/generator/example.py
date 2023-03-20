class PowTwo:
    def __init__(self, max_value=0):
        self.max_value = max_value
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max_value:
            raise StopIteration()

        result = 2 ** self.n
        self.n += 1
        return result


def pow_two_gen(max_value=0):
    n = 0
    while n < max_value:
        yield 2 ** n
        n += 1


if __name__ == "__main__":
    # for k in PowTwo(10):
    #     print("ClassGenerator:", k)
    # print()

    for k in pow_two_gen(10):
        print("ClassGenerator:", k)
    print()
