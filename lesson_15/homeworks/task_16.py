def triangle_up(height, in_l=" ", in_r=" ", in_m=" "):
    for i in range(height):
        print(" " * (height - i), end="")
        if i != 0:
            print("*", end="")
            print(in_l * (i - 1), end="")
            print(in_m, end="")
            print(in_r * (i - 1), end="")
            print("*", end="")
        else:
            print("*", end="")
        print()
    print("*" * (height * 2 + 1))


def triangle_down(height, in_l=" ", in_r=" ", in_m=" "):
    for i in range(height - 1, -1, -1):
        print(" " * (height - i), end="")
        if i != 0:
            print("*", end="")
            print(in_l * (i - 1), end="")
            print(in_m, end="")
            print(in_r * (i - 1), end="")
            print("*", end="")
        else:
            print("*", end="")
        print()


if __name__ == "__main__":
    triangle_up(8)
    print()
    triangle_up(8, in_l="*", in_m="*", in_r="*")
    print()
    triangle_up(8, in_l=" ", in_m="*", in_r=" ")
    print()
    triangle_up(8, in_l="*", in_m="*", in_r="*")
    triangle_down(8)
    print()
    triangle_up(8, in_l="*", in_m="*", in_r="*")
    triangle_down(8, in_m="*")
    print()
