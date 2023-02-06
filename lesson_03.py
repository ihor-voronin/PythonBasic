# Arithmetic Operators
# **
# +
# -
# *
# /
# %
# //

# Comparison Operators
a = 7
b = 9
# >
print(a > b)
# <
print(a < b)
# ==
print(a == 7)
print("int and str", 7 == "7")

print("6==7", 6 == 7)
print("8==8", 8 == 8)
# !=
print("a!=7", a != 7)
print("6!=7", 6 != 7)
print("8!=8", 8 != 8)
# >=
print("7 >= 7", 7 >= 7)
print("7 > 7", 7 > 7)
print("8 >= 7", 8 >= 7)
# <=
print("7 <= 7", 7 <= 7)
print("7 < 7", 7 < 7)

# Logical Operators
# and  True+True = True True+False=False False+True=False False+False=False
print("7 > 6 AND 4 > 5", (7>6) and (4>5))
print("7 < 6 AND 4 > 5", (7<6) and (4>5))
print("7 < 6 AND 4 < 5", (7<6) and (4<5))
print("7 > 6 AND 4 < 5", (7>6) and (4<5))
# or True+True=True True+False=True False+True=True False+False=False
print("7 > 6 OR 4 > 5", (7>6) or (4>5))
print("7 < 6 OR 4 > 5", (7<6) or (4>5))
print("7 < 6 OR 4 < 5", (7<6) or (4<5))
print("7 > 6 OR 4 < 5", (7>6) or (4<5))
# not not+True = False not+False=True
print("NOT 4 > 5", not (4>5))
print("5 > 4", 5 > 4)
# user == admin and user == staff
# not (user == client)
# user != client

# Bitwise Operators
# &
print("10 & 1", 10 & 1)
# |
# ~
# ^
# >>
# <<

# Assignment Operators
# =
a = 0
# +=
a = 10
a += 1  # a = a + 1
print("a += 1", a)
a = 10
a += 10 # a = a + 10
print("a += 10", a)
# -=
a = 0
a -= 1  # a = a - 1
print("a -= 1", a)
a = 0
a += 10 # a = a + 10
print("a -= 10", a)
# a *= 4   a = a * 4
# a /= 4   a = a / 4
# a %= 4   a = a % 4
# a **= 4  a = a ** 4
a = 2
a **= 4
print(a)
# &=
# |=
# ^=
# >>=
# <<=

# Identity Operators
# is
a = "1"
b = 1
print("int and str", a is b)
print("int and str", "1" == 1)
print("type of a is str:", type(a) is str)
print("a is str:", a is str)
a = 1000
b = 1000
b += 1
b -= 1
print("id(a)", id(a))
print("id(b)", id(b))
print("a =", a)
print("b =", b)
print("a is b", a is b)
print("a == b", a == b)
#  is not
print("type of a is not str: ", type(a) is not str)

# Membership Operators
# in
a = [1,2,3,4]
print("3 in list", 3 in a)
b = "Hello world"
print("letter in str", "l" in b.lower())
# not in
print("letter in str", "t" not in b.lower())
print("letter in str", "l" not in b.upper())
print("3 in list", 13 not in a)

# if <condition>:
#   <operand 1>
#   <operand 2>
#   ...
#   <operand N>

a = 1
if a>5:
    a += 20
    a += 2

# if <condition>:
#   <operand 1>
#   <operand 2>
#   ...
#   <operand N>
# else:
#   <operand 1>

# a = input("input letter:")
#
# if a == "a" and a == "1":
#     print(a, "== a")
# else:
#     print(a, "!= a")

# if <condition>:
#   <operand 1>
#   <operand 2>
#   ...
#   <operand N>
# elif <condition>:
#   <operand>
# else:
#   <operand 1>

num_1 = 198
num_2 = 317
# operator = input("input operator:")
# if operator == "+":
#     print(num_1 + num_2)
# elif operator == "-":
#     print(num_1 - num_2)
# else:
#     print("not operator")
#
# if num_1 == 40**10:
#     print("ops")
# print(num_1)



# while <condition>:
#   <operand 1>
#   <operand 2>
#   ...
#   <operand N>

print(" while loop\n\n")
counter = 0

while counter < 3:
    print(counter)
    counter += 1

print("\n\n")
# counter = 0
# 0<3 -> print 0+1=1
# 1<3 -> print 1+1=2
# 2<3 -> print 2+1=3
# 3<3 -> end

# while <condition>:
#   <operand while>
# else:  -> виконується по завершенню while
#   <operand else>
#
counter = 4

while counter < 3:
    print(counter)
    counter += 1
else:
    print("loop finished")

# break

print("\n\nWhile break\n\n")
counter = 4
while True:
    counter += 1
    pow_2 = 2 ** counter
    if pow_2 == 64:
        print("counter", counter)
        break

# counter = 4
# True -> 4+1=5  pow_2=2**5=32   32 == 64 -> not
# True -> 5+1=6  pow_2=2**6=64   64==64 -> print counter    break

# 5! = 1*2*3*4*5 = 120
# 6! = 1*2*3*4*5*6

factorial_value = 1  # start value
counter = 1  # start counter

factorial_num = 5

while counter <= 5:
    factorial_value *= counter
    counter += 1

print("factorial value", factorial_value)

# factorial_value = 1
# counter = 1
# factorial_value * counter = 1* 1 = 1
# counter = counter + 1 = 2
# factorial_value * counter = 1 * 2 = 2
# counter = counter + 1 = 3
# factorial_value * counter = 2 * 3 = 6
# counter = counter + 1 = 4
# factorial_value * counter = 6 * 4 = 24
# counter = counter + 1 = 5
# factorial_value * counter = 24 * 5 = 120
# counter = counter + 1 = 6

# while 1 == 1:  # equal while True:
#     print('1==1')

print("while continue")

counter = 0
while counter < 10:
    counter += 1
    if (counter % 2) == 0:  # 2 4 6 8 10 ...
        continue
    print("counter", counter)
    # if (counter % 2) != 0:
    #     print("counter", counter)


# 0<10 -> 0+1=1  if->X   print
# 1<10 -> 1+1=2  if->continue
# 2<10 -> 2+1=3  if->X   print
