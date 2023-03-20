# Pattern Iterable
class FirstN:
    def __init__(self, numbers=None):
        self.numbers = numbers or []
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.current < len(self.numbers):
            cur = self.numbers[self.current]
            self.current += 1
            return cur
        raise StopIteration()


class First3Letters:
    def __init__(self, string=None):
        self.string = string or ''
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.current < len(self.string):
            cur = self.string[self.current: min(self.current+3, len(self.string))]
            self.current += 3
            return cur
        raise StopIteration()


if __name__ == "__main__":
    sum_of_first_n = sum(FirstN([1, 10, 20, 30, 40]))
    list_first_n = list(FirstN([1, 10, 20, 30, 40]))
    print(sum_of_first_n)
    print(list_first_n)

    for i in FirstN([1, 10, 20, 30, 40]):
        print(i)

    for i in First3Letters("123abc567dfg22"):
        print(i)
