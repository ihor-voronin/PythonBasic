import test_module
import modules_example_2

# from test_module import PI as t_PI
# from test_module import long_long_long_long_long_long_long_long_long_long_long_name as l_name
# from modules_example_2 import PI as m_PI

#
# PI = 5
#
# print(test_module.PI, modules_example_2.PI, PI, t_PI, m_PI)
#
#
# test_module.long_long_long_long_long_long_long_long_long_long_long_name()
# l_name()

import random
# import pprint

# from pprint import pprint
from pprint import *

import turtle_draw

import lesson_07_1
from lesson_10.sub_module.sub_file_with_code import print_something
from sub_module.sub_sub_module.file import print_hello

# pprint.pprint(str(dir()))
pprint(str(dir()))
print(__name__)

if __name__ == "__main__":
    turtle_draw.draw_rectangle()
    lesson_07_1.do_something()
    print_something()
    print_hello()
    modules_example_2.me_2_print()

