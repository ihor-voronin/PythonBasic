if __name__ == "__main__":
    list_of_nums = [1, 10, 20, 30, 40]
    my_iterator = iter(list_of_nums)
    print(my_iterator)

    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))

    print("do something")
    for i in my_iterator:
        print(i)
