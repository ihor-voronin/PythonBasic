def decorator_name(func):
    # визначення внутрішньої функції
    def inner():
        # додатковий код перед декоруємою функцією
        print("I got decorated")

        # виконання оригінальної функції
        func()

    # return внутрішньої функції
    return inner


# визначення окремої функції, яку будемо "декорувати"
def ordinary():
    print("I am ordinary")

# декоруємо функцію
decorated_func = decorator_name(ordinary)

# виконуємо задекоовану функцію
print("decorate by pass as arg")
decorated_func()
print()


def decorator_name2(func):
    def inner():
        print("I got decorated2")
        func()
    return inner

@decorator_name2
def ordinary2():
    print("I am ordinary2")


# decorated_func = make_pretty2(ordinary2)
#
print("decorated by @")
ordinary2()
print()
# decorated_func()
# print()

def divide(a, b):
    return a/b


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)


print("decorate with args")
divide(2, 5)
divide(2, 0)
print()


def logging(func):
    def inner(a, b):
        print(f"Execute func {func.__name__} with param {a}, {b}")
        return func(a, b)
    return inner

@logging
def divide(a, b):
    print(a/b)


print(divide(7, 3))