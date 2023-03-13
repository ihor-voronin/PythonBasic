class Student:
    name: str
    _age: int
    __points: int

    def __init__(self, name: str, age: int, points: int) -> None:
        self.name = name
        self._age = age
        self.__points = points

    def about(self) -> str:
        return f"Student {self.name} \t {self._age} years old \t {self.__points} points"

    def get_age(self) -> int:
        return self._age

    def __change_age(self, num: int) -> None:
        self._age = num


student_01 = Student("Mike", 20, 97)
student_02 = Student("Leon", 21, 98)
student_03 = Student("Steve", 22, 77)

print(student_01.about())
print(student_02.about())
print(student_03.about())

print("Student 01 name:", student_01.name)
print("Student 02 name:", student_02.name)
print("Student 03 name:", student_03.name)

print()
# print("Bad practice to access to protected attributes")
print("Student 01 age:", student_01._age)
print("Student 02 age:", student_02._age)
print("Student 03 age:", student_03._age)
student_01._age = 99
# student_02.__change_age(88)
print("Student 01 age:", student_01.get_age())
print("Student 02 age:", student_02.get_age())
print("Student 03 age:", student_03.get_age())

print()
print("Try to access to private attributes")
try:
    print("Student 01 points:", student_01.__points)
    print("Student 02 points:", student_02.__points)
    print("Student 03 points:", student_03.__points)
except AttributeError as e:
    print("Oops cannot access to __points with error:", e)

print()
print("But we can access to private attributes")
print("Student 01 points:", student_01._Student__points)
print("Student 02 points:", student_02._Student__points)
print("Student 03 points:", student_03._Student__points)
