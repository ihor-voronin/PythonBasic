from pprint import pprint
from random import randint

if __name__ == "__main__":
    M = 4
    N = 5
    matrix = [[randint(1, 20) for i in range(M)] for j in range(N)]

    # pprint(matrix)

    sum_col = [0 for i in range(M)]
    for row in matrix:
        sum_row = 0
        for i in range(len(row)):
            print(f"{row[i]:>4}", end="")
            sum_row += row[i]
            sum_col[i] += row[i]
        print(f"\t{sum_row}")

    print()
    for i in sum_col:
        print(f"{i:>4}", end="")
