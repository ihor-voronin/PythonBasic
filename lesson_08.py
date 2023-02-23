
my_list = [ 1 , 2 , 3 , 4 , 5 , 2 , 1 , 10]
print(my_list.index(4))

my_tuple = (1,2,3,4,5,6)
my_dict = {
    1: 2,
    2: 2,
    3: 2,
    "my_key": "value"
}
my_set = {1,2,3,4,5}


def linear_search(list_elements, element):  # O(n)
    print("len()", len(list_elements))
    for i in range(len(list_elements)):
        print("i:", i)
        print("list_elements[", i, "]:", list_elements[i])
        if list_elements[i] == element:
            return i
    return -1


print("result of linear_search", linear_search(my_list, 12))

my_string = " hello world"
print(my_string.find("h"))

print("range(10)", list(range(10)))
print("range(8)", list(range(8)))
print("range(2, 10)", list(range(2, 10)))


my_list_sort = [11, 56, 42, 12, 22, -3, 37]
my_list_sort.sort()
print("my_list_sort.sort()", my_list_sort)

a = 1
b = 2
c = 3

a, b, c = c, b, a
print("a, b = b, a", a, b, c)

my_list_sort = [11, 56, 42, 12, 22, -3, 37]
def bubble_sort(list_to_sort):  # O(n*n)
    for _ in range(0, len(list_to_sort) - 1):  # 6
        #              0 ... last_index - 1
        for x in range(0, len(list_to_sort) - 1):  # 6 * 6
            if list_to_sort[x] > list_to_sort[x + 1]:
                # temp = list_to_sort[x]
                # list_to_sort[x] = list_to_sort[x+1]
                # list_to_sort[x+1] = temp
                list_to_sort[x], list_to_sort[x + 1] = list_to_sort[x+1], list_to_sort[x]
            print(list_to_sort)
    return list_to_sort

print("bubble_sort", bubble_sort(my_list_sort))

# [11, 56, 42, 12, 22, -3, 37]
# [11, 42, 56, 12, 22, -3, 37]
# [11, 42, 12, 56, 22, -3, 37]
# [11, 42, 12, 22, 56, -3, 37]
# [11, 42, 12, 22, -3, 56, 37]
# [11, 42, 12, 22, -3, 37, 56]


my_list_sort = [11, 56, 42, 12, 22, -3, 37]


def selection_sort(list_to_sort):  # O(n*n) 6 + 18
    for i in range(0, len(list_to_sort) - 1):  # 6 iterations
        min_value = i
        for j in range(i, len(list_to_sort)):  # 6+5+4+2+1 = 18
            if list_to_sort[min_value] > list_to_sort[j]:
                min_value = j
        print("sorted part:", list_to_sort[:i])
        print("not sorted part:", list_to_sort[i:])
        print("iteration[", i, "]:", list_to_sort)
        print("min_value:", min_value, "\tmin_value[", min_value, "]", list_to_sort[min_value])
        print("i:", i, "\tmin_value[", i, "]", list_to_sort[i])
        print()

        # swap two elements
        list_to_sort[min_value], list_to_sort[i] = list_to_sort[i], list_to_sort[min_value]

    return list_to_sort  # return sorted list


print("selection_sort", selection_sort(my_list_sort))

# [11, 56, 42, 12, 22, -3, 37] []  [11, 56, 42, 12, 22, -3, 37]
# [-3, 56, 42, 12, 22, 11, 37] [-3] [56, 42, 12, 22, 11, 37]
# [-3, 11, 42, 12, 22, 56, 37] [-3, 11] [42, 12, 22, 56, 37]
# [-3, 11, 12, 42, 22, 56, 37] [-3, 11, 12] [42, 22, 56, 37]
# [-3, 11, 12, 22, 42, 56, 37]
# [-3, 11, 12, 22, 37, 56, 42]
# [-3, 11, 12, 22, 37, 42, 56]
print("\n\n")

my_list_sort = [11, 56, 42, 12, 22, -3, 37]

def insertion_sort(list_to_sort):  # O(n*n) 1+2+2+5+2 = 12 + 6
    for i in range(1, len(list_to_sort)):  # 6
        temp = list_to_sort[i]
        min_index = i
        print("before iteration[", i, "]", list_to_sort)
        while min_index > 0 and temp < list_to_sort[min_index - 1]:  # 0 | 0..i
            print("min_index", min_index)
            print("list_to_sort[min_index]", list_to_sort[min_index])
            print("list_to_sort[min_index - 1]", list_to_sort[min_index - 1])
            list_to_sort[min_index] = list_to_sort[min_index - 1]
            min_index -= 1
        list_to_sort[min_index] = temp
        print("i:", i, "\tmin_index:", min_index)
        print("after iteration[", i, "]", list_to_sort)
        print()

    return list_to_sort


print(my_list_sort)
print("insertion_sort", insertion_sort(my_list_sort))
