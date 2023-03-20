def first_3_letters(string):
    current_index = 0

    while current_index < (len(string) - 1):
        yield string[current_index: current_index+3]
        current_index += 3


if __name__ == "__main__":
    for i in [1, 2, 3, 4]:
        print(i)

    for i in first_3_letters("aaa333bbb55"):
        print(i)
