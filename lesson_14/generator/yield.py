def first_n(n):
    # Початкове значення
    value = 0
    print("value", value)
    # цикл з лічильниколм та умовою число менше n
    while value < n:
        print("before yield value", value)
        # повернути поточне значення лічильника
        yield value
        print("after yield value", value)

        # збільшити лічильник
        value += 1
        print("after +1 value", value)


if __name__ == "__main__":
    for k in first_n(3):
        print("print by for", k)

    # print("\nCall generator manually")
    # generator = first_n(3)
    # print(next(generator))
    # print(next(generator))
    # print(next(generator))
