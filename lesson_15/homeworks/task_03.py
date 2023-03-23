# У школі вирішили набрати три нові математичні класи.
# Так як заняття з математики у них відбуваються в один і той же час,
# було вирішено виділити кабінет для кожного класу і купити нові парти.
# За кожною партою може сидіти не більше двох учнів. Відомо кількість учнів у кожному із трьох класів.
# Скільки всього потрібно закупити парт, щоб їх вистачило на всіх учнів?
# Програма отримує на вхід три натуральні числа: кількість учнів у кожному з трьох класів.
#
#
# Використовувати лише арифметичні оператори. (Підказка: знадобляться // + та %)
from typing import Tuple

STUDENTS_PER_DESK = 2


def input_data() -> Tuple[int, int, int]:
    class_1 = int(input("Students in class 1:"))
    class_2 = int(input("Students in class 2:"))
    class_3 = int(input("Students in class 3:"))
    return class_1, class_2, class_3


def calculation(class_1: int, class_2: int, class_3: int) -> int:
    sum_students = class_1 + class_2 + class_3
    return int((sum_students / 2).__ceil__())
    # return sum_students // STUDENTS_PER_DESK + sum_students % STUDENTS_PER_DESK
    # return sum_students // STUDENTS_PER_DESK + 1 if sum_students % STUDENTS_PER_DESK != 0 else 0


# 13 - 7
# 9  - 5
# 15 - 8
# 37 = 19 desks


def output_data(desk_amount: int) -> None:
    print(f"Amount of desks: {desk_amount}")


if __name__ == "__main__":
    output_data(calculation(*input_data()))
