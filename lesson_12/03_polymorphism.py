from typing import Union


class BaseCalculator:
    def add(self, x: Union[int, float], y: Union[int, float]) -> None:
        print("add result", x + y)

    def minus(self, x: Union[int, float], y: Union[int, float]) -> None:
        print("minus result", x - y)


class Calculator(BaseCalculator):
    def add(self, x: Union[int, float], y: Union[int, float]) -> None:
        print(f"add: {x} + {y} = {x + y}")

    def minus(self, x: Union[int, float], y: Union[int, float]) -> None:
        print(f"minus: {x} - {y} = {x-y}")


if __name__ == "__main__":
    base = BaseCalculator()
    calculator = Calculator()

    base.add(4, 5)
    base.minus(4, 5)

    calculator.add(4, 5)
    calculator.minus(4, 5)

    # calculator.add(4, 5, 10)
