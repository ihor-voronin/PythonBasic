# set

# {}
{"a", 5, True}

# empty set
empty_set = set()  # operator empty_set = {} - return dict! Not set!
print("empty_set", empty_set)

# set()
set_var = set([1, 2, 2, 3, 3])
print(set_var)

# {{1,2}, 3}
# frozenset(iterable)
frozen_set_var = frozenset(set_var)
print(frozen_set_var)

print({frozen_set_var, 2})
print({frozenset([1, 2, 3]), frozenset([2, 3])})

file_list = [
    "file1.txt",
    "file2.txt",
    "file3.txt",
    "file1.txt",
]
print(frozenset(file_list))

set_01 = {1, 2, 3, 4, 5}
set_02 = {3, 4, 5, 6, 7}

# in set_01 but not in set_02
print("operator - ", set_01 - set_02)

# in set_01 or set_02 or both
print("operator | ", set_01 | set_02)

# in both set_01 and set_02
print("operator & ", set_01 & set_02)

# in set_01 or set_02 but not both
print("operator ^ ", set_01 ^ set_02)

# operator [in] and [not in]
print("operator in", 4 in set_01)
print("operator in", 10 in set_01)
print("operator not in", 4 not in set_01)
print("operator not in", 10 not in set_01)

set_01 = {12, 14, 16, 123}
set_02 = {16, 14}

for item_set in set_02:
    if item_set in set_01:
        print(item_set)

# method add(value)
set_01.add(199)

list_duplicates = [1, 2, 2, 3, 3, 4, 4]

print("list to frozenset", frozenset(list_duplicates))

set_uniq = set()
for item_list in list_duplicates:
    set_uniq.add(item_list)

print(set(list_duplicates))


set_01 = {1, 2, 3, 4, 5}
set_02 = {3, 4, 5, 6, 7}

# method intersection(another_set)  operator &
print("intersection", set_01.intersection(set_02))
print("intersection", set_01 & set_02)

# method union(another_set)
print("union", set_01.union(set_02))
print("union", set_01 | set_02)

# method symmetric_difference(another_set)
print("symmetric_difference", set_01.symmetric_difference(set_02))
print("symmetric_difference", set_01 ^ set_02)

list_duplicates = [1, 2, 2, 3, 3, 4, 4]
list_duplicates.append(frozenset(list_duplicates))
print(list_duplicates)

# iterable
set_01 = {1, 2, 3, 4, 5}
print("set iterable ", end="")
for item_set in set_01:
    print(item_set, end=" ")
print()


# Dict
# key: value
# key: value
# key: value
# key: value
# key: value

# {}
new_dict = {}
print("type empty {}", type(new_dict))
new_dict = dict()
print("type empty dict()", type(new_dict))

new_dict = {
    14: "nick01",
    197: "nick02",
    141: {1: "user", 2: "type", 3: type},
    142.75: "nick04",
    True: "nick05",
    "True": "nick15",
}
print("duplicate keys", new_dict)
# key
# 1) immutable  - int, float, str, frozenset, bool
# 2) unique

print("by keys", new_dict[True])
print("by keys", new_dict["True"])
print("by keys", new_dict[141])

# dict() - empty dict
new_dict = dict()
# dict(**keyword_arg)
new_dict = {
    # key   :  value
    "winter": 1,
    "spring": 2,
    "summer": 3,
    "autumn": 4,
    4: "seasons",
}
print(new_dict)
print(new_dict[4])

new_dict = dict(winter=1, spring=2, summer=3, autumn=4)
print(new_dict)

new_tuple = (
    1,
    2,
    3,
    4,
)
print(new_tuple)

# dict(mapping, **keyword_arg)
days = [1, 2, 3]
days_names = ["mon", "tue", "wed"]

new_dict = dict(zip(days, days_names))
# 1 mon
# 2 tue
# 3 wed
print(new_dict)
#                key  value  key  value  key  value
new_dict = dict([(1, "mon"), (2, "tue"), (3, "wed"), (4, None)])
print(new_dict)
#                key  value  key  value  key  value
new_dict = dict(((1, "mon"), (2, "tue"), (3, "wed")))
print(new_dict)
#                key  value  key  value  key  value
new_dict = dict([[1, "mon"], [2, "tue"], [3, "wed"]])
print(new_dict)


# dict(iterable, **keyword_arg)
new_dict = dict({1: 'mon', 2: 'tue', 3: 'wed'})
print(new_dict)


# operator []
new_dict = {
    14: "nick01",
    197: "nick02",
    141: {1: "user", 2: "type", 3: type},
    142.75: "nick04",
    True: "nick05",
    "True": "nick15",
}

print(new_dict[14])
# print(new_dict["16"])

# method get(key, [default])
print("get 14", new_dict.get(14))
print("get 16", new_dict.get(16))
print("get 16", new_dict.get(16, "not found"))

# del <dict>[<key>]
# del new_dict[14]
# print("after del 14", new_dict)

# operator in, not in
print("operator in", 14 in new_dict)
print("operator in", 16 in new_dict)
print("operator not in", 14 not in new_dict)
print("operator not in", 16 not in new_dict)

if 16 in new_dict:
    del new_dict[16]

# if <condition>:
#   <operand>

# method clear()
new_dict.clear()  # new_dict = {}
# new_dict = {}  # only dict

print(new_dict)

new_dict = {
    14: "nick01",
    197: "nick02",
    141: {1: "user", 2: "type", 3: type},
    142.75: "nick04",
    True: "nick05",
    "True": "nick15",
}
# method copy()
copy_new_dict = new_dict.copy()
reference_new_dict = new_dict
new_dict[14] = "text"
print("copy", copy_new_dict)
print("original", new_dict)
print("reference", reference_new_dict)

# dict.fromkeys(keys, [value])
keys_tuple = ("key01", "key02", "key03")
value = 0
new_dict = dict.fromkeys(keys_tuple, value)
new_dict2 = dict.fromkeys(["hi", "in", "on"], 0)
new_dict3 = dict.fromkeys(keys_tuple)

print("dict.fromkeys", new_dict)
print("dict.fromkeys", new_dict2)
print("dict.fromkeys", new_dict3)

# method items()
new_dict = {
    14: "nick01",
    197: "nick02",
    141: {1: "user", 2: "type", 3: type},
    142.75: "nick04",
    True: "nick05",
    "True": "nick15",
}
print("items()", new_dict.items())
for key, value in new_dict.items():
    print("key:", key, "value:", value)

for item in new_dict:
    print("item:", item)

# method keys()
print("keys()", new_dict.keys())
for key in new_dict.keys():
    print("key:", key)

# method values()
print("values()", new_dict.values())
for value in new_dict.values():
    print("value:", value)

# method pop(key, [default])
new_dict = {
    14: "nick01",
    197: "nick02",
    141: {1: "user", 2: "type", 3: type},
    142.75: "nick04",
    True: "nick05",
    "True": "nick15",
    200: "nick04",
}
print("pop result", new_dict.pop(199, "not exist key"))
print("pop result", new_dict.pop(199, None))
print("pop", new_dict)

# method popitem()
print("popitem", new_dict.popitem())
print(new_dict)

# method setdefault(key, value)
print("setdefault", new_dict.setdefault(300, "Not Found"))
print(new_dict)

# method update(iterable)
new_dict.update({
    400: "text 400",
    500: "text 500",
    600: "text 600",
})
print("update result", new_dict)

list_num = [1, 2, 1]

new_dict = {}
for item_list in list_num:
    value = new_dict.get(item_list, 0)
    new_dict[item_list] = value + 1

#  item_list = 1
#  value = new_dict.get(1, 0) = 0
#  new_dict[1] = value + 1 = 0 + 1 = 1
#  new_dict = {1: 1}
#  item_list = 2
#  value = new_dict.get(2, 0) = 0
#  new_dict[2] = value + 1 = 0 + 1 = 1
#  new_dict = {1: 1, 2: 1}
#  item_list = 1
#  value = new_dict.get(1, 0) = 1
#  new_dict[1] = value + 1 = 1 + 1 = 2
#  new_dict = {1: 2, 2: 1}

print(new_dict)

sting_val = "Hi new world Hi new"


list_words = sting_val.split()  # ['Hi', 'new', 'world', 'Hi', 'new']
print("list_words", list_words)

set_word = set(list_words)  # {'Hi', 'new', 'world'}
print("set_word", set_word)

dict_word = {}
for word in set_word:  # word in {'Hi', 'new', 'world'}
    print("current word", word)
    print("count of word ", word, "is", sting_val.count(word))
    dict_word[word] = sting_val.count(word)

    if sting_val.count(word) > 1:
        print("duplicate word =", word)

# for key, value in dict_word.items():
#     if value > 1:
#         print("duplicate word =", key)
# word = Hi
# dict_word['Hi'] = 2
# word = new
# dict_word['new'] = 2
# word = world
# dict_word['world'] = 1

print("dict_word", dict_word)


# comprehension
# list

# [f(value) for value in <iterable>]
new_list = [num**2 for num in range(1, 10)]  # f(value) == num**2
print(new_list)

new_list = []
for num in range(1, 10):
    new_list.append(num**2)
print(new_list)

# [f(value) if <condition> else g(x) for value in <iterable>]
new_list = [num**2 if num%2==0 else 0 for num in range(1, 10)]
print(new_list)

new_list = []
for num in range(1, 10):
    if num % 2 == 0:
        new_list.append(num**2)
    else:
        new_list.append(0)
print(new_list)

# [f(value) for value in <iterable> if <condition> ]
new_list = [num**2 for num in range(1, 10) if num % 2 == 0]
print(new_list)

new_list = []
for num in range(1, 10):
    if num % 2 == 0:
        new_list.append(num**2)
print(new_list)

# dict

# {key:f(value) for value in <iterable>}
new_dict = {num: num**2 for num in range(1, 10)}
print(new_dict)

new_dict = {}
for num in range(1, 10):
    new_dict[num] = num**2
print(new_dict)


# {key:f(value) if <condition> else g(x) for value in <iterable>}
new_dict = {num: num**2 if num % 2 == 0 else 0 for num in range(1, 10)}
print(new_dict)

new_dict = {}
for num in range(1, 10):
    if num % 2 == 0:
        new_dict[num] = num**2
    else:
        new_dict[num] = 0
print(new_dict)

# {key: f(value) for value in <iterable> if <condition> }
new_dict = {num: num**2 for num in range(1, 10) if num % 2 == 0}
print(new_dict)

new_dict = {}
for num in range(1, 10):
    if num % 2 == 0:
        new_dict[num] = num**2
        # new_dict.update({num: num**2})
        # new_dict.update(zip([num], [num**2]))
print(new_dict)
