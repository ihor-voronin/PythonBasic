# <list>.sort([key], [reverse=False])

# sorted(collection, [key], [reverse=False])

cars = ['Ford', 'BMW', 'Volvo', "AD", "B", "C", "A"]

cars.sort()
print(cars)


def sort_by_len(element):
    return len(element)


cars.sort(key=sort_by_len)
print(cars)

cars = [
  {'car': 'Ford', 'year': 2005, 'count': 1},
  {'car': 'Mitsubishi', 'year': 2000, 'count': 76},
  {'car': 'BMW', 'year': 2019, 'count': 12},
  {'car': 'VW', 'year': 2011, 'count': 3}
]


def sort_by_year(e):
    return e['year']


cars.sort(key=sort_by_year)
print(cars)

# e - кожен елемент колекції ( елемент колекції == 1 словник)
cars.sort(key=lambda e: e['count'])
print(cars)

# <list>.sort() - сортує вже існуючий список <list>

# sorted(collection, [key], [reverse=False])
# sorted(cars, key=lambda e: e['year'] * e['count'])
print(sorted(cars, key=lambda e: e['year'] * e['count']))


def func():
    my_list = [4, 2, 1, 76, 22, 3]

    print("sorted", sorted(my_list))
    print("My_list", my_list)
    print(".sort", my_list.sort())
    print("My_list after .sort()", my_list)
    print("delete here")


func()

# all(collection)
# any(collection)

print("all([True, True, True])", all([True, True, True]))
print("all([True, True, False])", all([True, True, False]))
print("all([False, False, False])", all([False, False, False]))

user = [
    {"nickname": "some text", "age": 19},
    {"nickname": "some text2", "age": 21},
    {"nickname": "some text3", "age": 32},
]

print("age >= 18", all(map(lambda e: e['age'] >= 18, user)))

list_string = ["text1", "", "text2"]
list_string2 = ["text1", "gf", "text2"]
list_string3 = ["", "", ""]

print("all string", all(list_string))
print("all string2", all(list_string2))

# any(collection)

print("any", any([True, False, False]))
print("any", any([False, False, False]))
print("any string", any(list_string))
print("any string2", any(list_string2))
print("any string3", any(list_string3))

sub_routers = [
    "api/v1",
    "api/v2",
    "api/v3",
    "api/v4",
]
url = "https://my_site.com/api/v1/"

new_list = []
for i in sub_routers:
    if i in url:
        new_list.append(True)
    else:
        new_list.append(False)

if any(new_list):
    print("Yeap!")  # check if correct

if any([True if i in url else False for i in sub_routers]):
    print("Yeap!")

print("if ", [True if i in url else False for i in sub_routers])
print("if without else", [True for i in sub_routers if i in url])


