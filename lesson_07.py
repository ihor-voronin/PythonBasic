# Functions

print()
# <function_name>([args])
# len()
# range()

#
# def <function_name>([optional arguments]):
#    <codeblock of function with <function_name>>


def new_function():
    print("hello world")


new_function()
new_function()
new_function()

# required args
# def <function_name>(arg1, arg2, ... argN):
def new_function_2(num1, num2):
    print("multiply", num1 * num2)


new_function_2(10, 2)
new_function_2(20, 3)

# def <function_name>(arg1=default_value1, arg2=default_value2, ... ):

# 5! = 1*2*3*4*5 = 120
# 6! = 1*2*3*4*5*6 = 720
# 2! = 1*2 = 2


def factorial(num=5):
    result = 1
    for i in range(1, num + 1):
        result *= i
    print("factorial of", num, "is", result)


factorial(5)
factorial(6)
factorial()

# def <function_name>(required_arg1, required_arg2 ... , arg1=default_value1, arg2=default_value2, ...):


def calculator(num1, num2, sign="+"):
    if sign == "+":
        print("sum", num1 + num2)
    elif sign == "-":
        print("diff", num1 - num2)
    else:
        print(sign, "is incorrect")


calculator(10, 5, "-")

calculator(num1=20, num2=10, sign="+")
calculator(num2=10, sign="+", num1=20)
calculator(10, 20, sign="-")
calculator(10, num2=10, sign="-")
calculator(10, sign="-", num2=10)

print("hello world", "hi", 5, 1, True, "No", end="hi\n", sep="|")

# def <function_name>(*args, **kwargs):


def custom_print(*args):
    print("args in function", args)
    for arg in args:
        print("arg:", arg)


custom_print("hello world", "hi", 5, 1, True, "No")


def custom_print2(*args, log_level="INFO", end="\n", sep=" "):
    # <sting>.join("iterable")
    new_string = log_level
    new_string += sep.join([str(arg) for arg in args])
    new_string += end
    print(new_string)


custom_print2(" hello world", "hi", 5, 1, True, "No", sep="\t", end=" it's end\n", log_level="ERROR")

# def <function_name>(**kwargs>):


def custom_kwargs(**kwargs):
    print(kwargs)


custom_kwargs(num1=1, num2=10, num3=15)

count_of_elements = len([1, 2, 3])
print(count_of_elements)


# def <function_name>(<args>, <args with default value>, *args, **kwargs):
#   return <value>


def calculator(num1, num2, sign="+"):
    # return 200
    if sign == "+":
        return num1 + num2
    elif sign == "-":
        return num1 - num2
    else:
        return


value = calculator(1, 2, "+")
value2 = calculator(1, 2, "*")
print("calculator result", value2)


def calculator(num1: int, num2: int, sign: str = "+") -> int:
    # return 200
    if sign == "+":
        return num1 + num2
    elif sign == "-":
        return num1 - num2
    else:
        return 0


value = calculator(20, 26, "-")  # 20 - 26
print(value)

# if <condition>:
#    var = 2
#    <code>
# else:
#    print(var)
#    <code>

a = 1
b = 2
if a < b:
    # region 1
    c = 10
    if True:
        # region 1.1
        print("c var", c)
else:
    # region 2
    print("c var", c)

# global <variable name>
a = 20
def my_func():
    global d
    d = 15
    print("my_func", d)

def my_func_2():
    print("my_func_2", d)

my_func()
my_func_2()

def my_func_3(var=[]):
    var.append(1)
    print("my_func", var)

my_func_3()
my_func_3()


def func1():
    print()


# if __name__ == "__main__":
    # print(1)



# lambda <arguments> : <expression>

multiplier = lambda num: num * num
print("multiplier", multiplier(3))
def multiplier(num):
    return num * num
print("multiplier", multiplier(3))


multiplier2 = lambda num1, num2=1: num1 * num2
print("multiplier2", multiplier2(3))
def multiplier2(num1, num2=1):
    return num1 * num2
print("multiplier2", multiplier2(3))


list_str = ["hi", "on", "in", "at"]
def capitalize(str_var):
    return str_var.upper()

print(capitalize("hello"))

# map(<function>, <iterables>)

print(list(map(capitalize, list_str)))
# capitalize("hi") - > "HI"
# capitalize("on") - > "ON"
# capitalize("in") - > "IN"
# capitalize("at") - > "AT"
# --> ['HI', 'ON', 'IN', 'AT']
for var in map(capitalize, list_str):
    print(var)

print(list(map(lambda str_var: str_var.upper(), list_str)))

# filter(function, iterable)

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

# adults = filter(myFunc, ages)
# 5 -> 5 < 18 -> False
# 12 -> 12 < 18 -> False
# 17 -> 17 < 18 -> False
# 18 -> 18 < 18 -> True
# 24 -> 24 < 18 -> True
# 32 -> 32 < 18 -> True

adults = filter(lambda x: False if x < 18 else True, ages)

for x in adults:
  print(x)


list_continent = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
list1 = [
  { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' },
  { 'firstName': 'Agustín', 'lastName': 'M.', 'country': 'Chile', 'continent': 'Americas', 'age': 37, 'language': 'C' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
  { 'firstName': 'Laia', 'lastName': 'P.', 'country': 'Andorra', 'continent': 'Europe', 'age': 55, 'language': 'Ruby' },
  { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 65, 'language': 'PHP' }
]

def developer_processing(list_developers: list, list_continents: list) -> bool:
    developers_continents = [dev['continent'] for dev in list_developers]
    return set(list_continents) == set(developers_continents)

print(developer_processing(list1, list_continent))
