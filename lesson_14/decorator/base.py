# nested function
def outer(x):
    print("x", x)
    def inner(y):
        print("y", y)
        return x + y
    return inner


add_five = outer(5)

def inner_2(y):
    print("y", y)
    return 5 + y

print("add_five variable", add_five)
result = add_five(6)
def inner_3(y):
    print("y", 6)
    return 5 + 6

print("nested function", result)
print("nested function", outer(5)(7))


# Pass Function as Argument
def add(x, y):
    return x + y
def minus(x, y):
    return x - y
def calculate(func, x, y):
    return func(x, y)

result = calculate(add, 4, 6)
result2 = calculate(minus, 4, 6)
print("Pass Function as Argument", result)
print("Pass Function as Argument", result2)


# Return a Function as a Value
def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello


#
greet = greeting("Atlantis")
#
def hello():
    return "Hello, " + "Atlantis" + "!"

print("Return a Function as a Value", greet())
