fantasy_names = """
    Melnoliar Zekhi 21
    Kisnamon Girqa 61
    Rugher Tageith 31
    Zator Gigbam 91
    Reghah Mocber 211
    Hehror Qrorrur 111
    Honorable Drirrin 42
    Composed Jyqhuqun 18
    Cook Rirqerrar 57
    Conjurer Prinkikis 17
"""


def split_large_string_into_lines(sting):
    lines = sting.strip("\n").split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i].strip(" ")
        # lines[i] = lines[i].replace(" ", "")
    return lines


lines = split_large_string_into_lines(fantasy_names)

print(lines)


def convert_line_to_dict(line):
    words = line.split(" ")
    return {"name": words[0], "second_name": words[1], "age": int(words[2])}


list_fantasy = list(map(convert_line_to_dict, lines))

print(list_fantasy)

list_fantasy.sort(key=lambda e: e['age'])
print(list_fantasy)

# import pprint
from pprint import pprint

pprint(list_fantasy)

# min(collection)
# max(collection)
# sum(collection)

list_num = [5, 6, 7, 1, 2]

print("min", min(list_num))
print("max", max(list_num))
print("sum", sum(list_num))

list_num2 = [
    [1, 12, 3],  # 12  # sum 16
    [1, 14, 3],  # 14  # sum 18
    [1, 7, 3],   # 7
    [1, 8, 3],   # 8
]

pprint(sorted(list_num2, key=lambda e: max(e)))
print("sum map", sum(map(sum, list_num2)))
for line in list_num2:
    print(line, sum(line)/len(line))
