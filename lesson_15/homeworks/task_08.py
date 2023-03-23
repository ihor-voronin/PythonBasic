# Користувач вводить окремо рядок `s` і один символ `ch`.
#
# Необхідно здійснити пошук у рядку `s` всіх символів `ch`.
#
# s = input("Введіть рядок:")
# ch = input("Введіть символ:")
#
#
# Треба вивести всі індекси символа у введеному рядку.
#
# Для вирішення потрібно використовувати тільки функцію `find()`
#
# (rfind()), оператори `if` і `for`(while).

if __name__ == "__main__":
    s = input("Введіть рядок:")
    ch = input("Введіть символ:")

    # for i in range(len(s)):
    #     if s[i] == ch:
    #         print(i)

    start_index = 0
    while (find_index := s.find(ch, start_index)) != -1:
        print(find_index)
        start_index = find_index + 1
