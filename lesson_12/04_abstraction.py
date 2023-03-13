from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def mileage(self):
        pass


# class Car:
#     def mileage(self):
#         raise NotImplementedError()


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Volvo(Car):
    def mileage(self):
        print("The mileage is 20kmph ")

    def speed(self):
        print("100kmph")


if __name__ == "__main__":
    t = Tesla()
    t.mileage()

    s = Suzuki()
    s.mileage()

    v = Volvo()
    v.speed()

    try:
        c = Car()
        c.mileage()
    except (TypeError, NotImplementedError) as e:
        print("cannot create instance with error:", e)
    else:
        print("error not found")
