import sys

print("hello world", "sdsa", "hi", 12, 23.5, False, sep='-', end='\n\n')
print("text")

a = 28883
PI = 3.14
print(PI)
print(id(a))

a = "text"
PI = 4
print(PI)
print(id(a))

print(a, type(a))
print(PI, type(PI))

_variable = 1
variable = 2
variable2 = 3

var_1 = 124
var_2 = 45.6

# + - * / % ** //
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print("modulus", 10 % 3)  # 10 - 3 = 7 -3 = 4 - 3 = 1
print(10 ** 3)
print(10 // 3)

user = 17
count_avatars = 5
print("Avatar_id", user % count_avatars)
print("Iteration", user // count_avatars)

var_3 = "text in var"
var_4 = " another text"

print(var_3)

a = "2"
b = int(a)
c = float(a)
print(a, type(a))
print(b, type(b))
print(c, type(c))

# not_num = "-"
# int(not_num)
# int() float() str()

new_value = int(input("type num: "))
print("new Value:", new_value)
print(new_value, type(new_value))

new_value2 = int(input("type num2: "))
new_value2 = int(input("type num3: "))

var_6 = 678
new_str = str(var_6)
