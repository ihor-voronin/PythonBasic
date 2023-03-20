def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner


@star
@percent
def printer(msg):
    print(msg)


# printer("hello world")

@percent
@star
def printer2(msg):
    print(msg)


printer2("hello world")

def printer3(msg):
    print(msg)


# printer3("hello world")
