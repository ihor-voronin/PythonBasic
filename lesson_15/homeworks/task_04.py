# Дано ціле, позитивне, тризначне число.
# Наприклад: 123, 867, 374.
# Необхідно його перевернути.
# Наприклад, якщо ввели число 123, то має вийти на виході ЧИСЛО 321.
# ВАЖЛИВО! Працювати лише з числами.
# Рядки, оператор IF та цикли використовувати НЕ МОЖНА!


def num_as_string():
    num = input("input num:")
    print(num[::-1])


def num_as_math():
    num = int(input("input num:"))
    # 572 = 500 + 70 + 2
    n1 = num % 10
    n2 = num % 100 - n1
    n3 = num - n2 - n1
    print(n1, n2 // 10, n3 // 100)


def num_as_for():
    num = int(input("input num:"))
    result = 0
    while num > 10:
        result += num % 10
        num //= 10
        result *= 10

    print(result + num)


if __name__ == "__main__":
    # num_as_string()
    num_as_for()
