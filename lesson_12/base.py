matrix = [
    [1,2],
    [3,4]
]
num = 15

def print_matrix(custom_matrix):
    print(custom_matrix)


print(isinstance(matrix, object))
print(isinstance(num, object))
print(isinstance(print_matrix, object))

print(type(matrix))
print(type(num))
print(type(print_matrix))


class Studen:
    first_name: str
    last_name: str
    points: int
    current_lesson: int

    # execute on initialization
    def __init__(self, first_name, last_name, points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.points = points
        self.current_lesson = 0

    def about(self) -> None:
        print(f"Name:{self.first_name} "
              f"SecondName: {self.last_name} "
              f"Points: {self.points} "
              f"CurrentLesson {self.current_lesson}")

    def complete_lesson(self, points_by_lesson: int) -> None:
        self.current_lesson += 1
        self.points += points_by_lesson


print("MyClass")

my_class_instance = Studen("Mike", "Vasovski", 97)
my_class_instance2 = Studen("Alex", "Kotyk")

print("my_class_instance.first_name", my_class_instance.first_name)
print("my_class_instance.last_name", my_class_instance.last_name)
print("my_class_instance.points", my_class_instance.points)

print("my_class_instance2.first_name", my_class_instance2.first_name)
print("my_class_instance2.last_name", my_class_instance2.last_name)
print("my_class_instance2.points", my_class_instance2.points)

print("my_class_instance.about()")
my_class_instance.about()
print("my_class_instance2.about()")
my_class_instance2.about()

my_class_instance.complete_lesson(30)
print()
print("my_class_instance.about()")
my_class_instance.about()
print("my_class_instance2.about()")
my_class_instance2.about()


# Studen.about()
# print(type(my_class_instance))
# print(isinstance(my_class_instance, object))
# print(my_class_instance == my_class_instance2)
# print(id(my_class_instance))
# print(id(my_class_instance2))
