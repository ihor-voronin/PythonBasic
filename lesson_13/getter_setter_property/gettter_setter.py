class Celsius:
    __temperature: float

    def __init__(self, temperature: float = 0) -> None:
        self.__temperature = temperature

    def to_fahrenheit(self) -> float:
        return round(
            (self.__temperature * 1.8) + 32,
            5
        )

    def get_temperature(self) -> float:
        print("getting value")
        return self.__temperature

    def set_temperature(self, value) -> None:
        print("setting value")
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self.__temperature = value

    def del_temperature(self):
        print("del temperature")

    # create property method 1
    # temperature = property(fset=set_temperature, fdel=del_temperature, fget=get_temperature)

    # create property method 2
    # temperature = property()
    # temperature = temperature.getter(get_temperature)
    # temperature = temperature.setter(set_temperature)
    # temperature = temperature.deleter(del_temperature)


    # create property method 3

    # temperature = property()
    # temperature = temperature.getter(get_temperature)
    @property  # crete getter for property temperature
    def temperature(self):
        print("get temperature method")
        return self.__temperature

    @property
    def temperature2(self):
        return self.__temperature

    # temperature = temperature.setter(set_temperature)
    @temperature.setter  # create setter for property temperature
    def temperature(self, value):
        print("set temperature method")
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self.__temperature = value

    @temperature2.setter
    def temperature2(self, value):
        self.__temperature = value

    # temperature = temperature.deleter(del_temperature)
    @temperature.deleter  # create deleter for property temperature
    def temperature(self):
        print("del temperature method")

    @temperature2.deleter
    def temperature2(self):
        print("del t2")

# property(fget=None, fset=None, fdel=None, doc=None)


def set_temperature(self, value) -> None:
    print("setting value")
    if value < -10:
        raise ValueError("Temperature below -273 is not possible")
    self.__temperature = value


if __name__ == "__main__":
    # Create a new object, set temperature internally called by __init__
    my_temperature = Celsius(37)

    # method 1
    my_temperature.set_temperature(-175.182)
    print(my_temperature.get_temperature())

    # set
    my_temperature.temperature = -22
    # get
    print(my_temperature.temperature)
    # del
    del my_temperature.temperature

    print(Celsius.temperature.__dir__())
    my_temperature.temperature2 = -12
    print(my_temperature.temperature2)
    del my_temperature.temperature2

    # Get the to_fahrenheit method, get temperature called by the method itself
    print(my_temperature.to_fahrenheit())
