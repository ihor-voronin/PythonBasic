def expanded_form(num):
    if num <= 0:
        raise Exception()

    num_str = str(num)
    # print(num_str[0])
    list_nums = []
    for i in range(len(num_str)):
        if num_str[i] == "0":
            continue
        list_nums.append(num_str[i] + "0" * (len(num_str) - i - 1))
        # print(num_str[i]+'0' * (len(num_str) - i - 1), "+", end="")
        # print("i", i)
        # print("len(num_str)", len(num_str))

    print(" + ".join(list_nums))


def expanded_form_2(num):
    list_nums = []
    index = 0
    while num >= 10:
        number = num % 10
        if number != 0:
            list_nums.append(number * (10**index))
        num //= 10
        index += 1
    list_nums.append(num * (10**index))
    print(" + ".join([str(x) for x in list_nums[::-1]]))


if __name__ == "__main__":
    expanded_form_2(70304)  # повинно повернути '70000 + 300 + 4'
    expanded_form(42)
    # expanded_form(0)

# 7 0 3 0 4
