# n школярів ділять k яблук порівну, залишок, що не ділиться, залишається в кошику.
# Скільки яблук дістанеться кожному школяру? Скільки яблук залишиться у кошику?
# Програма отримує на вхід числа n і k і повинна вивести кількість яблук, що шукається (два числа).
#
# Використовувати лише арифметичні оператори (Підказка: знадобляться // та %)
from typing import Tuple

Apples = int
Students = int
ApplePerStudent = int
AppleInBracket = int


def input_data() -> Tuple[Apples, Students]:
    k = int(input("Apple amount:"))
    n = int(input("Students amount:"))
    return k, n


def calculation(k: Apples, n: Students) -> Tuple[ApplePerStudent, AppleInBracket]:
    return k // n, k % n


def output_data(
    apple_per_student: ApplePerStudent, apple_in_bracket: AppleInBracket
) -> None:
    print(
        f"Apples per student: {apple_per_student}\nApple in bracket: {apple_in_bracket}"
    )


if __name__ == "__main__":
    output_data(*calculation(*input_data()))
