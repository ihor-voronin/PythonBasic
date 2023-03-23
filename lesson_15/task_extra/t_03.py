from pprint import pprint


def snail(list_data):
    ...


if __name__ == "__main__":
    data = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]

    data2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    expected2 = [1, 2, 3, 6, 9, 8, 7, 4, 5]

    assert snail(data) == expected
    assert snail(data2) == expected2

    pprint(data)
    pprint(snail(data))
    pprint(expected)
