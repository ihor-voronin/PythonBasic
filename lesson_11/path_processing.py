import os
from os import path

print("dir()", dir())

print("__file__", __file__)

# path.abspath(path)
my_path = r"C:\.\Users\Voron\.\PycharmProjects\\PythonBasic\lesson_11\path_processing.py"
print("abspath", path.abspath(__file__))
print("abspath", path.abspath(my_path))

# path.basename(path)
print("basename", path.basename(__file__))
print("dirname", path.dirname(__file__))


# path.commonprefix(list)
print("commonprefix", path.commonpath([r'C:\Users\local\library', r'C:\Users\local\lib']))
# C:\Users\local\lib

# path.commonpath(list)
print("commonpath", path.commonpath([r'C:\Users\local\library', r'C:\Users\local\lib']))

# path.exists(path)
print("exists", path.exists(__file__))
new_file_path = path.dirname(__file__) + "\\new_file.txt"
print("new_file_path", new_file_path)
print("exists new_file_path", path.exists(new_file_path))

# path.isfile(path)
print("isfile", path.isfile(__file__))
print("path.dirname(__file__)", path.dirname(__file__))
print("isfile", path.isfile(path.dirname(__file__)))

# path.isdir(path)
print("isdir", path.isdir(__file__))
print("path.dirname(__file__)", path.dirname(__file__))
print("isdir", path.isdir(path.dirname(__file__)))

if path.isdir(__file__):
    print("code")

# path.islink(path)
# path.ismount(path)

# path.getsize(path)
print("getsize", path.getsize(__file__))

folder_path = path.dirname(__file__)
print("folder", folder_path)
list_file = ["new_folder", "new_folder_2", "new_file3.txt", ]

print(path.join(folder_path, *list_file))
print(path.join(folder_path, "new_folder", "new_folder_2", "new_file3.txt"))
print(path.join(folder_path, list_file[0], list_file[1], list_file[2]))

print(path.join("C:\\", "Users\\", "\\Voron", "PycharmProjects\\", "PythonBasic"))

project_path = path.dirname(path.dirname(__file__))
print("project_path", project_path)

print("item name\t isfolder")
for item in os.listdir(project_path):
    print("in folder:", item, "\t", path.isdir(path.join(project_path, item)))

# for folder_path, folder_name, filenames in os.walk(project_path):
#     print(folder_path, folder_name, filenames, sep="\t")
