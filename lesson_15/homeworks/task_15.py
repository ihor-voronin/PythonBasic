from pprint import pprint

#  Кожен кортеж складається з номера замовлення та твору ціни на товари та кількості.
#  Вартість товару повинна бути збільшена на $10, якщо вартість замовлення менша за $100.
#
# Рекомендовано використовувати lambda та map.


def book_processing(list_book):
    if list_book[-2] * list_book[-1] < 100:
        list_book[-1] += 10
    return list_book


if __name__ == "__main__":
    list_books = [
        [34587, "Learning Python, Mark Lutz", 4, 40.95],
        [98762, "Programming Python, Mark Lutz", 5, 56.80],
        [77226, "Head First Python, Paul Barry", 3, 32.95],
        [88112, "Einfuhrung in Python3, Bernd Klein", 3, 24.99],
    ]

    # result = []
    # for list_book in list_books:
    #     if list_book[-2] * list_book[-1] < 100:
    #         list_book[-1] += 10
    #     result.append(list_book)
    result = map(book_processing, list_books)
    # result = map(lambda b: [b[0], b[1], b[2], b[-1] if b[-2]*b[-1] > 100 else b[-1] + 10], list_books)

    pprint(tuple(result))
