from abc import ABC


class Animal(ABC):
    type: str

    def __init__(self, name):
        self.name = name

    def say_something(self):
        raise NotImplementedError()

    def __repr__(self):
        return f"{self.type}: {self.name}"


class Cat(Animal):
    def __init__(self, name):
        self.type = "cat"
        super().__init__(name)

    def say_something(self):
        return "meow"


class Dog(Animal):
    def __init__(self, name):
        self.type = "dog"
        super().__init__(name)

    def say_something(self):
        return "woof"


class Zoo:
    __animals: list
    __name: str

    def __init__(self, name):
        self.name = name
        self.__animals = []

    def get_name(self):
        return self.__name

    def add_pet(self, pet):
        self.__animals.append(pet)

    def delete_pet(self, pet):
        self.__animals.remove(pet)

    def get_animals(self):
        return self.__animals

    def __repr__(self):
        return f"Zoo: {self.name}\n" + "\t".join(str(animal) for animal in self.__animals)


if __name__ == "__main__":
    zoo = Zoo("ZooTopia")

    cat1 = Cat("murzik")
    cat2 = Cat("pushok")

    dog = Dog("bim")

    zoo.add_pet(cat1)
    zoo.add_pet(cat2)
    zoo.add_pet(dog)

    print(zoo.get_animals())
    print(zoo)
    for animal in zoo.get_animals():
        print(animal, animal.say_something())