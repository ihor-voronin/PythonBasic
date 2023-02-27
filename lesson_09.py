# pass statement

# pass <==> ...

result = 0
for i in range(10):
    pass

for i in range(10):
    ...


def my_func(num):
    pass


def my_func2(num):
    ...


# print(result)
# print(my_func(8))
# print(my_func2(8))


def write(text):
    pass


def change_inc(color, count):
    pass


# exception

# a = [1, 2]
# print(a[3])

# b = {1:2, 2:3}
# b[4]

def div(num1, num2):
    # raise Exception
    # raise Exception("zero division")
    if type(num2) == str:
        raise AttributeError("num2 must be int or float")
    if type(num2) == bool:
        raise AttributeError
    if num2 == 0:
        raise ZeroDivisionError("zero division")
    return f"{num1} / {num2}"


# raise Exception  # default exception
# raise Exception("default exception")  # default exception

# print(div(2, True))

# raise <exception>
# raise ArithmeticError
# raise <exception>(<message>)
# raise KeyError("message")


# try:
#     <code1 with exception>
# except [optional exception]:
#     <code2 if exception in code1>
# else:
#     <code3 if in code1 no errors>
# finally:
#     <code4 executed after code1, code2 or code3, but before uncaught exception>


def divide(x, y):
    try:
        res = x / y
        print("result is", res)
    except ZeroDivisionError:  # caught only ZeroDivisionError
        print("cannot divide")

def divide2(x, y):
    try:
        res = x / y
        print("result is", res)
    except:  # caught all errors
        print("cannot divide")

def divide3(x, y):
    try:
        res = x / y
        print("result is", res)
    except Exception:  # caught all errors
        print("cannot divide")

def divide4(x, y):
    try:
        res = x / y
        print("result is", res)
    except Exception as exc:  # caught all errors
        print(exc, "cannot divide")


def divide5(x, y):
    try:
        res = x / y
        print("result is", res)
    except (ZeroDivisionError, AttributeError) as exc:  # caught all errors
        print(exc, "cannot divide")

def divide6(x, y):
    try:
        res = x / y
    except (ZeroDivisionError, AttributeError) as exc:  # caught all errors
        print(exc, "cannot divide")
    else:
        print("result is", res)

    print("something")

def divide7(x, y):
    try:
        # code1
        res = x / y
    except (ZeroDivisionError, AttributeError, TypeError) as exc:  # caught all errors
        # code2
        print(exc, "cannot divide")
    else:
        # code3
        print("result is", res)
    finally:
        # after code1, code2, code3 but before uncaught error
        print("execute finally code")

    print("something")


divide(2, 1)

divide(2, 0)
divide2(2, 0)
divide3(2, 0)
divide4(2, 0)
divide5(2, 0)
print("divide6")
divide6(2, 0)
divide6(2, 1)

print("\ndevide7")
divide7(2, 1)
print()
divide7(2, 0)
print()
divide7("2", "1")

print("after exception")

# num = 0
# while num <= 0:
#     try:
#         num = int(input("input number bigger then 0:"))
#     except ValueError as my_exc:
#         print("incorrect number", my_exc)


#  5! = 1*2*3*4*5  =120

num = 1
result = 1
while num <= 5:
    result *= num
    num += 1


print("while factorial", result)

result = 1
for i in range(1, 6):
    result *= i

print("for factorial", result)

def factorial(num):
    if num == 1:
        return num
    return num * factorial(num-1)


print("recursion factorial", factorial(5))

# factorial(5)
# 5 == 1  -x-> false
# 5 * factorial(5-1)  => 5 * factorial(4)
# 4 == 1  -x-> false
# 4 * factorial(4-1)  => 5 * 4 * factorial(3)
# 3 == 1  -x-> false
# 3 * factorial(3-1)  => 5 * 4 * 3 * factorial(2)
# 2 == 1  -x-> false
# 2 * factorial(2-1)  => 5 * 4 * 3 * 2 * factorial(1)
# 1 == 1  --> True => return 1

# 1 * 2 * 3 * 4 * 5

def countdown(n):
    if n == 0:
        print("KABOOM")
    else:
        print(n)
        countdown(n-1)


countdown(10)
# countdown(10) -> print(10) -> countdown(9) -> print(9) -> ... -> countdown(1) -> print(1) -> countdown(0) -> print("KABOOM")


def infinity_countdown(n):
    print(n)
    infinity_countdown(n-1)
    # try:
    #     infinity_countdown(n-1)
    # except RecursionError:
    #     print("KABOOM")


import sys

print("setrecursionlimit", sys.setrecursionlimit(2000))

print("getrecursionlimit", sys.getrecursionlimit())

# print("infinity_countdown")
# infinity_countdown(10)

string = "helo hi ho"
symbol = "h"

def find_index(string_line, symb, start_index=0):
    if string_line == "":
        return

    if string_line[0] == symb:
        print("found symbol", symb, "with index", start_index)

    find_index(string_line[1:], symb, start_index=start_index+1)


print("execute find_index")
find_index(string, symbol)

# "helo hi ho", "h" start_index=0
# string_line[0] == symb => h == h -> print
# find_index("elo hi ho", "h", start_index=1)
# string_line[0] == symb => e == h -x-> False
# find_index("lo hi ho", "h", start_index=2)
# string_line[0] == symb => l == h -x-> False
# find_index("o hi ho", "h", start_index=3)
# string_line[0] == symb => o == h -x-> False
# find_index(" hi ho", "h", start_index=3)
# string_line[0] == symb => ' ' == h -x-> False
# .....
# find_index("o", "h", start_index=9)
# string_line[0] == symb => 'o' == h -x-> False
# find_index("", "h", start_index=10)
# string_line == "" => "" == "" -> return

# try:
#     infinity_countdown(10)
# except RecursionError:
#     print("recursion limit")

# infinity_countdown(10)
