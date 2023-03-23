def number_collaps(num):
    new_num = sum([int(i) for i in str(num)])
    if new_num < 10:
        return new_num
    return number_collaps(new_num)


if __name__ == "__main__":
    print(
        number_collaps(9184)
    )  # повинно повернути 1, так як 8+9+3+8 = 28 -> 2+8 = 10 -> 1+0 = 1
