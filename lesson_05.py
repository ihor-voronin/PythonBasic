a = []
a = list()

b = [1, True, "Hello"]

print(id(b))

b.append(2)

print(id(b))

c = "Hello world"

print(id(c))

c += "one"

print(id(c))

list_num = [1, 2, 3]

# while True:
#     num = int(input("input int:"))
#     if num == 0:
#         break
#     list_num.append(num)
#
# print(list_num)

# append
list_num.append(True)
list_num.append("True")
print(list_num)

# operator +
list_num = list_num + [False]
print(list_num)


list_num = list_num + ["False"] + [99]
list_num = list_num + [5, 6, 7]
print(list_num)

list_num += [[1,2,3], [True, False]]
print(list_num)

matrix = [[1,2,3], [4,5,6], [7,8,9]]
#  1 2 3
#  4 5 6
#  7 8 9

list_char = list("Hello world")
print("list char", list_char)

print("list range", list(range(1,10)))

string_num = "123456789"
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#           0  1  2  3  4  5  6  7  8
#                         -4 -3 -2 -1

print("list_num 5 element", list_num[5], string_num[5])
print("list_num 8 element", list_num[8], string_num[8])
print("list_num -1 element", list_num[-1], string_num[-1])
string_num += "0"
list_num += [10]
print("list_num 8 element", list_num[8], string_num[8])
print("list_num -1 element", list_num[-1], string_num[-1])
#                 0         1        2
#                0 1 2    0 1 2    0 1 2
list_in_list = [[1,2,3], [4,5,6], [7,8,9]]
print("list_in_list", list_in_list[1][1])
print("list_in_list", list_in_list[2][0])

list_in_list.append("test")
list_in_list[1].append(10)
print("list_in_list", list_in_list)
#                 0             1                  2
#                         0 1       2
#                                  0      1
#                                0   1
#                                    0
list_in_list = [[1,2,3], [4,5, [[9, [2]], 5]], [7,8,9]]
print("list_in_list", list_in_list)
print("list_in_list", list_in_list[1])
print("list_in_list", list_in_list[1][2])
print("list_in_list", list_in_list[1][2][0])
print("list_in_list", list_in_list[1][2][0][1])
print("list_in_list", list_in_list[1][2][0][1][0])


string_num = "123456789"
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("string", string_num[::2])
print("list_num", list_num[::2])

print("string 3:end", string_num[3:])
print("list_num 3:end", list_num[3:])
print("string_num", string_num)
print("list_num", list_num)
string_num += "0"
list_num += [10]
print("string 3:end", string_num[3:])
print("list_num 3:end", list_num[3:])

# list_num[3:] = [1, 2]
list_num[::2] = [1, 1, 1, 1, 1]
print(list_num)

new_list = []
# append(x)
new_list.append(1)
new_list += [2]
new_list[len(new_list):] = [3]
print("append new list", new_list)

# len                               8
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("len list", len(list_num))
list_num[len(list_num):] = [10]
print("list slice append", list_num)

# extend
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_num.extend([10, 11, 12])
print("extend list_num", list_num)
list_num = list_num + [13, 14, 15]
print("+ list_num", list_num)
list_num[len(list_num):] = [16, 17, 18]
print("slicing list_num", list_num)

print(list_num[len(list_num) - 1])
print(list_num[17])
print(list_num[-1])

# insert(i, x)
#           0  1  2  3  4  5  6  7  8
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_num.insert(4, 10)
print("insert list_num", list_num)
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("len list_num", len(list_num))
list_num.insert(len(list_num), 11)  # list_num.append(11)
print("insert list_num", list_num)

# remove(x)
#           0  1  2  3  4  5  6  7  8
list_num = [1, 2, 3, 4, 3, 6, 7, 8, 9]
list_num.remove(3)
#           0  1  2  3  4  5  6  7
#          [1, 2, 4, 3, 6, 7, 8, 9]
print("remove list_num", list_num)
print("remove list_num", list_num[6])
# list_num.remove(11)

# pop([i])
#           0  1  2  3  4  5  6  7  8
list_num = [1, 2, 3, 4, 3, 6, 7, 8, 9]
list_num.pop()
print("pop list_num", list_num)
list_num.pop(2)
print("pop(2) list_num", list_num)

# clear()
list_num = [1, 2, 3, 4, 3, 6, 7, 8, 9]
list_num.clear()
print("clear list_num", list_num)

# index(x)
#           0  1  2  3  4  5  6  7  8
list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("index list_num", list_num.index(5))
# print("index list_num", list_num.index(10))

# operator in
print("operator in", 10 in list_num)
print("operator in", 5 in list_num)

# operator not in
print("operator not in", 10 not in list_num)
print("operator not in", 5 not in list_num)

user_type = "staff"

if user_type in ["admin", "staff", "cashier"]:
    print("user_type in list")

if user_type not in ["client"]:
    print("user_type not in list")

list_duplicates = [2, 3, 2, 3, 4, 4]
list_without_duplicates = []

for element_in_list in list_duplicates:
    if element_in_list not in list_without_duplicates:
        list_without_duplicates.append(element_in_list)
# iteration 0
# element_in_list = 2
# 2 not in [] -> True
# list_without_duplicates = [2]
# iteration 1
# element_in_list = 3
# 3 not in [2] -> True
# list_without_duplicates = [2, 3]
# iteration 2
# element_in_list = 2
# 2 not in [2, 3] -> False
# iteration 3
# element_in_list = 3
# 3 not in [2, 3] -> False
# iteration 4
# element_in_list = 4
# 4 not in [2, 3] -> True
# list_without_duplicates = [2, 3, 4]
# iteration 5
# element_in_list = 4
# 4 not in [2, 3, 4] -> False

print("list_without_duplicates", list_without_duplicates)

# count(x)
#           0  1  2  3  4  5  6  7  8
list_num = [1, 2, 3, 4, 3, 6, 7, 3, 9]
print("count list_num", list_num.count(3))

# sort()
list_num = [1, 2, 3, 4, 11, 6, 7, 14, 9]
list_num.sort()
print("sort list_num", list_num)
list_num.sort(reverse=True)
print("sort(reverse=True) list_num", list_num)

# reverse()
list_num = [1, 2, 3, 4, 11, 6, 7, 14, 9]
list_num.reverse()
print("reverse list_num", list_num)


# tuple
new_tuple = tuple()
new_tuple = (1, 2)

yes_values = ("Y", "y", "yes", True)
num_tuple = (1, 2, 3, 4)

print("by index tuple", num_tuple[2])

num_list = list(num_tuple)
print("tuple to list", num_list)
print("tuple", num_tuple)
print("list", num_list)
new_num_tuple = tuple(num_list)
print("list to tuple", new_num_tuple)

USER_TYPES = (
    1,
    "text",
    True,
    (1, "Admin"),
    (2, "Staff"),
    [1, 2, 3]
)
print("USER_TYPES", USER_TYPES)
print("USER_TYPES[0]", USER_TYPES[0])
print("USER_TYPES[2]", USER_TYPES[2])

USER_TYPES[-1].clear()
USER_TYPES[-1].append(1)
USER_TYPES[-1].append(2)
# USER_TYPES[1] = "new"
print("USER_TYPES", USER_TYPES)

#
import random

# random  0.0 <= X < 1.0
print("random.random", random.random())

# uniform(a, b)  a <= N <= b
print("random.uniform", random.uniform(0, 10))
print("random.uniform to int", int(random.uniform(0, 10)))

# randint(a, b)  a <= N < b
print("random.randint", random.randint(1, 11))

list_of_random_numbers = []

for i in range(10):
    list_of_random_numbers.append(random.randint(120, 160))

print("random list", list_of_random_numbers)
