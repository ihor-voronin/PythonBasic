class Person:
    firstname: str
    lastname: str

    def __init__(self, first_name: str, last_name: str) -> None:
        self.firstname = first_name
        self.lastname = last_name

    def about(self) -> str:
        return f"FirstName: {self.firstname} \t LastName {self.lastname}"


class Animal:
    def about(self):
        return "Meow"

    def say_something(self, text):
        return "meow-meow" + text


class PointMixin:
    def is_complete_course(self) -> bool:
        return self.points > 75


class Student(Person, Animal, PointMixin):
    # pass
    points: int

    def __init__(self, first_name: str, last_name: str, points: int) -> None:
        self.points = points
        super().__init__(first_name, last_name)
        # super(Student, self).__init__(first_name, last_name)

    def about(self) -> str:
        return super().about() + f"\t {self.points} points"
        # return f"FirstName: {self.firstname} \t LastName {self.lastname}" + f"\t {self.points} points"

    def say_something(self, *args):
        return super().say_something("oops")


if __name__ == "__main__":
    person = Person("John", "Doe")
    print(person.about())
    print(type(person))

    student = Student("Mike", "Olsen", 96)
    print(student.about())
    print(type(student))
    print(student.say_something())

    print(Person.__subclasses__())
    print(Animal.__subclasses__())
    print(Student.__subclasses__())

    print("is_complete_course", student.is_complete_course())
