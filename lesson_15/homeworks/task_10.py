# Дано перелік чисел. Визначте, скільки в цьому списку елементів, які більше двох своїх сусідів (ліворуч та праворуч),
# і виведіть кількість таких елементів.
# Останні елементи списку ніколи не враховуються, оскільки у них недостатньо сусідів.
from random import randint

if __name__ == "__main__":
    numbers = [randint(0, 10) for i in range(10)]
    print(numbers)

    count_of_neighbors = 0
    for index in range(1, len(numbers) - 1):
        if numbers[index] > numbers[index - 1] and numbers[index] > numbers[index + 1]:
            count_of_neighbors += 1
            print(numbers[index], end=" ")

        print("~", end=" ")

    print()
    index = 1
    while index < (len(numbers) - 1):
        if numbers[index] > numbers[index - 1] and numbers[index] > numbers[index + 1]:
            count_of_neighbors += 1
            print(numbers[index], end=" ")
            index += 1
        index += 1
        print("&", end=" ")
