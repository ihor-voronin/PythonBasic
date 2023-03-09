from pprint import pprint

from lesson_11.custom_context_file_reader import custom_context_file_reader

# file-open
# "r" - Читати - Значення за замовчуванням. Відкриває файл для читання, помилка, якщо файл не існує
#
# "a" - Додати - Відкриває файл для додавання, створює файл, якщо він не існує
#
# "w" - Записати - Відкриває файл для запису, створює файл, якщо він не існує
#
# "x" - Створити - створює вказаний файл, повертає помилку, якщо файл існує
#
# "t" - Текст - значення за замовчуванням. Текстовий режим
#
# "b" - Двійковий файл - файл у двійковому режимі (наприклад, зображення), повертає помилку, якщо файл існує

# open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)

file = open("fantasy_names.txt")
print("open with default mode", type(file))
file.close()

file = open("file_image_test.png", "rb")
print("open with read binary mode", type(file))
file.close()

file = open("file_image_test.png", "wb")
print("open with write binary mode", type(file))
file.close()

with open("fantasy_names.txt", "r") as file:
    print("open with context manager", type(file))


# custom context manager for file
with custom_context_file_reader('fantasy_names.txt') as reader:
    print(reader.read())


# Reading and Writing Opened Files

# .read(<size>)
# Це зчитування з файлу на основі кількості байтів розміру.

file = open('fantasy_names.txt', "r")
print("read 30 bytes:", file.read(30))
print("read 100 bytes:", file.read(100))
print("read all file:", file.read())
file.close()

with open("fantasy_names.txt", "r") as file:
    print("read new 150 bytes", file.read(150))


# .readline(<count of symbols>)
# Це зчитує максимальну кількість символів із рядка.
# Це продовжується до кінця рядка, а потім обертається назад.

file = open('fantasy_names.txt', "r")
print("readline 20 symbols:", file.readline(20))
print("readline 50 symbols:", file.readline(50))
print("readline 50 symbols:", file.readline(50))
print("readline all in line:", file.readline())
file.close()


# .readlines()
# Це зчитує решту рядків із файлового об’єкта та повертає їх у вигляді списку.

file = open('fantasy_names.txt', "r")
print("readlines all lines:")
pprint(file.readlines())
file.close()


# Ітeрація по строкам
# Read and print the entire file line by line
print("Iterating over lines variant 1")
file = open('fantasy_names.txt', "r")
line = file.readline()
while line != '':  # The EOF char is an empty string
    print(line, end='')
    line = file.readline()
file.close()
print()

print("Iterating over lines variant 2")
file = open('fantasy_names.txt', "r")
for line in file.readlines():
    print(line, end='')
file.close()
print()

with open('fantasy_names.txt', "r") as file:
    for line in file.readlines():
        print(line, end='')
print()


# write line(s)

# .write(string)
# Записує строку в файл

# .writelines(seq)
# Це записує послідовність у файл. До кожного елемента послідовності не додаються закінчення рядків.
# Ви повинні додати відповідне закінчення рядка.

file = open("fantasy_names.txt", "r")
text = file.readlines()
file.close()

file2 = open("fantasy_names_reverse.txt", "w")
for line in reversed(text):
    file2.write(line)
file2.close()

try:
    file = open("fantasy_names_reverse_non_exist.txt", "x")
except FileExistsError:
    print("error FileExistsError")
finally:
    file.close()

file = open("fantasy_names_reverse.txt", "a")
try:
    file.write("end line")
except Exception:
    print("error")
finally:
    file.close()

with open("fantasy_names_reverse.txt", "w") as file:
    file.write("empty")


file3 = open("fantasy_names_reverse_2.txt", "w")
file3.writelines(reversed(text))
file3.close()


