# Pattern Iterable
class FirstN(object):
    def __init__(self, n):
        self.n = n
        self.num = 0

    # дає змогу отримувати поточне значення
    def __iter__(self):
        print("__iter__")
        return self

    # даж змогу отримувати наступне значення
    def __next__(self):
        print("__next__")
        return self.next()

    def next(self):
        if self.num < self.n:
            cur = self.num
            print("cur", cur)
            self.num += 1
            print("self.num", self.num)
            # cur, self.num = self.num, self.num+1
            return cur

        print("self.num", self.num)
        print("Iteration stop")
        raise StopIteration()


if __name__ == "__main__":
    # sum_of_first_n = sum(FirstN(10))
    # list_first_n = list(FirstN(10))
    # print(sum_of_first_n)
    # print(list_first_n)
    # print(FirstN(10))
    # for i in FirstN(10):
    #     print(i)

    # my_generator = FirstN(10)
    # for i in my_generator:
    #     print(i)
    #
    # for i in my_generator:
    #     print(i)

    my_generator2 = FirstN(4)
    # my_generator2 = iter(range(4))
    print(next(my_generator2))
    print(next(my_generator2))
    print(next(my_generator2))
    print(next(my_generator2))
    print(next(my_generator2))