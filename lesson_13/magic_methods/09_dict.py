from pprint import pprint


class TempClass:
    """
    Temp class
    """
    a = 1

    def temp_function(self):
        pass


if __name__ == "__main__":
    TempClass.my_func = lambda self, x: x+2
    pprint(TempClass.__dict__)
