# За цим цілим числом N роздрукуйте всі квадрати натуральних чисел, що не перевищують N,
# в порядку зростання.

if __name__ == "__main__":
    N = int(input("N:"))

    print(f"{N}\t", end="")
    i = 1
    while i**2 < N:
        print(i**2, end=" ")
        i += 1

    for i in range(1, N // 2):
        i_2 = i**2
        if i**2 > N:
            break
        print(i**2, end=" ")
