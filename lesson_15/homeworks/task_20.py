from pprint import pprint
from random import randint


def print_matrix(matrix_to_print):
    for i in range(M):
        for j in range(M):
            print(f"{matrix_to_print[j][i]:<4}", end="")
        print()


def print_sum_columns(matrix_to_print):
    for row in matrix_to_print:
        print(f"{row[-1]:<4}", end="")


def is_bigger(x, y):
    return x > y


def is_lower(x, y):
    return x < y


def bubble_sort(list_to_sort, condition):  # O(n*n)
    for _ in range(0, len(list_to_sort) - 2):
        for x in range(0, len(list_to_sort) - 2):
            if condition(list_to_sort[x], list_to_sort[x + 1]):
                list_to_sort[x], list_to_sort[x + 1] = (
                    list_to_sort[x + 1],
                    list_to_sort[x],
                )
    return list_to_sort


def bubble_sort_matrix(matrix_to_sort):  # O(n*n)
    for _ in range(0, len(matrix_to_sort) - 2):
        for x in range(0, len(matrix_to_sort) - 2):
            if matrix_to_sort[x][-1] > matrix_to_sort[x + 1][-1]:
                matrix_to_sort[x], matrix_to_sort[x + 1] = (
                    matrix_to_sort[x + 1],
                    matrix_to_sort[x],
                )
    return matrix_to_sort


if __name__ == "__main__":
    M = 4
    matrix = [[randint(1, 20) for i in range(M)] for j in range(M)]
    # pprint(matrix)
    # print()
    print_matrix(matrix)

    for i in range(len(matrix)):
        matrix[i].append(sum(matrix[i]))

    # print()
    # print_matrix(matrix)
    # print("-"*(M*4))
    # print_sum_columns(matrix)

    for i in range(0, len(matrix), 2):
        matrix[i] = bubble_sort(matrix[i], is_bigger)

    for i in range(1, len(matrix), 2):
        matrix[i] = bubble_sort(matrix[i], is_lower)

    new_matrix = bubble_sort_matrix(matrix)
    print()
    print()
    print_matrix(new_matrix)
    print("-" * (M * 4))
    print_sum_columns(new_matrix)

# [1 2 3]
# [4 5 6]
# [7 8 9]

# |1| 2| 3
# |4| 5| 6
# |7| 8| 9
