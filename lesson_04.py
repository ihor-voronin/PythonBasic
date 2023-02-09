# Ternary Operator
# if <condition>:
# ...<operand>

# <on_true> if <expression> else <on_false>
a = 20
b = "Hello world" if a < 20 else "another text"
print(b)

if a < 20:
    b = "Hello world"
else:
    b = "another text"
print(b)

# (<on_false>, <on_true>)[<expression>]
b = ("another text", "Hello world")[a < 20]
print(b)
# {True: <on_true>, False: <on_true>}[<expression>]
b = {True: "Hello world", False: "another text"}[a < 20]
print(b)

# Range function
# range(<start>, [stop], [step])
print(list(range(5, 10)))
print(list(range(10)))
print(list(range(5, 10, 2)))
num = 14
print(list(range(num, 0, -1)))
print(range(num, 0, -1))


# For lop
# for <variable_name> in <sequence>:
# ....<operand 1>
# ....<operand 2>
# .... ...
# ....<operand N>
print("for")
for num in range(0, 10):
    print(num, end=" ")
else:
    print("end")

print("while")
a = 0
while a < 10:
    print(a, end=" ")
    a += 1
else:
    print("end")
print("")
for i in range(1,3):
    for j in range(1,3):
        print(j*i, end=" ")
    print("")

# i = 1
# j = 1
# print 1* 1
# j = 2
# print 2 * 1
# print ""
# i = 2
# j = 1
# print 1 * 2
# j = 2
# print 2 * 2
# print ""
print("")
for i in 1, 2, 3:
    if i % 2 == 0:
        break
    print(i)
print("print num after loop", num)

print("")
for i in "s", "test", "text":
    print(i)


# for <variable_name> in <sequence>:
# ....<operand 1>
# ....<operand 2>
# .... ...
# ....<operand N>
# else:
# ....<operand>

text_var = "text"
text_var2 = 'text'
print(text_var == text_var2)
text_var3 = '''

text


    sadsa
fdsfds sada
dasfds sss
'''

print(text_var3)
text_var = "Hello world"
for char_symbol in text_var:
    print(char_symbol, end=" - ")


print("\n\n")
# Strings
# Special symbols
# \\
print("\\")
# \'
print('It\'s')
# \"
print('It\"s')
# \0
print('It\0')
# \a
print('It\a')
# \b
print('It\b')
# \f
print('It\f')
# \n
print('It\nIn')
# \r
print('It\ntext\rInText')
# \t
print('It\tIn')
# \v
print('It\vIn')
print('\u2764')
print('\U0001F60E')
print('\x42')
print("\120")
# \ooo            \120
# \u0000          \u2764
# \U00000000      \U000024C5
# \xhh            \x42

print(ord('P'))
print(chr(80))
print(hex(ord('P')))
print('\x50')
for char in "username":
    print(ord(char), end=" ")
print("")
for char in "1123":
    print(ord(char), end=" ")
print("")

path = 'C:\\Users\\Voron\\OneDrive\\Рабочий стол\\work'
path2 = r'C:\Users\Voron\OneDrive\Рабочий стол\work'
print(path)
print(path2)

# Concatenate string
string_1 = 'This message should appear on the console'
string_2 = 'So should this'
string_3 = 'And this, too'

string_concatenation = string_2 + string_3
print(string_concatenation)

# Multiply string
spam_string = ("spam" + " ") * 3
print(spam_string)

# Length of string
# len(<string>)
print(len(spam_string))
print(len(""))

# Access by index
#            01234
string_01 = "Hello"
#            H -5
#            e -4
#            l -3
#            l -2
#            o -1
print(string_01[-3])  # l
print(string_01[4])   # o
print(string_01[len(string_01) - 1])  # o
print(string_01[-1])  # o
print(string_01[-5])

# Slicing
string_01 = "Hello"
new_string = string_01[0:4]
print(new_string[0:4])

print(string_01[4:0:-1])
# string[<start>:<end>:<step>]
print(string_01[1:])
print(string_01[:2])
print(string_01[::2])  # H l o
print("678"[::-1])
# print(input("num:")[::-1])
# num_string = "567"
url_string = "https://docs.google.docs.com/presentation/"
sub_string = url_string[:6]
print(sub_string)


# <string1>.find(<string2>, [start], [stop])
# print(url_string.find("/"))
print(url_string[
      url_string.find("docs"):url_string.find("/", url_string.find("docs"))
      ])
# <string1>.rfind(<string2>, [start], [stop])
# print(url_string.rfind("docs"))
# print(url_string[:20])
# <string1>.index(<string2>, [start], [stop])
# print(url_string.index("docs"))
# <string1>.rindex(<string2>, [start], [stop])
# print(url_string.rindex("docs"))
# <string>.replace(<template>, <replacement>)
print(url_string.replace("o", "AAAA"))
# <string>.split(<template>)
string_text = "hello, world second"
print((string_text.split(" ")))
for word in string_text.split(" "):
    print("count: ", len(word), word)
# <string>.isdigit()
num_var = "5678"
print(string_text.isdigit())
print(num_var.isdigit())
# <string>.isalpha()
letters_var = "asdsada"
print(string_text.isalpha())
print(letters_var.isalpha())
print(num_var.isalpha())

# <string>.isalnum()
print("isalnum", "45dfs".isalnum())

# <string>.islower()
print("islower", string_text.islower())
# <string>.isupper()
print("isupper", string_text.isupper())
# <string>.isspace()
print("isspace", " ".isspace())
# <string>.istitle()
print("istitle", "Hi World no".istitle())
# <string>.upper()
print("upper", "Hi World no".upper())
# <string>.lower()
print("upper", "Hi World no".lower())
# <string1>.startswith(<string2>)
print("startswith", url_string.startswith("https"))
# <string1>.endswith(<string2>)
print("endswith", "Hi World no".endswith("no"))
# <string>.join(<sequence>)
print("join", " ".join(["Hello", "world"]))
# ord(<symbol>)
# chr(<number>)
# <string>.capitalize()
print("capitalize", "Hi World no".capitalize())
# <string>.center(<width>, [fill])
print("center", "Hi World no".center(100, '~'))
# <string1>.count(<string2>, [start], [stop])
print("count", "Hi World no World".count("world"))
# <string>.expandtabs(<tabsize>)
expandtabs_string = "Hi\tWorld\tno\tWorld"
new_str = expandtabs_string.expandtabs()
print("count", new_str)
# <string>.lstrip([chars])
print("lstrip", ".....Hi World no World ".lstrip("."))
# <string>.rstrip([chars])
print("rstrip", "Hi World no World ...".rstrip("."))
# <string>.strip([chars])
print("strip", "....Hi World no World ...".strip("."))
# <string>.partition(<template>)
print("partition", "....Hi World no World ...".partition("World"))
# <string>.rpartition(<separator>)
print("rpartition", "....Hi World no World ...".rpartition("World"))
# <string>.swapcase()
print("swapcase", "....Hi World no World ...".swapcase())
# <string>.title()
print("title", "....Hi world no World ...".title())
# <string>.zfill(<width>)
print("title", "....Hi world no World ...".zfill(100))
print("5678".zfill(12))
# <string>.ljust(<width>, [fillchar])
print("ljust", "....Hi world no World ...".ljust(100, "~"))
# <string>.rjust(<width>, [fillchar])
print("rjust", "....Hi world no World ...".rjust(100, "~"))
# <string>.format(*args, **kwargs)
number = 10
owner = "Me"
print("format", "{number} it's my number {owner}".format(number=number, owner=owner))
print("f-string", f"{number} it's my number {owner}")
print("print", number, "it's my number", owner)
